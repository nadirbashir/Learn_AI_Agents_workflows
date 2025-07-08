from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI() #loads environment variable automatically if env name is OPENAI_API_KEY otherwise load manually

def generate_x_post(topic: str) -> str:
    prompt = f"""
        You are a senior technical writer and developer educator who specializes in creating clear, practical, and beginner-friendly tutorials.

        Your job is to generate a step-by-step guide for the topic provided by the user. Your tutorial should:

        Begin with a brief explanation of what the topic is and why it matters.
        Follow with clear, numbered steps.
        Include code snippets or examples where applicable.
        Avoid unnecessary jargon — explain concepts simply.
        Use headings and subheadings to organize content logically.
        Finish with a short recap or tips for next steps.
        
        Make sure the tutorial is beginner-friendly but technically correct, and keep it concise and engaging.

        Here's the topic provided by the user for which you need to generate a tutorial:
        <topic>
        {topic}
        </topic>
"""
    response = client.responses.create(model="gpt-4o", input=prompt)

    return response.output_text


def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post:")
    print(x_post)


if __name__ == "__main__":
    main()