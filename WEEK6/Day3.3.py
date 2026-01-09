import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
from IPython.display import Markdown, display
from datetime import datetime
from polygon import RESTClient

load_dotenv(override=True)

polygon_api_key = os.getenv("POLYGON_API_KEY")
if not polygon_api_key:
    print("POLYGON_API_KEY is not set")

client = RESTClient(polygon_api_key)
client.get_previous_close_agg("AAPL")[0]