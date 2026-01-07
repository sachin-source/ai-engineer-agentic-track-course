# The imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os

load_dotenv(override=True)

fetch_params = {"command": "uvx", "args": ["mcp-server-fetch"]}

async def mcp_fetch_tools():
    async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=60) as server:
        return await server.list_tools()

fetch_tools = trace(mcp_fetch_tools)