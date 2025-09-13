# scanner/detectors.py
import re

SQL_ERRORS = [
    r"you have an error in your sql syntax",
    r"mysql_fetch",
    r"sql syntax.*mysql",
    r"unclosed quotation mark after the character string",
    r"ORA-\d{5}"
]

def detect_xss(response_text, payload):
    """Return True if the payload appears directly in response body."""
    if not response_text:
        return False
    return payload in response_text

def detect_sqli(response_text):
    """Return (True, evidence) if common SQL error phrases are found."""
    if not response_text:
        return False, None
    lower = response_text.lower()
    for pat in SQL_ERRORS:
        if re.search(pat, lower):
            return True, pat
    return False, None
