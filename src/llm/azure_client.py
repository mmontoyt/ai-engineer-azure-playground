from src.llm.base import BaseLLMClient
from src.core.config import settings
from src.utils.logging import get_logger

logger = get_logger(__name__)

class AzureOpenAIClient(BaseLLMClient):
    """
    Azure OpenAI implementation.
    Reads credentials from settings (environment variables)
    """
    def __init__(self):
        self.endpoint = settings.azure_openai_endpoint
        self.api_key = settings.azure_openai_api_key
        self.deployment = settings.azure_openai_deployment
        self._validate_config()

    def _validate_config(self):
        """
        Fails fast if Azure credentials are missing.
        Better to fail at startup than mid-request
        """
        missing = []
        if not self.endpoint: 
            missing.append("AZURE_OPENAI_ENDPOINT")
        if not self.api_key:
            missing.append("AZURE_OPENAI_API_KEY")
        if not self.deployment:
            missing.append("AZURE_OPENAI_DEPLOYMENT")
        
        if missing:
            raise ValueError(
                f"Missing Azure OpenAI config: {', '.join(missing)}"
            )
        
        logger.info(f"MissingOpenAClient initialized: deployment={self.deployment}")

                
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Azure OpenAI call not implemented yet.")