from dotenv import load_dotenv
load_dotenv(override=True)

from autogen_ext.models.openai import OpenAIChatCompletionClient
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

from autogen_ext.models.ollama import OllamaChatCompletionClient
ollamamodel_client = OllamaChatCompletionClient(model="llama3.2")