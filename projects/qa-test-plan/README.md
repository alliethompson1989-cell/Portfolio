# QA test plan: appointment rescheduling

**Scenario:** A fictional healthcare scheduling application allows staff to reschedule appointments. The goal is to verify workflow behavior, not just whether the Save button can be clicked.

## Example acceptance criteria

- A permitted staff member can choose an available future time and save the change.
- The appointment displays the updated time after refresh.
- A conflicting slot cannot be booked.
- An unauthorized role cannot reschedule the appointment.
- A failed integration must not silently show success.
- Keyboard-only users can complete the operation, and validation messages are announced accessibly.

## Test coverage

See [test_matrix.csv](test_matrix.csv) for positive, negative, permission, integration, and accessibility scenarios. See [sample_defect_report.md](sample_defect_report.md) for an example of a reproducible defect write-up.

## Release questions

What happens if the integration updates but the local save fails? Who owns the reconciliation? Is there a reliable audit trail? Do UI status messages reflect the real committed state?

**Important:** This is an invented product and a work-sample exercise. No real patient or employer information is used.
