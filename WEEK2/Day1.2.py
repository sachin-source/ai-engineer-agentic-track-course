from dotenv import load_dotenv
from agents import Agent, Runner, trace
# The usual starting point

load_dotenv(override=True)


# Make an agent with name, instructions, model

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")

# Run the joke with Runner.run(agent, prompt) then print final_output

async def tell_joke():
    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
        print(result.final_output)

import asyncio
asyncio.run(tell_joke())