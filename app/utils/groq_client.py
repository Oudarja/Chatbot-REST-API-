# app/utils/groq_client.py
import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_LLM_MODEL = os.getenv("GROQ_LLM_MODEL")

client = Groq(api_key=GROQ_API_KEY)

async def generate_response(prompt: str) -> str:
    completion = client.chat.completions.create(
        model=GROQ_LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return completion.choices[0].message.content
