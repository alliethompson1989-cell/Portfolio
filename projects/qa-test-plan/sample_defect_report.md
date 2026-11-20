# Example defect report (fictional)

**ID:** QA-DEMO-04  
**Title:** Rescheduling reports success when external calendar update fails  
**Severity:** High (potential scheduling discrepancy)  
**Environment:** Demonstration environment; invented behavior

## Preconditions

- Staff role can edit an appointment.
- An appointment exists with an active external calendar association.
- External calendar request is configured to respond with HTTP 503.

## Steps to reproduce

1. Open the existing appointment.
2. Select a new available time.
3. Save the change while the external calendar endpoint returns 503.
4. Observe the success message and refresh the appointment.
5. Compare the application record with the integration event state.

## Expected

The system either confirms a fully committed change or clearly indicates a partial failure with a recoverable state. The UI must not imply both systems were updated when only one was.

## Actual (invented for this work sample)

The UI displays “Appointment updated” even though the external calendar was not updated.

## Evidence to request

- Correlation ID, sanitized request/response, and timestamp.
- Application record before and after Save.
- Retry or dead-letter queue behavior, if present.

## Suggested investigation

Check transaction boundaries, async job handling, retry semantics, and UI success criteria. Confirm whether the issue is reproducible outside the controlled failure test.

*All details are fictional and provided only to show defect-documentation style.*
