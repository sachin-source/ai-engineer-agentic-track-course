# Autogen by microsoft

## Main Concepts
- Model : Model is similar to LLM in other terms
- Message : It represent message between agents or events that happen with agent's interactions
- Agents : Agent
- Team : Group of agents to achieve common goal

## AutoGen Core
- An agent interaction framework
- Agnostic to agentinc abstraction
- Somewhat similar positioning to LangGraph
- But focus is on managing interactions between destributed and diverse agents

### AutoGen Core fundamental principle
- Decouples an agent's logic from how messages are delivered
- The framework handles creation & communication
- The Agents are responsible for their logic - that is not the remit of Autogen Core

### AutoGen Core runtime
- Standalone
- Distributed