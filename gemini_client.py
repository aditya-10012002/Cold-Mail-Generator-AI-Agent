import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

class GeminiClient:
    def __init__(self):
        # Initialize the Gen AI client with your API key
        self.client = genai.Client(api_key=API_KEY)

    def generate(self, prompt: str, model: str = 'gemini-2.0-flash') -> str:
        response = self.client.models.generate_content(
            model=model,
            contents=[prompt],
            config=types.GenerateContentConfig(temperature=0.7, max_output_tokens=512)
        )
        return response.text