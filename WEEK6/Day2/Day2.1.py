import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from IPython.display import display, Markdown

load_dotenv(override=True)

from accounts import Account

# account = Account.get("Ed")
# account

# account.buy_shares("AMZN", 3, "Because this bookstore website looks promising")
# account.report()
# account.list_transactions()

# Now let's use our accounts server as an MCP server

params = {"command": "uv", "args": ["run", "accounts_server.py"]}
async def run_mcp_server():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        return await server.list_tools()

mcp_tools = asyncio.run(run_mcp_server())

instructions = "You are able to manage an account for a client, and answer questions about the account."
request = "My name is Ed and my account is under the name Ed. What's my balance and my holdings?"
model = "gpt-4.1-mini"