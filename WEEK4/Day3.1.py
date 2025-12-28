from typing import Annotated
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from IPython.display import Image, display
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
import requests
import os
from langchain_openai import ChatOpenAI
from typing import TypedDict

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool

# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)

serper = GoogleSerperAPIWrapper()
# serper.run("What is the capital of France?")

tool_search =Tool(
        name="search",
        func=serper.run,
        description="Useful for when you need more information from an online search"
    )

# tool_search.invoke("What is the capital of France?")