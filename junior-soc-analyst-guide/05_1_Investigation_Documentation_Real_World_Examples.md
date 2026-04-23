# Investigation Documentation Real-World Examples

These examples show how investigation notes can be written so another analyst, manager, or auditor can understand what happened without needing to repeat the work.

---

## Example 1: Suspicious Login Investigation Record

### Scenario
A user reports that they received an MFA prompt they did not initiate. The SIEM also shows a successful login from a new device.

### Good Investigation Summary
```
At 09:22 on 2026-04-23, user finance.ap.manager@company.com successfully authenticated to Microsoft 365 from a new Windows device and a residential IP address not previously associated with the user. The login followed 12 MFA push attempts between 09:14 and 09:22. User confirmed by phone that they did not initiate the login or approve the MFA request intentionally.

Initial assessment: Suspected account compromise through MFA fatigue.
Current status: Escalated to Identity team for session revocation, password reset, and MFA method review.
```

### Timeline Example
| Time | Event |
| --- | --- |
| 09:14 | First MFA push attempt observed |
| 09:14-09:22 | 12 total MFA push attempts sent |
| 09:22 | Successful login from new device |
| 09:26 | SIEM correlation alert generated |
| 09:31 | Analyst reviewed login history and device details |
| 09:38 | User confirmed activity was not expected |
| 09:42 | Escalated to Identity team |

### Evidence Recorded
- SIEM alert ID
- User principal name
- Source IP and approximate geolocation
- Device ID or device fingerprint
- Screenshot or export of authentication logs
- User confirmation method and time

### Strong Closing Note
```
No mailbox forwarding rule or privilege change observed during initial review. SharePoint access occurred after suspicious login and should be reviewed by Tier 2. Analyst did not perform containment directly; escalation sent to Identity queue at 09:42.
```

---

## Example 2: Malware Alert Documentation

### Scenario
An endpoint detects and blocks a malicious document opened by a user.

### Good Investigation Summary
```
At 10:36 on 2026-04-23, EDR generated a high-severity alert on LAP-2044 for WINWORD.EXE spawning POWERSHELL.EXE after the user opened Updated_Invoice_April.docm. The document originated from an external email. EDR blocked the child process and quarantined the file. No confirmed second-stage execution was observed in endpoint telemetry available to Tier 1.

Initial assessment: Attempted malware delivery via malicious Office document. Blocked at endpoint, but possible email campaign exposure exists.
```

### Timeline Example
| Time | Event |
| --- | --- |
| 10:28 | Email delivered to user mailbox |
| 10:35 | User opened attachment |
| 10:36 | Word spawned suspicious PowerShell process |
| 10:36 | EDR blocked process and quarantined document |
| 10:41 | SOC reviewed email sender and attachment details |
| 10:48 | SOC found same sender delivered email to 14 recipients |
| 10:53 | Escalated to email security team |

### Evidence Recorded
- Endpoint hostname
- Logged-in user
- Parent and child process names
- Attachment name and hash, if available
- Email sender and subject
- EDR disposition: blocked, quarantined, allowed, or unknown
- List or count of other recipients

### Common Documentation Mistake
Do not write only "malware blocked, closing ticket." A blocked alert can still matter if the same message was delivered to other mailboxes or if the user opened additional files.

---

## Example 3: DLP Alert With Business Validation

### Scenario
A DLP alert shows a finance user uploaded a large spreadsheet to an external sharing site.

### Good Investigation Summary
```
At 16:52 on 2026-04-23, DLP generated an alert for finance.analyst@company.com uploading Investor_Redemption_Report_Q2.xlsx to an external file-sharing service. The file name suggests sensitive finance data. The user role and quarter-end timing may support a legitimate business purpose, but the destination service was not visible in the approved vendor list available to SOC.

Initial assessment: Requires business validation before final classification.
```

### Timeline Example
| Time | Event |
| --- | --- |
| 16:52 | DLP alert generated |
| 16:58 | Analyst confirmed user role and department |
| 17:04 | Analyst checked approved vendor list |
| 17:10 | Escalated to Finance data owner for validation |
| 17:31 | Manager confirmed upload was expected but vendor approval needed |
| 17:45 | Compliance team added for policy review |

### Evidence Recorded
- File name and size
- User and department
- Destination domain or application
- DLP policy name
- Business owner contacted
- Final validation result

### Strong Closing Note
```
Classification remains pending until Compliance confirms whether the destination is approved for this data type. Business owner confirmed the activity was expected for quarter-end reporting, but approval status is unresolved.
```

