# MCP Server – Complete Notes  
**(Model Context Protocol Server)**

---

## Overview

These are **complete, exam-ready + practical notes on MCP Server (Model Context Protocol Server)** — written in a **clear, layered way** so you can use them for:

- 📚 Learning  
- 🔁 Revision  
- 💼 Interviews  
- 🛠️ Real-world projects  

---

## What is MCP?

**MCP (Model Context Protocol)** is an **open protocol** that allows **LLMs (Large Language Models)** to securely and consistently **access external tools, data, and services** through a standardized interface.

> 💡 Think of MCP as **USB-C for AI tools**

- One protocol  
- Many tools  
- Any LLM can plug in  

---

## Why MCP Was Needed

### Problems Before MCP

- Every AI tool had a **custom API**
- Tight coupling between:
  - LLM ↔ Tool
- Difficult to:
  - Reuse tools
  - Switch models
  - Secure access

### Solutions Provided by MCP

- ✅ Standard tool interface  
- ✅ Model-agnostic  
- ✅ Secure context handling  
- ✅ Easy extensibility  

---

## What is an MCP Server?

An **MCP Server** is a backend service that:

- Exposes **tools, data, or capabilities**
- Follows the **MCP specification**
- Communicates with:
  - MCP clients (ChatGPT, Claude, IDEs, AI agents)

> **In simple words:**  
> **MCP Server = Tool provider for AI models**

---

## MCP Architecture
LLM (Client)
↓
MCP Client
↓
MCP Server
↓
Tools / APIs / Databases / Files

---

## MCP Server Responsibilities

An MCP Server must:

1. Advertise available tools  
2. Describe tool schemas  
3. Receive tool invocation requests  
4. Execute the tool  
5. Return structured results  

---

## Key MCP Concepts

### Tools

A **tool** is a function that the LLM can call.

**Examples:**
- Search databases
- Read files
- Call REST APIs
- Run shell commands
- Query GitHub

Each tool includes:
- Name  
- Description  
- Input schema  
- Output schema  

---

### Resources

Static or semi-static data sources:
- Files  
- Logs  
- Documents  
- Configuration data  

---

### Prompts

Reusable system instructions that:
- Guide LLM behavior  
- Add contextual grounding  

---

## MCP Communication Model

MCP uses **JSON-RPC** over:
- STDIO  
- HTTP  
- WebSocket  

### Typical Request Flow

1. LLM decides to use a tool  
2. MCP Client sends request  
3. MCP Server executes the tool  
4. Server returns response  
5. LLM continues reasoning  

---

## MCP Server Lifecycle

1. Server starts  
2. Tools are registered  
3. Server waits for requests  
4. Executes tools  
5. Sends results  
6. Logs activity and handles errors  

---

## MCP Server Tool Definition Example

```json
{
  "name": "get_weather",
  "description": "Get current weather for a city",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": { "type": "string" }
    },
    "required": ["city"]
  }
}
MCP Server Execution Example
{
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "city": "Mumbai"
    }
  }
}
Response
{
  "temperature": "32°C",
  "condition": "Sunny"
}

Security in MCP Server
Security Features

Tool access control

Scoped permissions

No arbitrary execution unless explicitly allowed

Explicit tool exposure

Best Practices

✅ Never expose unrestricted shell access

✅ Validate all inputs

✅ Sanitize outputs

✅ Log every tool call

MCP vs Traditional APIs
| Feature           | Traditional API   | MCP Server         |
| ----------------- | ----------------- | ------------------ |
| Client            | Fixed application | Any LLM            |
| Tool discovery    | Manual            | Automatic          |
| Schema            | Informal          | Strict JSON Schema |
| Context awareness | ❌                 | ✅                  |
| Reusability       | Low               | High               |


MCP Server Use Cases:
AI coding assistants
DevOps automation
Data analysis agents
Embedded AI systems
IDE integrations
Chatbots with live data
MCP Server Languages & Frameworks

Commonly used languages:
Node.js
Python
Rust
Go

Official SDKs:
@modelcontextprotocol/sdk
mcp-python
Simple MCP Server (Node.js Example)
import { Server } from "@modelcontextprotocol/sdk/server";

const server = new Server({
  name: "demo-mcp-server",
  version: "1.0.0"
});

server.tool("hello", async ({ name }) => {
  return `Hello ${name}`;
});

server.start();
MCP Server vs Plugins
| Aspect          | MCP | Plugins |
| --------------- | --- | ------- |
| Standardized    | ✅   | ❌       |
| Model-agnostic  | ✅   | ❌       |
| Local execution | ✅   | ❌       |
| Open protocol   | ✅   | ❌       |


Advantages of MCP Server

✅ Vendor-neutral

✅ Scalable

✅ Secure

✅ Modular

✅ Future-proof

Limitations

⚠ Requires proper schema design

⚠ Ecosystem still evolving

⚠ Security must be handled carefully

MCP in the AI Ecosystem

MCP acts as a bridge between:

🧠 Reasoning (LLMs)

🛠️ Execution (real systems)

MCP = Brain ↔ Hands of AI