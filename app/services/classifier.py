from app.llm.providers import get_llm_provider
from app.schemas import AnalyzeResponse


def classify_message(message: str) -> AnalyzeResponse:
    provider = get_llm_provider()
    return provider.analyze_message(message)
