# 🔍 Web Vulnerability Scanner (Educational Project)

This is a **simple Python-based web vulnerability scanner** built for a **cybersecurity internship project**.  
It demonstrates how to crawl web forms, inject test payloads, and detect common issues like **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)**.

⚠️ **Important:** This tool is for **educational use only**. Do **NOT** run it on websites you do not own or do not have **written permission** to test. See [SAFE_USAGE.md](SAFE_USAGE.md).

---

## ✨ Features
- Crawls HTML forms on target pages.
- Injects safe test payloads for:
  - XSS (payload reflection detection)
  - SQLi (error-based detection)
- Generates a JSON report with findings.
- Can be run automatically in **GitHub Actions** (no local setup needed).
- Optional simple **Flask web UI** to run scans interactively.

---

## 📂 Project Structure
