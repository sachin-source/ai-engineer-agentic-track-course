from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class PushNotification(BaseModel):
    """A message to be sent to the User"""
    argument: str = Field(..., description="Description of the argument.")

class PushNotificationTool(BaseTool):
    

    name: str = "Send a Push Notification"
    description: str = (
        "This tool is used to send a push notification to the user."
    )
    args_schema: Type[BaseModel] = PushNotification

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
