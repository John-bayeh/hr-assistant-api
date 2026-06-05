from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("✓ API key loaded successfully")
    print(f"Key starts with: {api_key[:8]}...")
else:
    print("✗ API key not found")