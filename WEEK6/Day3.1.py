import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
from IPython.display import Markdown, display
from datetime import datetime
load_dotenv(override=True)

params = {"command": "npx","args": ["-y", "mcp-memory-libsql"],"env": {"LIBSQL_URL": "file:./memory/ed.db"}}

async def mcp_tools():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        return await server.list_tools()

# mcp_tools = asyncio.run(mcp_tools())

instructions = "You use your entity tools as a persistent memory to store and recall information about your conversations."
request = "My name's Ed. I'm an LLM engineer. I'm teaching a course about AI Agents, including the incredible MCP protocol. \
MCP is a protocol for connecting agents with tools, resources and prompt templates, and makes it easy to integrate AI agents with capabilities."
model = "gpt-4.1-mini"

async def mcp_with_agent():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, request)
        display(Markdown(result.final_output))
# asyncio.run(mcp_with_agent())

async def mcp_with_agent_and_time():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="agent", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("conversation"):
            result = await Runner.run(agent, "My name's Ed. What do you know about me?")
        display(Markdown(result.final_output))
# asyncio.run(mcp_with_agent_and_time())