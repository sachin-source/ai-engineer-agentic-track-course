from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class FinancialResearcher():
    """FinancialResearcher crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
