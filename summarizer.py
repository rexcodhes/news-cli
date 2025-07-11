import os
import pathlib
import google.generativeai as genai
from dotenv import load_dotenv
from newspaper import Article

env_path = pathlib.Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def extract_article(url: str) -> str:
    art = Article(url)
    art.download()
    art.parse()
    return art.title + "\n\n" + art.text

def gemini_summary(text: str, max_tokens: int = 512) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = ("Summarise the following news article into 4-6 concise bullet points, retaining factual accuracy:\n\n"
              + text)
    response = model.generate_content(prompt, generation_config={"max_output_tokens": max_tokens})
    return response.text.strip()   
    