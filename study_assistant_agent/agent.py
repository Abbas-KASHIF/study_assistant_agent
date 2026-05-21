import re
from pathlib import Path
from typing import Optional

from study_assistant_agent.models import AgentResponse
from study_assistant_agent.tools.calculator import safe_calculate
from study_assistant_agent.tools.file_reader import normalize_text, read_text_file
from study_assistant_agent.tools.search_tool import count_keyword, keyword_search
from study_assistant_agent.tools.summarizer import summarize_text


class StudyAssistantAgent:
    """
    A simple intelligent assistant that routes user requests to tools.

    The agent can:
    - calculate arithmetic expressions,
    - read and summarize files,
    - search keywords inside files,
    - answer general study/system implementation questions using built-in knowledge.
    """

    def handle(self, query: str, file_path: Optional[str] = None) -> AgentResponse:
        if not query or not query.strip():
            raise ValueError("User query cannot be empty.")

        query_clean = query.strip()
        query_lower = query_clean.lower()

        if self._looks_like_calculation(query_lower):
            expression = self._extract_expression(query_clean)
            result = safe_calculate(expression)
            return AgentResponse(
                user_query=query_clean,
                intent="calculation",
                answer=f"The calculated result is {result}.",
                tools_used=["calculator"],
                evidence={"expression": expression, "result": result},
            )

        if file_path:
            text = normalize_text(read_text_file(file_path))

            keyword = self._extract_keyword(query_clean)
            if "search" in query_lower or "find" in query_lower:
                snippets = keyword_search(text, keyword)
                count = count_keyword(text, keyword)
                answer = (
                    f"I found the keyword '{keyword}' {count} time(s). "
                    f"Relevant snippets: " + (" | ".join(snippets) if snippets else "No snippets found.")
                )
                return AgentResponse(
                    user_query=query_clean,
                    intent="file_search",
                    answer=answer,
                    tools_used=["file_reader", "search_tool"],
                    evidence={"keyword": keyword, "matches": count, "snippets": snippets},
                )

            summary = summarize_text(text)
            return AgentResponse(
                user_query=query_clean,
                intent="file_summary",
                answer=f"File summary: {summary}",
                tools_used=["file_reader", "summarizer"],
                evidence={"file": str(Path(file_path)), "summary": summary},
            )

        return self._knowledge_answer(query_clean)

    def _knowledge_answer(self, query: str) -> AgentResponse:
        q = query.lower()

        if "deployment" in q:
            answer = (
                "A suitable deployment strategy for this project is staged local deployment. "
                "First run automated tests, then install dependencies in a virtual environment, "
                "then run the command-line application with sample data. For larger use, the same "
                "logic could be released as an API service using rolling or canary deployment."
            )
            intent = "deployment_explanation"
        elif "test" in q:
            answer = (
                "Testing should include unit tests for each tool, integration tests for the agent workflow, "
                "input validation tests, and error handling tests. Expected and actual results should be compared."
            )
            intent = "testing_explanation"
        elif "version" in q or "git" in q:
            answer = (
                "Versioning should use Git with regular meaningful commits, for example initial structure, "
                "tool implementation, agent workflow, tests, documentation, and final deployment preparation."
            )
            intent = "versioning_explanation"
        else:
            answer = (
                "I can help with calculations, text-file summaries, keyword search in files, testing notes, "
                "deployment explanations, and Git/versioning guidance."
            )
            intent = "general_help"

        return AgentResponse(
            user_query=query,
            intent=intent,
            answer=answer,
            tools_used=["knowledge_router"],
            evidence={},
        )

    def _looks_like_calculation(self, query: str) -> bool:
        return "calculate" in query or bool(re.fullmatch(r"[0-9+\-*/(). %^]+", query.strip()))

    def _extract_expression(self, query: str) -> str:
        expression = query.lower().replace("calculate", "").replace("^", "**").strip()
        if not expression:
            raise ValueError("No expression found to calculate.")
        return expression

    def _extract_keyword(self, query: str) -> str:
        # Examples: "search testing", "find deployment"
        words = query.replace(":", " ").split()
        stop_words = {"search", "find", "keyword", "in", "the", "file", "for"}
        useful = [w for w in words if w.lower() not in stop_words]
        return useful[-1] if useful else words[-1]
