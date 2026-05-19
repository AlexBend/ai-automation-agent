from enum import Enum
from pydantic import BaseModel, Field


class RequestCategory(str, Enum):
    support = "support"
    sales = "sales"
    technical = "technical"
    billing = "billing"
    unknown = "unknown"


class RequestPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class AnalyzeRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=3,
        max_length=5000,
        description="Incoming user message that should be analyzed.",
    )
    user_id: str | None = Field(
        default=None,
        description="Optional external user identifier.",
    )


class AnalyzeResponse(BaseModel):
    category: RequestCategory
    priority: RequestPriority
    summary: str
    needs_human: bool
    confidence: float = Field(ge=0, le=1)
