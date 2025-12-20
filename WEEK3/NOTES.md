# Crew running notes

### Core concepts
* Agent : An autonomous unit, with an LLM, a role, a goal, a backstory, memory, tools.
* Task : A specific assignment to be carried out, with a description, expected output, agent.
* Crew : A team of *Agents* and *Tasks*; either :  
Sequential : run tasks in order they are defined  
Hierarchical : use a manager LLM to assign
