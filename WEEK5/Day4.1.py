from dataclasses import dataclass
from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.langchain import LangChainToolAdapter
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from IPython.display import display, Markdown

from dotenv import load_dotenv

load_dotenv(override=True)

ALL_IN_ONE_WORKER = False

@dataclass
class Message:
    content: str

from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost

host = GrpcWorkerAgentRuntimeHost(address="localhost:50051")
host.start()

serper = GoogleSerperAPIWrapper()
langchain_serper =Tool(name="internet_search", func=serper.run, description="Useful for when you need to search the internet")
autogen_serper = LangChainToolAdapter(langchain_serper)

instruction1 = "To help with a decision on whether to use AutoGen in a new AI Agent project, \
please research and briefly respond with reasons in favor of choosing AutoGen; the pros of AutoGen."

instruction2 = "To help with a decision on whether to use AutoGen in a new AI Agent project, \
please research and briefly respond with reasons against choosing AutoGen; the cons of Autogen."

judge = "You must make a decision on whether to use AutoGen for a project. \
Your research team has come up with the following reasons for and against. \
Based purely on the research from your team, please respond with your decision and brief rationale."