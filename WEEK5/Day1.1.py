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

import os
import sqlite3

# Delete existing database file if it exists
if os.path.exists("tickets.db"):
    os.remove("tickets.db")

# Create the database and the table
conn = sqlite3.connect("tickets.db")
c = conn.cursor()
c.execute("CREATE TABLE cities (city_name TEXT PRIMARY KEY, round_trip_price REAL)")
conn.commit()
conn.close()

# Populate our database
def save_city_price(city_name, round_trip_price):
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute("REPLACE INTO cities (city_name, round_trip_price) VALUES (?, ?)", (city_name.lower(), round_trip_price))
    conn.commit()
    conn.close()

# Some cities!
save_city_price("London", 299)
save_city_price("Paris", 399)
save_city_price("Rome", 499)
save_city_price("Madrid", 550)
save_city_price("Barcelona", 580)
save_city_price("Berlin", 525)