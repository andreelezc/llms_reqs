from openai import OpenAI
import os

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

url = "https://github.com/andreelezc/llms_reqs/blob/master/screenshots/mockup_001.png?raw=true"

prompt = """
Analyze the following app screen and list its functional requirements (FR) in detail.
Format your answer as: FR#{i}: The system must {requirement}. Provide only the list of requirements
"""

sg_prompt = """Generate a scene graph for this app mockup, identifying the objects (UI components) and 
their relationships. Provide this as a structured JSON output. Do not add additional text, only provide the JSON."
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": sg_prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    },
                },
            ],
        }
    ],
    temperature=0.2,
    max_tokens=1000,
)

print(response.choices[0])
