from dotenv import load_dotenv
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken

load_dotenv(override=True)

model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
ollamamodel_client = OllamaChatCompletionClient(model="llama3.2")

message = TextMessage(content="I'd like to go to London", source="user")
print(message)

agent = AssistantAgent(
    name="airline_agent",
    model_client=model_client,
    system_message="You are a helpful assistant for an airline. You give short, humorous answers.",
    model_client_stream=True
)

async def getResponse():
    return await agent.on_messages([message], cancellation_token=CancellationToken())

response = getResponse()
response.chat_message.content