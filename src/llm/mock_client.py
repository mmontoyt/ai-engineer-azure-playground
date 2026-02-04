from src.llm.base import BaseLLMClient


class MockLLMClient(BaseLLMClient):
    """
    Mock implementation of an LLM client.
    Used for local development and testing.
    """

    def generate(self, prompt: str) -> str:
        return f"[MOCK RESPONSE] You said: {prompt}"