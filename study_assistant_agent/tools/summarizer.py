from typing import List


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Produce a simple extractive summary by selecting the first meaningful sentences.

    This is intentionally deterministic so tests and deployment remain stable.
    """
    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    sentences = _split_sentences(text)
    selected = sentences[:max_sentences]
    return " ".join(selected)


def _split_sentences(text: str) -> List[str]:
    marks = ".!?"
    sentences: List[str] = []
    current = []

    for char in text.strip():
        current.append(char)
        if char in marks:
            sentence = "".join(current).strip()
            if sentence:
                sentences.append(sentence)
            current = []

    tail = "".join(current).strip()
    if tail:
        sentences.append(tail)

    return sentences
