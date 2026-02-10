"""
Main agent logic for grief counseling assistant.
"""

from pydantic import BaseModel

from grief_counseling.config import Config
from grief_counseling.utils.client import call_llm
from grief_counseling.utils.prompter import Prompter


class Agent:
    """
    Main Counselor Agent
    """

    def __init__(self):
        self.prompter = Prompter()

    def respond(self, user_message: str, recent_history: list[dict]) -> str | BaseModel:
        """
        Generates response based on user message, recent conversation history
        and system prompt.
        """
        system_prompt = self.prompter.build_system_prompt(
            core={
                "agent_name": Config.AGENT_NAME,
            }
        )

        # 4. Przygotuj strukturę wiadomości dla API
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(recent_history)
        messages.append({"role": "user", "content": user_message})

        # 5. === STRUCTURED OUTPUT ===
        # Wywołujemy LLM i oczekujemy konkretnego modelu danych
        response = call_llm(messages)

        return response
