from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
# Old - decommissioned
MODEL_NAME: str = "llama3-8b-8192"

# New - current and fast
MODEL_NAME: str = "llama-3.3-70b-versatile"
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env file")