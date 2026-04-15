from src.llm.base import BaseLLMClient
from src.models.schemas import ChatRequest, ChatResponse
from src.utils.logging import get_logger

logger = get_logger(__name__)


class ChatService:
    def __init__(self, llm_client: BaseLLMClient):
        self.llm_client = llm_client

    def process(self, request: ChatRequest) -> ChatResponse:
        logger.info(f"Processing request: message_length={len(request.message)}")

        raw_response = self.llm_client.generate(request.message)

        logger.info(f"Response generated provider={self.llm_client.__class__.__name__}")
        
        return ChatResponse(
            response=raw_response,
            provider=self.llm_client.__class__.__name__
        )