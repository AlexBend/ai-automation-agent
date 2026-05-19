from app.config import settings
from app.llm.base import LLMProvider
from app.schemas import AnalyzeResponse
from app.services.rules import rule_based_classify


class MockLLMProvider:
    """
    Mock provider for local development and tests.

    It does not call any external LLM API.
    This keeps tests stable, fast and free.
    """

    def analyze_message(self, message: str) -> AnalyzeResponse:
        return rule_based_classify(message)


def get_llm_provider() -> LLMProvider:
    provider_name = settings.llm_provider.lower().strip()

    if provider_name == "mock":
        return MockLLMProvider()

    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
