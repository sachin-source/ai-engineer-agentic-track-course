# The imports

import asyncio
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

instructions = """
You browse the internet to accomplish your instructions.
You are highly capable at browsing the internet independently to accomplish your task, 
including accepting all cookies and clicking 'not now' as
appropriate to get to the content you need. If one website isn't fruitful, try another. 
Be persistent until you have solved your assignment,
trying different options and sites as needed.
"""

async def agent_with_mcp_servers():
    async with MCPServerStdio(params=files_params, client_session_timeout_seconds=60) as mcp_server_files:
        async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as mcp_server_browser:
            agent = Agent(
                name="investigator", 
                instructions=instructions, 
                model="gpt-4.1-mini",
                mcp_servers=[mcp_server_files, mcp_server_browser]
                )
            with trace("investigate"):
                result = await Runner.run(agent, "Find a great recipe for Banoffee Pie, then summarize it in markdown to banoffee.md")
                print(result.final_output)

asyncio.run(agent_with_mcp_servers())