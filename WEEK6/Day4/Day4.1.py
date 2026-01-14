import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, Tool
from agents.mcp import MCPServerStdio
from IPython.display import Markdown, display
from datetime import datetime
from accounts_client import read_accounts_resource, read_strategy_resource
from accounts import Account
import asyncio

load_dotenv(override=True)

polygon_api_key = os.getenv("POLYGON_API_KEY")
polygon_plan = os.getenv("POLYGON_PLAN")

is_paid_polygon = polygon_plan == "paid"
is_realtime_polygon = polygon_plan == "realtime"

print(is_paid_polygon)
print(is_realtime_polygon)

if is_paid_polygon or is_realtime_polygon:
    market_mcp = {"command": "uvx","args": ["--from", "git+https://github.com/polygon-io/mcp_polygon@master", "mcp_polygon"], "env": {"POLYGON_API_KEY": polygon_api_key}}
else:
    market_mcp = ({"command": "uv", "args": ["run", "market_server.py"]})

trader_mcp_server_params = [
    {"command": "uv", "args": ["run", "accounts_server.py"]},
    {"command": "uv", "args": ["run", "push_server.py"]},
    market_mcp
]

brave_env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}

researcher_mcp_server_params = [
    {"command": "uvx", "args": ["mcp-server-fetch"]},
    {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": brave_env}
]

researcher_mcp_servers = [MCPServerStdio(params, client_session_timeout_seconds=30) for params in researcher_mcp_server_params]
trader_mcp_servers = [MCPServerStdio(params, client_session_timeout_seconds=30) for params in trader_mcp_server_params]
mcp_servers = trader_mcp_servers + researcher_mcp_servers

async def get_researcher(mcp_servers) -> Agent:
    instructions = f"""You are a financial researcher. You are able to search the web for interesting financial news,
look for possible trading opportunities, and help with research.
Based on the request, you carry out necessary research and respond with your findings.
Take time to make multiple searches to get a comprehensive overview, and then summarize your findings.
If there isn't a specific request, then just respond with investment opportunities based on searching latest news.
The current datetime is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    researcher = Agent(
        name="Researcher",
        instructions=instructions,
        model="gpt-4.1-mini",
        mcp_servers=mcp_servers,
    )
    return researcher

async def get_researcher_tool(mcp_servers) -> Tool:
    researcher = await get_researcher(mcp_servers)
    return researcher.as_tool(
            tool_name="Researcher",
            tool_description="This tool researches online for news and opportunities, \
                either based on your specific request to look into a certain stock, \
                or generally for notable financial news and opportunities. \
                Describe what kind of research you're looking for."
        )

async def test_mcp_connection():
    research_question = "What's the latest news on Amazon?"

    for server in researcher_mcp_servers:
        await server.connect()
    researcher = await get_researcher(researcher_mcp_servers)
    with trace("Researcher"):
        result = await Runner.run(researcher, research_question, max_turns=30)
    display(Markdown(result.final_output))

asyncio.run(test_mcp_connection())

async def get_account_resource(name: str):
    return await read_accounts_resource(name)

async def get_strategy_resource(name: str):
    return await read_strategy_resource(name)

async def reset_trader_acc():
    ed_initial_strategy = "You are a day trader that aggressively buys and sells shares based on news and market conditions."
    Account.get("Ed").reset(ed_initial_strategy)

    display(Markdown(get_account_resource("Ed")))
    display(Markdown(get_strategy_resource("Ed")))


asyncio.run(reset_trader_acc())

agent_name = "Ed"

# Using MCP Servers to read resources
account_details = asyncio.run(get_account_resource(agent_name))
strategy = asyncio.run(get_strategy_resource(agent_name))

instructions = f"""
You are a trader that manages a portfolio of shares. Your name is {agent_name} and your account is under your name, {agent_name}.
You have access to tools that allow you to search the internet for company news, check stock prices, and buy and sell shares.
Your investment strategy for your portfolio is:
{strategy}
Your current holdings and balance is:
{account_details}
You have the tools to perform a websearch for relevant news and information.
You have tools to check stock prices.
You have tools to buy and sell shares.
You have tools to save memory of companies, research and thinking so far.
Please make use of these tools to manage your portfolio. Carry out trades as you see fit; do not wait for instructions or ask for confirmation.
"""

prompt = """
Use your tools to make decisions about your portfolio.
Investigate the news and the market, make your decision, make the trades, and respond with a summary of your actions.
"""

# print(instructions)

async def run_trader_with_mcp():
    for server in mcp_servers:
        await server.connect()

    researcher_tool = await get_researcher_tool(researcher_mcp_servers)
    trader = Agent(
        name=agent_name,
        instructions=instructions,
        tools=[researcher_tool],
        mcp_servers=trader_mcp_servers,
        model="gpt-4o-mini",
    )
    with trace(agent_name):
        result = await Runner.run(trader, prompt, max_turns=30)
    display(Markdown(result.final_output))

asyncio.run(run_trader_with_mcp())

# And let's look at the results of the trading
async def read_acc_resource():
    await read_accounts_resource(agent_name)

from traders import Trader
trader = Trader("Ed")

async def run_trader():
    await trader.run()
    await read_accounts_resource("Ed")

asyncio.run(run_trader())