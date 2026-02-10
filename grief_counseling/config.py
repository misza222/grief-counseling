"""
Configuration for grief_counseling.

This file has basic settings and constants used across the application. You can expand it with more parameters as needed.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Main configuration class for grief_counseling.
    """

    # App settings
    AGENT_NAME = "Steve"

    # LLM
    LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gpt-4")
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL")

    TEMPERATURE = 0.0
    MAX_TOKENS = 10_000

    if not LLM_API_KEY or not LLM_BASE_URL or not LLM_MODEL_NAME:
        raise ValueError(
            "one of the LLM_* env variables not found! "
            "Please set it in your environment variables or .env file."
        )

    # Folders
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
