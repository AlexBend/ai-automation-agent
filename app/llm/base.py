from typing import Protocol

from app.schemas import AnalyzeResponse


class LLMProvider(Protocol):
    def analyze_message(self, message: str) -> AnalyzeResponse:
        """
        Analyze incoming message and return structured classification result.
        """
        ...
