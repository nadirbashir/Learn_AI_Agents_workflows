from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_x_post(topic: str) -> str:

    prompt = f"""
        You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).

        Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
        Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).

        Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.

        Here's the topic provided by the user for which you need to generate a post:
        <topic>
        {topic}
        </topic>

        Here are some examples of topics and generated posts:
        <examples>
            <example-1>
                <topic>
                Open LLMs are great because they are more than enough for many workflows and offer free use & 100% privacy!
                </topic>
                <generated-post>
                Yes, Gemini 2.5 pro is amazing. But form many tasks, it's too expensive & simply overkill.
                    
                Don't sleep on open LLMs which you can run locally on your MacBook!
                    
                Open LLMs like Gemma 3 can be run locally via Ollama or LM Studio, offer 100% privacy and
                are more than capable enough for most use-cases and workflows. 🚀
                </generated-post>
            </example-1>
            <example-1>
                <topic>
                Despite LLMs learn to code! Because AI-assisted coding > Vibe coding 
                </topic>
                <generated-post>
                There's never been a better time to learn coding! seriously!
                    
                Yes, you can vibe code sloppy apps all day.
                    
                If you want to build something that actually works, you need to learn code though.
                combine that with AI assistants like copilot and nothing's going to stop you!
                </generated-post>
            </example-1>
            
        </examples>

        Please use the tone, language, structure , and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
        Don't use the content from the examples!
"""
    response = client.responses.create(model="gpt-4o", input=prompt)

    return response.output_text


def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post: ")
    print(x_post)


if __name__ == "__main__":
    main()