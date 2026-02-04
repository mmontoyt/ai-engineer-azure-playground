from abc import ABC, abstractmethod


class BaseLLMClient(ABC):  # Abstract base class for LLM clients
    """
    Abstract base class for LLM clients.
    Defines the contract that any LLM provider must follow.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM given a prompt.
        """
        pass