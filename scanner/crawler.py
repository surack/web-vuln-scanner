# scanner/crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "web-vuln-scanner/1.0 (lab-only)"})

def get_forms(url, timeout=10):
    """
    Return a list of forms found on the given URL.
    Each form: {"action": full_url, "method": "get"/"post", "inputs": [{"name","type","value"}]}
    """
    try:
        r = SESSION.get(url, timeout=timeout)
        r.raise_for_status()
    except Exception:
        return []  # return empty if not reachable

    soup = BeautifulSoup(r.text, "lxml")
    forms = []
    for form in soup.find_all("form"):
        action = form.get("action") or url
        method = form.get("method", "get").lower()
        inputs = []
        for inp in form.find_all(["input", "textarea", "select"]):
            name = inp.get("name")
            if not name:
                continue
            itype = inp.get("type", "text")
            value = inp.get("value", "")
            inputs.append({"name": name, "type": itype, "value": value})
        forms.append({"action": urljoin(url, action), "method": method, "inputs": inputs})
    return forms
