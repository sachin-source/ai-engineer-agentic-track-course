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