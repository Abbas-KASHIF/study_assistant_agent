# Study Assistant Agent

## Project goal

Study Assistant Agent is a Python-based AI/agent-style command-line assistant. It receives a user request, decides what kind of task is required, calls one or more tools, and returns a structured answer.

The project was created for the practical task **System Implementation, Testing, and Deployment for an AI- and Agent-Based Python System**.

## Main functions

The assistant can:

- calculate arithmetic expressions using a safe calculator tool,
- read text, markdown, CSV, and JSON files,
- summarize local text files,
- search keywords inside local files,
- explain testing, deployment, and versioning concepts.

## Agent-based approach

The system contains a single intelligent agent named `StudyAssistantAgent`. The agent uses rule-based intent detection to choose the correct tool. This keeps the project simple, testable, and deterministic.

## Tools used by the agent

| Tool | File | Purpose |
|---|---|---|
| Calculator | `study_assistant_agent/tools/calculator.py` | Safely solves arithmetic expressions |
| File reader | `study_assistant_agent/tools/file_reader.py` | Reads supported local files |
| Search tool | `study_assistant_agent/tools/search_tool.py` | Searches keywords and counts matches |
| Summarizer | `study_assistant_agent/tools/summarizer.py` | Creates short extractive summaries |

## Project structure

```text
study_assistant_agent/
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   └── sample_notes.txt
├── docs/
│   ├── FINAL_REPORT.md
│   └── JOURNAL.md
├── study_assistant_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── models.py
│   └── tools/
│       ├── calculator.py
│       ├── file_reader.py
│       ├── search_tool.py
│       └── summarizer.py
└── tests/
    ├── test_agent.py
    ├── test_calculator.py
    └── test_file_tools.py
```

## Installation

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to run

Calculation:

```bash
python main.py "calculate 10 + 5 * 2"
```

Summarize a file:

```bash
python main.py "summarize this file" --file data/sample_notes.txt
```

Search inside a file:

```bash
python main.py "search deployment" --file data/sample_notes.txt
```

Ask about deployment:

```bash
python main.py "explain deployment"
```

## Testing

Run all tests:

```bash
python -m pytest tests -v
```

The tests check calculator behavior, file processing, search, summarization, input validation, and the full agent workflow.

## Configuration

The system can run without environment variables. Optional variables are shown in `.env.example`:

- `APP_NAME`: application name,
- `MAX_PREVIEW_CHARS`: optional preview size setting.

## Data conversion

Input data is received as command-line text and optional local file content. File content is read as UTF-8 text, normalized by removing unnecessary whitespace, then passed to the summarizer or search tool. The calculator tool converts a user arithmetic string into a safe Python abstract syntax tree before calculating it. This preserves correctness and avoids unsafe `eval()` execution.

## Deployment preparation

This project is prepared as a local command-line application. Another user can clone the GitHub repository, create a virtual environment, install dependencies, and run the application using the commands above.

## Proposed deployment strategy

The suitable strategy is staged local deployment:

1. run automated tests,
2. install in a clean virtual environment,
3. test using sample data,
4. release to GitHub,
5. for a larger version, convert the same agent logic into an API and use rolling or canary deployment.

## Versioning

Git should be used with meaningful commits, for example:

```bash
git add .
git commit -m "Initial project structure"
git commit -m "Add calculator and file tools"
git commit -m "Implement agent workflow"
git commit -m "Add tests and documentation"
git commit -m "Prepare final deployment documentation"
```
