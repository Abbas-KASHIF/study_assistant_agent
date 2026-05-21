# Final Report: System Implementation, Testing, and Deployment

## 1. System description and goal

The project is called **Study Assistant Agent**. It is a Python-based AI-assisted command-line system. The goal of the system is to help a user with simple study and information-processing tasks by using external tools during execution.

The system receives a user request, analyzes the request, selects a suitable tool, processes the task, and returns a meaningful answer. This satisfies the requirement that the system must receive input, process the request, use at least one tool, and return a useful result.

## 2. AI or agent-based approach

The system uses a single-agent workflow. The central class is `StudyAssistantAgent`. It works as a controller and decision-maker. The agent does not solve every task directly. Instead, it routes the request to specialized tools.

Example workflow:

1. User enters a query.
2. Agent validates the input.
3. Agent detects the intent.
4. Agent calls the required tool.
5. Tool returns processed data.
6. Agent prepares the final response.

This is an agent-based solution because the software selects actions based on the user request and uses tools to complete the task.

## 3. Programming concepts and usage

### Modular programming

The project is divided into separate files and folders. Each module has a clear responsibility. This makes the system easier to understand and maintain.

### Object-oriented programming

The main logic is implemented in the `StudyAssistantAgent` class. The response structure is represented by the `AgentResponse` dataclass.

### Dataclasses

`AgentResponse` stores the user query, detected intent, answer, tools used, and evidence. This makes the output structured and clear.

### File processing

The file reader tool reads external text-based files. This allows the agent to use external data during execution.

### Exception handling

The program raises clear errors for empty input, unsupported file formats, missing files, unsafe calculator expressions, and empty summary text.

### Safe expression parsing

The calculator uses Python's `ast` module instead of unsafe `eval()`. Only safe arithmetic operations are allowed.

### Testing

The project uses `pytest` to test the calculator, file tools, search, summarizer, and complete agent workflow.

### Version control

The project is prepared for Git and GitHub with a clear structure, `.gitignore`, README, tests, and documentation.

## 4. Tools and their role

| Tool | Role |
|---|---|
| Calculator | Calculates arithmetic expressions safely |
| File reader | Reads external files used as input data |
| Search tool | Searches keywords and returns relevant snippets |
| Summarizer | Converts longer text into a short summary |
| Knowledge router | Provides short built-in explanations for testing, deployment, and versioning |

## 5. Input and output handling

Input is received through command-line arguments. The user provides a query and optionally a file path. The output is printed in a structured way:

- detected intent,
- tools used,
- final answer.

Examples:

```bash
python main.py "calculate 10 + 5"
python main.py "summarize this file" --file data/sample_notes.txt
python main.py "search deployment" --file data/sample_notes.txt
```

## 6. Data porting and conversion

The system uses different kinds of data conversion:

1. Command-line input is converted into a clean query string.
2. File data is read as UTF-8 text.
3. File text is normalized by removing unnecessary whitespace.
4. Search input is converted into a keyword.
5. Calculator input is converted into a safe abstract syntax tree.
6. Tool outputs are converted into a structured `AgentResponse`.

Correctness is preserved because each transformation is simple, deterministic, and tested.

## 7. Testing process

Testing was performed with `pytest`. Testing was done together with implementation, not only at the end.

### Test scenarios and expected results

| Test scenario | Expected result |
|---|---|
| Calculator handles `2 + 3 * 4` | Returns `14` |
| Calculator handles parentheses | Returns correct arithmetic result |
| Calculator receives unsafe expression | Raises `ValueError` |
| Text normalization receives multiline text | Returns one clean line |
| Search tool searches keyword | Returns snippets and correct count |
| Summarizer receives four sentences | Returns selected number of sentences |
| Agent receives calculation query | Uses calculator and returns result |
| Agent receives file summary query | Uses file reader and summarizer |
| Agent receives file search query | Uses file reader and search tool |

### Testing conclusion

The tests show that the main workflow and individual tools work correctly. The project includes both successful test cases and error-handling test cases.

## 8. Deployment preparation

The project is prepared for local deployment as a command-line tool.

Deployment steps:

```bash
git clone <repository-url>
cd study_assistant_agent
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest tests -v
python main.py "calculate 10 + 5"
```

For macOS/Linux activation:

```bash
source .venv/bin/activate
```

The repository includes:

- source code,
- tests,
- documentation,
- dependency list,
- `.env.example`,
- GitHub Actions workflow.

## 9. Proposed deployment strategy

The best deployment strategy is **staged local deployment**.

This means the software is not directly released without checking. First it is tested, then installed in a clean environment, then executed with sample data, and only after that it is published as a stable version.

For a larger future version, the same system could be deployed as an API-based assistant. In that case, a rolling deployment or canary deployment would be safer because only a small part of users would receive the new version first.

## 10. Final conclusion

The Study Assistant Agent meets the practical task requirements. It is a Python system with agent-based logic, tool usage, input and output handling, testing, deployment preparation, documentation, and GitHub-ready structure. The project is small but complete, understandable, and maintainable.
