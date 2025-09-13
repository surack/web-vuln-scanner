# scanner/payloads.py

XSS_PAYLOADS = [
    "\"'><script>/*x*/</script>",     # simple marker
    "<svg/onload=console.log('x')>",  # non-alert payload
]

SQLI_TESTS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "'; -- ",
]
