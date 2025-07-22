import os
from pathlib import Path


DB_TIMEOUT = 10 

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "french_learner.db"
TRANSCRIPT_EN = BASE_DIR / "data" / "english_transcript.txt"
TRANSCRIPT_FR = BASE_DIR / "data" / "french_transcript.txt"

# LLM Configuration
LLM_MODELS = {
    "translator": "gemma3:1b",
    "evaluator": "granite3.1-dense:2b",
    "word_helper": "qwen2.5:3b",
    "french_word_meaning": "granite3.1-dense:2b"
}


# UI Configuration
COLOR_SCHEME = {
    "primary": "#4B8BBE",
    "secondary": "#ED2939",
    "background": "#F8F9FA",
    "text": "#333333"
}