from dotenv import load_dotenv
import os

load_dotenv()

AI_API_KEY = os.getenv("GROQ_API_KEY")
if not AI_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")