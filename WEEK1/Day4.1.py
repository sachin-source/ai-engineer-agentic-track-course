# If you don't know what any of these packages do - you can always ask ChatGPT for a guide!

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr

load_dotenv(override=True)
openai = OpenAI()

reader = PdfReader("me/linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

print(linkedin)
with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()