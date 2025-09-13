# webui/app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from scanner.scanner import scan_url
import json, os

app = Flask(__name__)
app.secret_key = "change-me-in-production"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target")
        if not target:
            flash("Enter a target URL (lab-only).")
            return redirect(url_for("index"))
        report = scan_url(target)
        os.makedirs("scans", exist_ok=True)
        safe_name = target.replace("://", "_").replace("/", "_")
        fname = os.path.join("scans", f"{safe_name}.json")
        with open(fname, "w") as f:
            json.dump(report, f, indent=2)
        return redirect(url_for("results", fname=os.path.basename(fname)))
    return render_template("index.html")

@app.route("/results/<fname>")
def results(fname):
    path = os.path.join("scans", fname)
    if not os.path.exists(path):
        return "Not found", 404
    with open(path) as f:
        report = json.load(f)
    return render_template("results.html", report=report)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
