import os
from pathlib import Path


DB_TIMEOUT = 10 

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "french_learner.db"
TRANSCRIPT_EN = BASE_DIR / "data" / "english_transcript.txt"
TRANSCRIPT_FR = BASE_DIR / "data" / "french_transcript.txt"
TRANSCRIPT_YOUTUBE = BASE_DIR / "data" / "youtube_transcript.txt"

# LLM Configuration
LLM_MODELS = {
    "translator": "granite3.3:2b",
    "evaluator":   "granite3.3:2b",
    "word_helper":   "granite3.3:2b", 
    "youtube_transcript_generator": "qwen2.5:3b", 
    "french_word_meaning": "granite3.1-dense:2b",
    "french_accent_correction" : "qwen2.5:3b"# phi3.5:3.8b  cogito:3b  granite3.1-dense:2b    granite3.3:2b qwen3:1.7b               
}


# UI Configuration
COLOR_SCHEME = {
    "primary": "#4B8BBE",
    "secondary": "#ED2939",
    "background": "#F8F9FA",
    "text": "#333333"
}