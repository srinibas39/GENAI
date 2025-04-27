from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Why is sky blue?"
)
print(response.text)

