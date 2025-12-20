# Crew running notes

### Flowors
* Crews : Autonomous solutions with AI teams of agents with different roles  
For autonomous problem solving, creative collaboration, or exploratory tasks

* Flows : Structured automations by dividing complex tasks into precise workflows  
For deterministic outcomes, auditability, or precise control over execution

### Core concepts
* Agent : An autonomous unit, with an LLM, a role, a goal, a backstory, memory, tools.
* Task : A specific assignment to be carried out, with a description, expected output, agent.
* Crew : A team of *Agents* and *Tasks*; either :  
Sequential : run tasks in order they are defined  
Hierarchical : use a manager LLM to assign

### Yaml configuration
*Agent* and *Tasks* can be created by code, setting the backstory, description, expected output, etc  
or you can define each in a YAML file that's provided when you create the code.