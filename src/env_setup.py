import os
from dotenv import load_dotenv
import google.generativeai as genai
import warnings

warnings.filterwarnings("ignore")

def configure_google_api():
    """
    Configures the environment to use Google's Generative AI using the API key from the .env file.
    """
    load_dotenv()  # Load environment variables from the .env file
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Set GOOGLE_API_KEY in the .env file.")
    genai.configure(api_key=api_key)
