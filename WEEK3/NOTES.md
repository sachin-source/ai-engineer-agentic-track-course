# Crew running notes
## Theory or explainatory part
### Flowors
- Crews : Autonomous solutions with AI teams of agents with different roles  
For autonomous problem solving, creative collaboration, or exploratory tasks

- Flows : Structured automations by dividing complex tasks into precise workflows  
For deterministic outcomes, auditability, or precise control over execution

### Core concepts
- Agent : An autonomous unit, with an LLM, a role, a goal, a backstory, memory, tools.
- Task : A specific assignment to be carried out, with a description, expected output, agent.
- Crew : A team of **Agents** and **Tasks**; either :  
Sequential : run tasks in order they are defined  
Hierarchical : use a manager LLM to assign
- Tools : Equiping agents with capabilities
- context : Information passed from 1 task to another

### Yaml configuration
**Agent** and **Tasks** can be created by code, setting the backstory, description, expected output, etc  
or you can define each in a YAML file that's provided when you create the code.

### crew.py
It all comes together with a Crew definition with decorators:
- @CrewBase is annotated for class
- @agent is annotated for agent definitions
- @task is annotated for task definitions
- @crew is annotated to the final function that generates Crew

### LLMs
CrewAI uses the super simple framework - **LiteLLM** under the hood to interface with almost any LLM; set keys in .env file

### Memory - more perspective
- Short-Term memory : Temporarily stores recent interactions and outcomes using RAG, enabling agents to access relevant information during the current executions
- Long-term memory : Preserves valuable insights and learnings, building knowledge over time
- Entity memory : Information about people, places and concepts encountered during tasks, facilitating deeper understanding and relationship mapping. Uses RAG for storing entity information
- Contextual memory :Maintains the context of interactions by combining all the above

## Installation and project setup
- Install crewAI using UV - **uv tool install crewai**
- Create a new project with - **crewai create my_project**
- Run with **crewai run**         