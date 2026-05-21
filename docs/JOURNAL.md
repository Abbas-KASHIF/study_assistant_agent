# Project Journal

## Step 1 – 24.04

At the first stage, the planned system was a Python-based Study Assistant Agent. The goal was to create a simple AI-assisted system that receives a user request and uses tools to return a meaningful answer.

The planned AI/agent approach was a single intelligent agent. The agent would analyze the user input, choose the correct tool, call that tool, and present the final result.

Planned tools:

- calculator tool,
- file reader tool,
- keyword search tool,
- summarization tool.

Preliminary programming concepts:

- functions,
- classes,
- modules,
- conditionals,
- exception handling,
- file processing,
- testing,
- Git versioning.

## Step 2 – 08.05

The implementation was refined into a modular Python project. The main agent class became `StudyAssistantAgent`. The system now has separate modules for models, configuration, tools, and tests.

Programming concepts actually used:

- classes: `StudyAssistantAgent` and `AgentResponse`,
- dataclasses: structured agent output,
- modules and packages: separate project parts,
- exception handling: invalid input and unsupported files,
- file handling: reading local text files,
- regular expressions: detecting arithmetic tasks,
- abstract syntax tree parsing: safe calculator evaluation,
- unit tests: testing individual tools and the agent workflow.

Tools are integrated through the agent. The agent detects the intent and calls only the needed tool. For example, calculation requests call the calculator tool, file summary requests call the file reader and summarizer, and keyword requests call the file reader and search tool.

## Step 3 – 15.05

Testing was performed using `pytest`. The tests include functional testing, tool testing, input validation testing, and error handling testing.

Test scenarios:

1. Calculator receives `2 + 3 * 4` and returns `14`.
2. Calculator rejects unsafe expressions.
3. File text normalization removes unnecessary whitespace.
4. Keyword search finds matching snippets.
5. Summarizer returns the required number of sentences.
6. Agent calculation workflow uses the calculator tool.
7. Agent file summary workflow uses file reader and summarizer.
8. Agent file search workflow uses file reader and search tool.

Deployment preparation:

The system can be run as a local command-line application. The user creates a virtual environment, installs dependencies from `requirements.txt`, and runs `main.py`.

Data conversion:

User input is received as a string. File content is converted into normalized text. Calculator input is converted into an abstract syntax tree before evaluation. This keeps data consistent and avoids unsafe code execution.

## Final Submission – 22.05

The final system is a working Study Assistant Agent implemented in Python. It demonstrates agent-based logic, tool usage, input/output handling, testing, documentation, deployment preparation, and GitHub-ready project structure.

Final programming concepts:

- modular programming,
- object-oriented programming,
- dataclasses,
- safe expression parsing,
- file processing,
- input validation,
- exception handling,
- automated testing,
- version control.

Final tools and their role:

- calculator tool: solves arithmetic safely,
- file reader tool: reads external data files,
- search tool: retrieves keyword evidence from text,
- summarizer tool: transforms text into a short summary.

Testing conclusion:

All main components are covered by tests. The tests verify successful cases and error cases. This makes the project reliable and easier to maintain.

Deployment conclusion:

The system is suitable for local command-line deployment. For future improvement, it can be changed into a web service or API-based assistant.

Chosen deployment strategy:

A staged local deployment strategy is most suitable. First the developer runs tests, then installs the system in a clean environment, then checks sample workflows, and finally publishes the stable version on GitHub.
