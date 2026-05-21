from pathlib import Path


def read_text_file(path: str) -> str:
    """Read a UTF-8 text/markdown/csv file and return its content."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if file_path.suffix.lower() not in {".txt", ".md", ".csv", ".json"}:
        raise ValueError("Only .txt, .md, .csv, and .json files are supported.")

    return file_path.read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Clean text by normalizing whitespace."""
    return " ".join(text.replace("\n", " ").split())
