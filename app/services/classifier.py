from app.schemas import AnalyzeResponse, RequestCategory, RequestPriority


def classify_message(message: str) -> AnalyzeResponse:
    text = message.lower().strip()

    category = RequestCategory.support
    priority = RequestPriority.low
    needs_human = False
    confidence = 0.65

    if any(word in text for word in ["login", "password", "error", "500", "api", "integration", "bug"]):
        category = RequestCategory.technical
        priority = RequestPriority.medium
        confidence = 0.8

    if any(word in text for word in ["invoice", "payment", "billing", "refund", "charge"]):
        category = RequestCategory.billing
        priority = RequestPriority.medium
        confidence = 0.78

    if any(word in text for word in ["price", "demo", "trial", "buy", "sales"]):
        category = RequestCategory.sales
        priority = RequestPriority.low
        confidence = 0.75

    if any(word in text for word in ["urgent", "critical", "production", "down", "500 errors", "security"]):
        priority = RequestPriority.high
        needs_human = True
        confidence = 0.88

    if category == RequestCategory.technical and priority in {RequestPriority.medium, RequestPriority.high}:
        needs_human = True

    summary = build_summary(message)

    return AnalyzeResponse(
        category=category,
        priority=priority,
        summary=summary,
        needs_human=needs_human,
        confidence=confidence,
    )


def build_summary(message: str) -> str:
    clean_message = " ".join(message.split())

    if len(clean_message) <= 120:
        return clean_message

    return clean_message[:117] + "..."
