from fastapi import FastAPI
from src.core.config import settings
from src.llm.mock_client import MockLLMClient

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

llm_client = MockLLMClient()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment
    }


@app.post("/chat")
def chat(prompt: str):
    response = llm_client.generate(prompt)
    return {"response": response}