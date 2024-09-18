from openai import OpenAI
import json
import pandas as pd
import base64
import os

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Load examples from a JSON file
with open("input_data/dataset.json", "r") as file:
    examples = json.load(file)

# Initialize an empty DataFrame with the necessary columns
columns = ["ID", "Image Filename", "Caption", "Process Flow", "FR #1", "FR #2", "FR #3", "FR #4", "FR #5", "FR #6",
           "FR #7", "FR #8", "FR #9", "FR #10"]
output_df = pd.DataFrame(columns=columns)

# Directory where images are stored
image_directory = "TA_Screens_RF/"

# Iterate through each example
for example in examples:
    # Get the image file path
    image_path = os.path.join(image_directory, example["Image Filename"])

    # Encode the image in base64
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Send the example and encoded image to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a computer science student with no experience. You are learning to elicit "
                           "requirements. Format your answer with the same fields, style of writing, and depth of "
                           "detail as in the examples."
            },
            {
                "role": "user",
                "content": f"Identify the Functional Requirements (FR) from this mockup screenshot. Focus only on the "
                           f"main functionality specifically, with no additional functionalities related to the "
                           f"overall user interface and experience.\n{json.dumps(example)}",
                "name": "mockup_example"
            },
            {
                "role": "user",
                "content": f"data:image/png;base64,{encoded_image}",
                "name": "mockup_image"
            }
        ],
        temperature=0.5,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Parse the response from the assistant
    response_content = response['choices'][0]['message']['content']

    # Convert the generated response into a dictionary
    generated_data = json.loads(response_content.strip("```json\n").strip("\n```"))

    # Append the generated data to the DataFrame
    output_df = output_df.append(generated_data, ignore_index=True)

# Save the DataFrame to a CSV file
output_df.to_csv("results/baseline_requirements.csv", index=False)

print("Batch processing completed, and results saved to baseline_requirements.csv")