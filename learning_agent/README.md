# Simple Learning AI Agent

A basic AI agent that learns from user interactions and stores knowledge in memory.

## Features

- **Learn**: Store information about topics
- **Recall**: Retrieve learned information
- **Persistent Memory**: Saves knowledge to `agent_memory.json`
- **Interactive**: Chat-like interface

## Installation

```bash
python learning_agent/agent.py
```

## Usage

```
You: learn Python: A programming language
Agent: ✓ Learned: Python

You: tell me about Python
Agent: A programming language

You: what do you know?
Agent: I know about: Python

You: stats
Agent: Agent Stats: {...}
```

## Commands

| Command | Example |
|---------|----------|
| Learn | `learn [topic]: [information]` |
| Recall | `tell me about [topic]` |
| List | `what do you know?` |
| Stats | `stats` |
| Exit | `exit` |

## How It Works

1. The agent stores information in a JSON file for persistence
2. It learns new topics through `learn` commands
3. It recalls information when asked
4. All interactions are tracked for learning progression

## Future Enhancements

- [ ] Machine learning model integration
- [ ] Natural language processing
- [ ] Conversation context awareness
- [ ] Query expansion
- [ ] Feedback mechanism
