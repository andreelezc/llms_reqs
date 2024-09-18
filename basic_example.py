from openai import OpenAI
import os

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

url = "https://drive.google.com/file/d/1-mkSEruCH_yCmKkp99AqecMhTjvp-tjF/view?usp=drive_link"

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://drive.google.com/file/d/1-mkSEruCH_yCmKkp99AqecMhTjvp-tjF"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])