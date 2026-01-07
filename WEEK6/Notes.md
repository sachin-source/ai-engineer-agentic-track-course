# MCP - Model Context Protocol
## MCP Core Concepts
- **Host** is an LLM app like claude or our Agent architecture
- **MCP Client** lives inside Host and connects 1:1 to MCP Server
- **MCP Server** provides tools, context and prompts

## Notes
- MCP servers most often run on your box - Download open-source MCP Servers, run them locally

## Transport Mechanisms
- STDIO : spawns a process and communicates via standard input/output
- SSE : Server Sent Events - uses HTTPS connections with streaming