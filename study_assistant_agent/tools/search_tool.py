from typing import List, Tuple


def keyword_search(text: str, keyword: str, context_words: int = 8) -> List[str]:
    """
    Search a keyword inside text and return short context snippets.
    """
    if not keyword or not keyword.strip():
        raise ValueError("Keyword cannot be empty.")

    words = text.split()
    keyword_lower = keyword.lower()
    results: List[str] = []

    for index, word in enumerate(words):
        clean_word = word.strip(".,!?;:()[]{}").lower()
        if keyword_lower in clean_word:
            start = max(0, index - context_words)
            end = min(len(words), index + context_words + 1)
            snippet = " ".join(words[start:end])
            results.append(snippet)

    return results[:5]


def count_keyword(text: str, keyword: str) -> int:
    """Count simple keyword occurrences in a text."""
    return text.lower().count(keyword.lower())
