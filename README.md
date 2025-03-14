# OpenAI Agents SDK

This repository contains a boilerplate for working with OpenAI's Agents SDK, allowing you to build and run AI agents.

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (Python package installer/manager)

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd openai-agents-sdk
```

### 2. Install uv (if not already installed)

```bash
# On Windows with pip
pip install uv

# On macOS with Homebrew
brew install uv

# On Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Create a virtual environment with uv

```bash
uv venv
```

### 4. Activate the virtual environment

```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 5. Install dependencies

```bash
uv install
```

### 6. Configure environment variables

Replace the `.env` file with the .env file and place your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Running the Example

```bash
# Run the hello world example
uv run hello_world.py
```

## Example Output

The `hello_world.py` file demonstrates a simple agent that generates a haiku about recursion in programming. The output will look something like:

```
Code within the code,
Functions calling themselves,
Infinite loop's dance.
```

## Creating Your Own Agents

You can create your own agent scripts following the pattern in `hello_world.py`. Remember to run them using `uv run` command:

```bash
uv run your_agent_script.py
```

## Project Requirements

This project requires Python 3.13 or higher and uses the following dependencies:

- openai-agents (version 0.0.4 or higher)
- python-dotenv (version 1.0.1 or higher)
