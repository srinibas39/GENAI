from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
# client = OpenAI(OPENAI_API_KEY)

# response = client.responses.create(
#     model="gpt-3.5",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)