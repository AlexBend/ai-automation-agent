from fastapi import FastAPI
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.classifier import classify_message


app = FastAPI(
    title="AI Automation Agent",
    description="FastAPI service for AI-powered request classification and automation.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_request(payload: AnalyzeRequest) -> AnalyzeResponse:
    return classify_message(payload.message)
