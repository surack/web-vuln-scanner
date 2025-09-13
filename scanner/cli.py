# scanner/cli.py
import argparse
import os
import json
from scanner.scanner import scan_url

def main():
    parser = argparse.ArgumentParser(description="Run web vuln scanner (lab-only)")
    parser.add_argument("--target", required=True, help="Target URL to scan (lab-only)")
    args = parser.parse_args()

    out = scan_url(args.target)
    os.makedirs("scans", exist_ok=True)
    safe_name = args.target.replace("://", "_").replace("/", "_")
    fname = os.path.join("scans", f"{safe_name}.json")
    with open(fname, "w") as f:
        json.dump(out, f, indent=2)
    print(f"[+] Scan complete. Results written to {fname}")

if __name__ == "__main__":
    main()
