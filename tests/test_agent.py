"""
Unit tests for Agent class.
"""

from unittest.mock import Mock, patch

import pytest

from grief_counseling.agent import Agent
from grief_counseling.config import Config


class TestAgent:
    """Test suite for Agent class."""

    @pytest.fixture
    def agent(self):
        """Create an Agent instance with mocked Prompter."""
        with patch("grief_counseling.agent.Prompter") as mock_prompter_class:
            mock_prompter_instance = Mock()
            mock_prompter_class.return_value = mock_prompter_instance
            agent = Agent()
            agent.prompter = mock_prompter_instance
            yield agent

    def test_agent_initialization(self):
        """Test Agent initializes with a Prompter."""
        with patch("grief_counseling.agent.Prompter"):
            agent = Agent()
            assert agent.prompter is not None

    def test_respond_builds_system_prompt(self, agent):
        """Test that respond() builds system prompt with correct config."""
        # Arrange
        agent.prompter.build_system_prompt.return_value = "System prompt text"
        user_message = "Hello"
        recent_history = []

        with patch("grief_counseling.agent.call_llm") as mock_call_llm:
            mock_call_llm.return_value = "Response"

            # Act
            agent.respond(user_message, recent_history)

            # Assert
            agent.prompter.build_system_prompt.assert_called_once()
            call_args = agent.prompter.build_system_prompt.call_args
            assert len(call_args[1]["core"]) == 1
            assert call_args[1]["core"]["agent_name"] == Config.AGENT_NAME

    def test_respond_message_structure(self, agent):
        """Test that messages are structured correctly before calling LLM."""
        # Arrange
        system_prompt = "You are a counselor."
        agent.prompter.build_system_prompt.return_value = system_prompt
        user_message = "I'm struggling"
        recent_history = [
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello"},
        ]

        with patch("grief_counseling.agent.call_llm") as mock_call_llm:
            mock_call_llm.return_value = "I understand"

            # Act
            agent.respond(user_message, recent_history)

            # Assert - verify message structure
            call_args = mock_call_llm.call_args[0][0]
            assert len(call_args) == 4  # system + 2 history + 1 user
            assert call_args[0]["role"] == "system"
            assert call_args[0]["content"] == system_prompt
            assert call_args[1]["role"] == "user"
            assert call_args[1]["content"] == "Hi"
            assert call_args[2]["role"] == "assistant"
            assert call_args[2]["content"] == "Hello"
            assert call_args[3]["role"] == "user"
            assert call_args[3]["content"] == user_message

    def test_respond_empty_history(self, agent):
        """Test respond() with empty conversation history."""
        # Arrange
        agent.prompter.build_system_prompt.return_value = "System"
        user_message = "First message"
        recent_history = []

        with patch("grief_counseling.agent.call_llm") as mock_call_llm:
            mock_call_llm.return_value = "Response to first message"

            # Act
            response = agent.respond(user_message, recent_history)

            # Assert
            assert response == "Response to first message"
            call_args = mock_call_llm.call_args[0][0]
            assert len(call_args) == 2  # system + user only

    def test_respond_multiple_history_entries(self, agent):
        """Test respond() with multi-turn conversation history."""
        # Arrange
        agent.prompter.build_system_prompt.return_value = "System"
        user_message = "What now?"
        recent_history = [
            {"role": "user", "content": "Q1"},
            {"role": "assistant", "content": "A1"},
            {"role": "user", "content": "Q2"},
            {"role": "assistant", "content": "A2"},
        ]

        with patch("grief_counseling.agent.call_llm") as mock_call_llm:
            mock_call_llm.return_value = "Final answer"

            # Act
            agent.respond(user_message, recent_history)

            # Assert
            call_args = mock_call_llm.call_args[0][0]
            assert len(call_args) == 6  # system + 4 history + user
            assert call_args[5]["content"] == user_message

    def test_respond_calls_llm_with_correct_messages(self, agent):
        """Test that respond() calls call_llm with exactly the right messages."""
        # Arrange
        agent.prompter.build_system_prompt.return_value = "Some system prompt!"
        user_message = "Tell me a joke"
        recent_history = [{"role": "user", "content": "Hi"}]

        with patch("grief_counseling.agent.call_llm") as mock_call_llm:
            mock_call_llm.return_value = "Knock knock!"

            # Act
            response = agent.respond(user_message, recent_history)

            # Assert
            mock_call_llm.assert_called_once()
            messages = mock_call_llm.call_args[0][0]
            assert messages[0] == {"role": "system", "content": "Some system prompt!"}
            assert messages[-1] == {"role": "user", "content": user_message}
            assert response == "Knock knock!"
