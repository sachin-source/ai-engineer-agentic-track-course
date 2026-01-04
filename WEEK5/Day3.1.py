from dataclasses import dataclass
from autogen_core import AgentId, MessageContext, RoutedAgent, message_handler
from autogen_core import SingleThreadedAgentRuntime
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv(override=True)

# Let's have a simple one!
@dataclass
class Message:
    content: str

class SimpleAgent(RoutedAgent):
    def __init__(self) -> None:
        super().__init__("Simple")

    @message_handler
    async def on_my_message(self, message: Message, ctx: MessageContext) -> Message:
        """Handles messages sent to this agent. AutoGen will route messages based on the input type."""
        return Message(content=f"This is {self.id.type}-{self.id.key}. You said '{message.content}' and I disagree.")

# Register the agent in the runtime; SingleThreadedAgentRuntime is for STANDALONE
runtime = SingleThreadedAgentRuntime()
async def agent_registeration():
    await SimpleAgent.register(runtime, "simple_agent", lambda: SimpleAgent())

agent_registeration()

runtime.start()

agent_id = AgentId("simple_agent", "default")

async def send_message(message: Message, agent_id: AgentId):
    return await runtime.send_message(message, agent_id)

response = send_message(Message("Well hi there!"), agent_id)
print(">>>", response.content)

async def shutdown():
    await runtime.stop()
    await runtime.close()

shutdown()