# Runbooks and Playbooks Real-World Examples

These examples show how an analyst follows written procedures during realistic SOC work. The key skill is to follow the process, record deviations, and escalate when the playbook reaches a decision point.

---

## Example 1: Phishing Email Report Playbook

### Scenario
An employee reports a suspicious invoice email using the company phishing report button.

### Playbook Followed
Phishing Report Handling Playbook

### Steps Taken
1. Confirm the reported message is preserved in the phishing mailbox or email security console.
2. Review sender address, reply-to address, subject, links, and attachments.
3. Check whether the same sender or subject was delivered to other users.
4. Detonate or submit attachment/link using approved tools only.
5. Classify the email as malicious, suspicious, legitimate, or inconclusive.
6. If malicious, request message purge from all affected mailboxes.
7. Notify the reporting user with the approved response template.

### Decision Point
The playbook says to escalate if the email was delivered to more than 10 users or if any user clicked a suspicious link.

### Realistic Outcome
- The email was delivered to 22 users.
- Two users clicked the link.
- The analyst escalated to Tier 2 and email security for purge and clicker review.

### Documentation Example
```
Followed Phishing Report Handling Playbook through Step 6. Message assessed as malicious due to credential-harvesting link and mismatched sender domain. Delivery search found 22 recipients. URL click logs show 2 users clicked. Escalated at playbook decision point for user impact review and mailbox purge.
```

---

## Example 2: Lost Laptop Runbook

### Scenario
A manager reports that an employee left a corporate laptop in a taxi after a client meeting.

### Runbook Followed
Lost or Stolen Endpoint Runbook

### Steps Taken
1. Open an incident ticket and record reporter, user, asset tag, and time of loss.
2. Confirm whether the device is enrolled in endpoint management.
3. Check last check-in time, last known location, and encryption status.
4. Confirm whether the user had local administrator access.
5. Initiate remote lock or wipe only according to approval rules.
6. Disable or review active sessions for the user if required.
7. Notify asset management and the user's manager.

### Decision Point
The runbook requires management approval before remote wipe unless the device is confirmed stolen or contains regulated data.

### Realistic Outcome
- Device was encrypted.
- Last check-in was 23 minutes before the report.
- User handled client contact lists but not regulated financial records.
- Manager approved remote lock first, with wipe held pending recovery attempt.

### Documentation Example
```
Followed Lost or Stolen Endpoint Runbook. Device LAP-1188 is encrypted and enrolled in endpoint management. Last check-in 14:12. Remote lock initiated after manager approval. Remote wipe not performed because device is not confirmed stolen and manager requested recovery window. Asset management notified.
```

---

## Example 3: Ransomware Alert Playbook

### Scenario
EDR generates an alert for rapid file rename activity and known ransomware-like behavior on a file server.

### Playbook Followed
Suspected Ransomware Response Playbook

### Steps Taken
1. Confirm alert details and affected host.
2. Check whether file modifications are ongoing.
3. Identify user account responsible for the file operations.
4. Isolate endpoint or server according to emergency containment rules.
5. Escalate to Incident Response immediately.
6. Preserve logs and avoid deleting evidence.
7. Track business impact and affected shares.

### Decision Point
The playbook allows immediate containment if encryption-like behavior is active.

### Realistic Outcome
- File modification activity was ongoing.
- The responsible account was a normal user account accessing a shared drive.
- The affected endpoint was isolated.
- Incident Response took ownership for containment and recovery.

### Documentation Example
```
Followed Suspected Ransomware Response Playbook. Alert showed active rapid file rename behavior against shared drive paths. Activity was ongoing at time of review. Account j.santos@company.com was associated with file operations. Endpoint LAP-3320 isolated under emergency containment rule. Escalated to IR at 11:08 with affected share details and SIEM/EDR alert IDs.
```

