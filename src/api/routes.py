from fastapi import APIRouter, Depends
from src.models.schemas import ChatRequest, ChatResponse
from src.services.chat_service import ChatService
from src.llm.base import BaseLLMClient
from src.llm.mock_client import MockLLMClient
from src.core.config import settings

router = APIRouter()


def get_llm_client() -> BaseLLMClient:
    if settings.llm_provider == "azure":
        from src.llm.azure_client import AzureOpenAIClient
        return AzureOpenAIClient()
    return MockLLMClient()


def get_chat_service(
    llm_client: BaseLLMClient = Depends(get_llm_client)
) -> ChatService:
    return ChatService(llm_client=llm_client)


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service)
):
    return service.process(request)