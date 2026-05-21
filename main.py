import argparse
from study_assistant_agent.agent import StudyAssistantAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Study Assistant Agent")
    parser.add_argument("query", help="Question or command for the agent")
    parser.add_argument("--file", dest="file_path", help="Optional text/markdown/csv/json file path")
    args = parser.parse_args()

    agent = StudyAssistantAgent()
    response = agent.handle(args.query, args.file_path)

    print("\n=== Study Assistant Agent ===")
    print(f"Intent: {response.intent}")
    print(f"Tools used: {', '.join(response.tools_used)}")
    print(f"Answer: {response.answer}")


if __name__ == "__main__":
    main()
