from app.llm.providers import MockLLMProvider, get_llm_provider
from app.schemas import RequestCategory, RequestPriority


def test_get_default_llm_provider():
    provider = get_llm_provider()

    assert isinstance(provider, MockLLMProvider)


def test_mock_llm_provider_analyzes_message():
    provider = MockLLMProvider()

    result = provider.analyze_message("Our production API is down with 500 errors")

    assert result.category == RequestCategory.technical
    assert result.priority == RequestPriority.high
    assert result.needs_human is True
    assert result.confidence >= 0.8
