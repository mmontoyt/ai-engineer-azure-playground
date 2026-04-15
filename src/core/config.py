from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Engineer API"
    environment: str = "local"
    log_level: str = "info"

    # LLM config — vacío por ahora, Azure llegará después
    llm_provider: str = "mock"  # "mock" | "azure"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()