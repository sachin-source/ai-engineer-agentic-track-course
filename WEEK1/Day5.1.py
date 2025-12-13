# imports

from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import requests
from pypdf import PdfReader
import gradio as gr

# The usual start

load_dotenv(override=True)
openai = OpenAI()