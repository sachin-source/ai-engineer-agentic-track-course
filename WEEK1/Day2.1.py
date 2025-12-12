# Start with imports - ask ChatGPT to explain any package that you don't know

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from IPython.display import Markdown, display

# Always remember to do this!
load_dotenv(override=True)

# Print the key prefixes to help with any debugging
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]

openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=messages,
)
question = response.choices[0].message.content
print(question)

competitors = []
answers = []
messages = [{"role": "user", "content": question}]

# The API we know well
# I've updated this with the latest model, but it can take some time because it likes to think!
# Replace the model with gpt-4.1-mini if you'd prefer not to wait 1-2 mins

model_name = "gpt-5-nano"

response = openai.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

# Anthropic has a slightly different API, and Max Tokens is required

model_name = "claude-sonnet-4-5"

claude = Anthropic()
response = claude.messages.create(model=model_name, messages=messages, max_tokens=1000)
answer = response.content[0].text

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.5-flash"

response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

deepseek = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com/v1")
model_name = "deepseek-chat"

response = deepseek.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

# Updated with the latest Open Source model from OpenAI

groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
model_name = "openai/gpt-oss-120b"

response = groq.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
model_name = "llama3.2"

response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)