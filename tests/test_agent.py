from pathlib import Path
from study_assistant_agent.agent import StudyAssistantAgent


def test_agent_calculation():
    agent = StudyAssistantAgent()
    response = agent.handle("calculate 10 + 5")
    assert response.intent == "calculation"
    assert "calculator" in response.tools_used
    assert "15" in response.answer


def test_agent_file_summary(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Deployment prepares software for use. Testing detects defects.", encoding="utf-8")
    agent = StudyAssistantAgent()
    response = agent.handle("summarize this file", str(file_path))
    assert response.intent == "file_summary"
    assert "file_reader" in response.tools_used


def test_agent_file_search(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Git supports versioning. Git records project changes.", encoding="utf-8")
    agent = StudyAssistantAgent()
    response = agent.handle("search Git", str(file_path))
    assert response.intent == "file_search"
    assert response.evidence["matches"] == 2
