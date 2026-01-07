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


playwright_params = {"command": "npx","args": [ "@playwright/mcp@latest"]}

async def mcp_playwright_tools():
    async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as server:
        return await server.list_tools()

playwright_tools = trace(mcp_playwright_tools)


sandbox_path = os.path.abspath(os.path.join(os.getcwd(), "sandbox"))
files_params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}

async def mcp_file_tools():
    async with MCPServerStdio(params=files_params,client_session_timeout_seconds=60) as server:
        return await server.list_tools()

file_tools = trace(mcp_file_tools)