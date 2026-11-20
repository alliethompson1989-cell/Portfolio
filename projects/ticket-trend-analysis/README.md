# Ticket trend review

**Scenario:** A fictional healthcare SaaS support queue contains overlapping reports of access, integration, reporting, and scheduling issues. The goal is to separate recurring symptoms from isolated tickets and produce a short list of follow-up questions for Product and Engineering.

**Method:** Read CSV records, validate required fields, count issue clusters, and flag unresolved tickets past an aging threshold. The report distinguishes *signals* from confirmed root causes.

**Run from the repository root:**

```bash
python projects/ticket-trend-analysis/analyze_tickets.py
python -m unittest discover -s projects/ticket-trend-analysis -p 'test_*.py'
```

**What I'd check next:** Are the recurring sync delays limited to one integration or configuration? Did the access complaints begin after the same role change? Do logs and system records support the ticket narrative? Could documented workarounds be masking a systemic defect?

**Important:** All records are fictional. This is a self-contained demonstration, not a report from a real employer or production environment.
