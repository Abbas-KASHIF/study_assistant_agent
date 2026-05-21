import pytest
from study_assistant_agent.tools.file_reader import normalize_text
from study_assistant_agent.tools.search_tool import count_keyword, keyword_search
from study_assistant_agent.tools.summarizer import summarize_text


def test_normalize_text():
    assert normalize_text("Hello\n   world") == "Hello world"


def test_keyword_search_and_count():
    text = "Testing is important. Unit testing checks small parts. Integration testing checks combined parts."
    assert count_keyword(text, "testing") == 3
    results = keyword_search(text, "testing")
    assert len(results) >= 1


def test_summarize_text():
    text = "First sentence. Second sentence. Third sentence. Fourth sentence."
    assert summarize_text(text, max_sentences=2) == "First sentence. Second sentence."


def test_empty_summary_error():
    with pytest.raises(ValueError):
        summarize_text("")
