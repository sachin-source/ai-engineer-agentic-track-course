# Lang graph from lang chain

## Terminologies
- Agent workflows are represented as **graphs**
- **State** represent the current snapshot of the application
- **Nodes** are python functions that represent agentic logic; They receive the current *state* as input, do something, and return an updated *state*.
- **Edges** are python functions that determine which *Node* to execute next based on the *State*. They can be conditional or fixed.  
Nodes do the work  
Edges choose what to do next
