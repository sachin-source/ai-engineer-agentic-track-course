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

async def async_mcp_account_manager():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="account_manager", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("account_manager"):
            result = await Runner.run(agent, request)
        display(Markdown(result.final_output))

asyncio.run(async_mcp_account_manager())

from accounts_client import get_accounts_tools_openai, read_accounts_resource, list_accounts_tools

async def read_mcp_accounts_resource():
    return await read_accounts_resource()

mcp_tools = asyncio.run(read_mcp_accounts_resource())
print(mcp_tools)

async def get_mcp_accounts_tools_openai():
    return await get_accounts_tools_openai()

openai_tools = asyncio.run(get_mcp_accounts_tools_openai())
print(openai_tools)

request = "My name is Ed and my account is under the name Ed. What's my balance?"

async def test_mcp_account_client():
    with trace("account_mcp_client"):
        agent = Agent(name="account_manager", instructions=instructions, model=model, tools=openai_tools)
        result = await Runner.run(agent, request)
        display(Markdown(result.final_output))

asyncio.run(test_mcp_account_client())

async def read_ed_account():
    return await read_accounts_resource("ed")

context = asyncio.run(read_ed_account())
print(context)