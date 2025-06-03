from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# Set and validate API key
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("Please add your API key to the .env file as GEMINI_API_KEY=your_key_here")

def Generate_Response(prompt):
    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction = """
            You are a skilled movie synopsis writer. Your task is to:
            - Create engaging, concise summaries of movie plots
            - Keep summaries between 30-50 words
            - Focus on the main plot points and core themes
            - Maintain the movie's genre tone
            - Avoid major spoilers and plot twists
            - Use descriptive language that captures the movie's essence
            """,
            responseModalities = ["TEXT"]
            ),
        contents=[prompt]
    )
    return response.text

# prompt = input("Ask Ai: ")
# response = Generate_Response(prompt)
