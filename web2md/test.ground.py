# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

HERE = Path(__file__).parent


load_dotenv(dotenv_path=HERE.parent/'.envs')

def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-lite-preview-06-17"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""查询最新关于伊朗和以色列的新闻"""),
            ],
        )
    ]
    config = types.GenerateContentConfig(

        tools=[types.Tool(
            google_search=types.GoogleSearch()
        )]
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Who won the euro 2024?",
        config=config,
    )

    # Print the grounded response
    print(response.text)
    print(response.to_json_dict())

if __name__ == "__main__":
    generate()
