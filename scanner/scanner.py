# scanner/scanner.py
import time
import json
from .crawler import get_forms, SESSION
from .payloads import XSS_PAYLOADS, SQLI_TESTS
from .detectors import detect_xss, detect_sqli

def scan_url(url, delay=0.5):
    """
    Scan the given URL (single page): discover forms, inject payloads, detect results.
    Returns a dict with findings.
    """
    findings = []
    forms = get_forms(url)
    for form in forms:
        form_action = form.get("action")
        method = form.get("method", "get")
        inputs = form.get("inputs", [])
        # For each input, test XSS and SQLi payloads
        for field in inputs:
            name = field["name"]
            for payload in XSS_PAYLOADS:
                data = {name: payload}
                try:
                    if method == "post":
                        r = SESSION.post(form_action, data=data, timeout=10)
                    else:
                        r = SESSION.get(form_action, params=data, timeout=10)
                except Exception:
                    continue
                if detect_xss(r.text, payload):
                    findings.append({
                        "type": "xss",
                        "url": form_action,
                        "param": name,
                        "payload": payload,
                        "evidence": payload
                    })
                time.sleep(delay)
            for payload in SQLI_TESTS:
                data = {name: payload}
                try:
                    if method == "post":
                        r = SESSION.post(form_action, data=data, timeout=10)
                    else:
                        r = SESSION.get(form_action, params=data, timeout=10)
                except Exception:
                    continue
                found, evidence = detect_sqli(r.text)
                if found:
                    findings.append({
                        "type": "sqli",
                        "url": form_action,
                        "param": name,
                        "payload": payload,
                        "evidence": evidence
                    })
                time.sleep(delay)
    result = {
        "target": url,
        "timestamp": time.time(),
        "form_count": len(forms),
        "findings": findings
    }
    # write a last_scan.json for convenience if running locally or in Actions
    try:
        with open("last_scan.json", "w") as fh:
            json.dump(result, fh, indent=2)
    except Exception:
        pass
    return result
