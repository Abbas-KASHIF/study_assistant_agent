import pytest
from study_assistant_agent.tools.calculator import safe_calculate


def test_addition_and_multiplication():
    assert safe_calculate("2 + 3 * 4") == 14


def test_parentheses():
    assert safe_calculate("(2 + 3) * 4") == 20


def test_rejects_unsafe_expression():
    with pytest.raises(ValueError):
        safe_calculate("__import__('os').system('echo unsafe')")
