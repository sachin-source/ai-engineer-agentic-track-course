from dotenv import load_dotenv
from agents import Agent, Runner, trace
# The usual starting point

load_dotenv(override=True)


# Make an agent with name, instructions, model

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")