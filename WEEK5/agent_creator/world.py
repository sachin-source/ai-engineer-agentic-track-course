from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost
from agent import Agent
from creator import Creator
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime
from autogen_core import AgentId
import messages
import asyncio

HOW_MANY_AGENTS = 20

async def create_and_message(worker, creator_id, i: int):
    try:
        result = await worker.send_message(messages.Message(content=f"agent{i}.py"), creator_id)
        with open(f"idea{i}.md", "w") as f:
            f.write(result.content)
    except Exception as e:
        print(f"Failed to run worker {i} due to exception: {e}")
