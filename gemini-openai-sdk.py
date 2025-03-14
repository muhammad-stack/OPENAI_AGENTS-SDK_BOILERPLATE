import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel , Runner , set_tracing_disabled
import os


load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name = "Assistant",
        instructions = "You only respond in haikus",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
    )

    result = await Runner.run(
        agent,
        "Tell me about yourself in programming"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())