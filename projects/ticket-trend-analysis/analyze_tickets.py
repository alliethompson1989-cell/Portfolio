"""Summarize patterns in a fictional support queue using only the Python standard library."""

from collections import Counter
import csv
from datetime import date
from pathlib import Path
import sys

REQUIRED_FIELDS = {"id", "opened_date", "status", "severity", "product_area", "symptom"}


def load_tickets(path):
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not REQUIRED_FIELDS.issubset(set(reader.fieldnames or [])):
            raise ValueError(f"CSV must contain: {', '.join(sorted(REQUIRED_FIELDS))}")
        rows = list(reader)
    if any(not all(row.get(field) for field in REQUIRED_FIELDS) for row in rows):
        raise ValueError("Every ticket must have all required fields populated")
    if len({row['id'] for row in rows}) != len(rows):
        raise ValueError("Duplicate ticket IDs found")
    return rows


def summarize(rows, as_of=date(2026, 10, 31), aging_days=14):
    if aging_days < 0:
        raise ValueError("aging_days must be nonnegative")
    areas = Counter(row["product_area"] for row in rows)
    symptoms = Counter(row["symptom"] for row in rows)
    open_rows = [row for row in rows if row["status"].strip().casefold() != "resolved"]
    aged = []
    for row in open_rows:
        days = (as_of - date.fromisoformat(row["opened_date"])).days
        if days >= aging_days:
            aged.append((row["id"], days))
    return {
        "total": len(rows),
        "unresolved": len(open_rows),
        "by_area": areas.most_common(),
        "repeated_symptoms": [(symptom, count) for symptom, count in symptoms.most_common() if count >= 2],
        "aged_open": sorted(aged, key=lambda entry: (-entry[1], entry[0])),
    }


def render(result):
    lines = [
        "SUPPORT QUEUE REVIEW | SYNTHETIC DATA",
        f"Total tickets: {result['total']}",
        f"Not resolved: {result['unresolved']}",
        "",
        "Tickets by product area:",
    ]
    lines += [f"  {area}: {count}" for area, count in result["by_area"]]
    lines.append("\nRepeated symptoms (signals to investigate, not confirmed causes):")
    lines += [f"  {symptom}: {count}" for symptom, count in result["repeated_symptoms"]]
    lines.append("\nOpen tickets at least 14 days old:")
    lines += [f"  {ticket_id}: {days} days" for ticket_id, days in result["aged_open"]]
    return "\n".join(lines)


if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("sample_tickets.csv")
    print(render(summarize(load_tickets(source))))
