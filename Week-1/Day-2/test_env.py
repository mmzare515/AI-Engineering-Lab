from dotenv import load_dotenv # type: ignore
import os

# Load environment variables
load_dotenv()

# Retrieve variables
api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL")

# Validation
if not api_key:
    raise ValueError("API key was not found in the .env file.")

if not model:
    raise ValueError("MODEL variable is missing.")

# Safe output
print("Environment variables loaded successfully.")
print(f"Selected model: {model}")