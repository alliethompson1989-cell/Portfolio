# SQL data validation checks

**Scenario:** A fictional scheduling application exports appointment records and external integration statuses. Some records have been intentionally corrupted for a repeatable quality check.

**What the SQL checks:**

1. Orphaned foreign keys (appointments tied to a provider who does not exist).
2. Duplicate external references that could cause ambiguous syncing.
3. Status disagreements between the application and a fictional external event system.
4. Missing external references.

**Run from the repository root:**

```bash
python projects/sql-validation/run_checks.py
```

No database server or extra Python package is required; the script loads the included SQLite schema into memory and prints results. In a production workflow, I'd verify the canonical status definitions and integration contract *before* treating a mismatch as an actual defect.

**Important:** All records and rules are fictional. Nothing here represents patient, customer, or employer data.
