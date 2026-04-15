from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="The user message to send to the LLM"
    )


class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        description="The LLM generated response"
    )
    provider: str = Field(
        ...,
        description="Which LLM provider handled the request"
    )