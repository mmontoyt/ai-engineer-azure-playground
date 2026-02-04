from src.llm.base import BaseLLMClient


class AzureOpenAIClient(BaseLLMClient):
    """
    Azure OpenAI implementation.
    (To be implemented in next steps)
    """

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Azure OpenAI client not implemented yet.")