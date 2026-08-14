import json
import os
from datetime import datetime

TRACKER_FILE = "scores.json"

def load_scores():
    if not os.path.exists(TRACKER_FILE):
        return []
    with open(TRACKER_FILE, "r") as f:
        return json.load(f)

def save_score(problem: str, verdict: str, intent: str, language: str = ""):
    scores = load_scores()
    scores.append({
        "date":     datetime.now().strftime("%Y-%m-%d %H:%M"),
        "problem":  problem[:80] + "..." if len(problem) > 80 else problem,
        "intent":   intent,
        "verdict":  verdict,
        "language": language,
    })
    with open(TRACKER_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def get_stats():
    scores = load_scores()
    if not scores:
        return {"total": 0, "passed": 0, "failed": 0, "pass_rate": 0}
    evaluations = [s for s in scores if s["intent"] == "evaluator"]
    passed = len([s for s in evaluations if "PASS" in s["verdict"].upper()])
    failed = len([s for s in evaluations if "FAIL" in s["verdict"].upper()])
    total  = len(evaluations)
    return {
        "total":     total,
        "passed":    passed,
        "failed":    failed,
        "pass_rate": round((passed / total * 100) if total > 0 else 0, 1),
    }
