# Start with imports - ask ChatGPT to explain any package that you don't know

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from IPython.display import Markdown, display

# Always remember to do this!
load_dotenv(override=True)