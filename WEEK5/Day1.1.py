from dotenv import load_dotenv
load_dotenv(override=True)

from autogen_ext.models.openai import OpenAIChatCompletionClient
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

from autogen_ext.models.ollama import OllamaChatCompletionClient
ollamamodel_client = OllamaChatCompletionClient(model="llama3.2")

from autogen_agentchat.messages import TextMessage
message = TextMessage(content="I'd like to go to London", source="user")
print(message)