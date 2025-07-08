import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_post(topic: str) -> str:
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = types.Content(
        role='user',
        parts=[types.Part.from_text(text=topic)]
        ),
        config = types.GenerateContentConfig(
            system_instruction = """
            You are an expert social media manager, and you excel at crafting viral and high engaging posts for X (formerly Twitter).
            Follow these rules:
            1. Generate post that is concise, impactful, and tailored to the topic provided by the user.
            2. Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).
            3. Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
        """
        )
    )
    return response.text

def main():
    usr_input = input("what should be the post about?")
    x_post = generate_post(usr_input)
    print(x_post)
if __name__ == "__main__":
    main()