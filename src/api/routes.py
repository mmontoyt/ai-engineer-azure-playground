from fastapi import APIRouter, Depends
from src.models.schemas import ChatRequest, ChatResponse
from src.services.chat_service import ChatService
from src.llm.base import BaseLLMClient
from src.llm.mock_client import MockLLMClient

router = APIRouter()


def get_llm_client() -> BaseLLMClient:
    """
    Dependency: returns the active LLM client.
    In the future, this will read from settings to decide
    which client to instantiate (mock vs azure).
    """
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