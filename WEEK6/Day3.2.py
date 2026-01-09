import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
from IPython.display import Markdown, display
from datetime import datetime
load_dotenv(override=True)

env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": env}

async def test_mcp():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        return await server.list_tools()

# mcp_tools = asyncio.run(test_mcp())

instructions = "You are able to search the web for information and briefly summarize the takeaways."
request = f"Please research the latest news on Amazon stock price and briefly summarize its outlook. \
For context, the current date is {datetime.now().strftime('%Y-%m-%d')}"
model = "gpt-4o-mini"

async def test_mcp_agent():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        display(Markdown(result.final_output))

asyncio.run(test_mcp_agent())

from market import get_share_price
# get_share_price("AAPL")

# no rate limiting concerns!

for i in range(1000):
    get_share_price("AAPL")
get_share_price("AAPL")