from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATA_DIR = BASE_DIR / "data"

APP_NAME = os.getenv("APP_NAME", "Study Assistant Agent")
MAX_PREVIEW_CHARS = int(os.getenv("MAX_PREVIEW_CHARS", "1200"))
