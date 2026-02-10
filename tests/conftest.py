import os


def pytest_configure():
    os.environ["LLM_API_KEY"] = "llm_api_key_value"
    os.environ["LLM_MODEL_NAME"] = "llm_model_name_value"
    os.environ["LLM_BASE_URL"] = "llm_base_url_value"
