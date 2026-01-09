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

mcp_tools = asyncio.run(test_mcp())