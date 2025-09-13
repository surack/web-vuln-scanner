# tests/test_crawler.py
from scanner.crawler import get_forms

def test_get_forms_returns_list():
    # example.com is safe and reachable; this is a smoke test
    forms = get_forms("https://example.com")
    assert isinstance(forms, list)
