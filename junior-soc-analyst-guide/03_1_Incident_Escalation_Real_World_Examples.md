# Incident Escalation Real-World Examples

These examples show how a Junior SOC Analyst can decide whether to escalate, who to contact, and what information to include. The scenarios are written to reflect realistic SOC handoffs where clarity and timing matter.

---

## Example 1: Confirmed Malware Blocked on One Laptop

### Scenario
An endpoint alert shows a malicious document was opened, but the payload was blocked before execution.

### Initial Facts
- User: operations.coordinator@company.com
- Device: LAP-2044
- Detection: Malicious macro behavior blocked
- Current status: Endpoint online, user still logged in
- Business impact: No confirmed data loss or outage
- Related alerts: Same sender delivered email to 14 users

### Escalation Decision
Escalate to the security operations or incident response queue as a medium-to-high priority because the initial endpoint was protected, but the same campaign may affect other users.

### Who to Notify
- Tier 2 SOC or Incident Response team
- Email security administrator
- Service desk, if user contact or device isolation is needed

### Escalation Message Example
```
Priority: Medium/High
Issue: Blocked malware attempt from suspicious email attachment

EDR detected and blocked malicious macro behavior on LAP-2044 for operations.coordinator@company.com at 10:36 AM. Parent process was WINWORD.EXE after opening Updated_Invoice_April.docm from an external sender. No confirmed payload execution observed. SIEM shows same sender delivered similar email to 14 internal recipients.

Requested actions:
- Search and remove related email from all mailboxes
- Confirm whether any other recipient opened the attachment
- Review LAP-2044 for additional post-alert activity
- Advise whether device isolation is required
```

### Why This Is the Right Escalation
The analyst does not need to prove full compromise before escalating. The combination of malicious document behavior and multiple recipients creates campaign risk.

---

## Example 2: Privileged Account Login From Unexpected Country

### Scenario
A domain admin account logs in successfully from a country where the administrator is not located.

### Initial Facts
- Account: admin.network@company.com
- Account type: Privileged administrator
- Login time: 3:18 AM local time
- Source location: Foreign country not used by the company
- MFA: Successful
- User confirmation: Admin is asleep and did not approve login

### Escalation Decision
Escalate immediately as critical. This is a suspected privileged account compromise.

### Who to Notify
- Incident Response lead
- Identity and Access Management team
- SOC manager or on-call security lead
- Infrastructure owner for domain services

### Escalation Message Example
```
Priority: Critical
Issue: Suspected privileged account compromise

admin.network@company.com successfully authenticated at 03:18 from an unexpected foreign IP. The account has domain admin privileges. MFA was recorded as successful, but user confirmation indicates the admin did not initiate or approve the login.

Immediate concerns:
- Privileged account exposure
- Possible active session in cloud or domain environment
- Potential lateral movement risk

Requested actions:
- Revoke active sessions
- Disable or reset privileged account credentials per procedure
- Review administrative activity since 03:18
- Check for new users, group changes, mailbox changes, and remote access activity
```

### Why This Is the Right Escalation
Privileged accounts have high blast radius. Waiting for additional proof can allow the attacker more time to change access or move laterally.

---

## Example 3: Possible False Positive That Still Needs Business Owner Review

### Scenario
A data loss prevention alert fires when a finance analyst uploads a large spreadsheet to an external file-sharing site.

### Initial Facts
- User: finance.analyst@company.com
- File name: `Investor_Redemption_Report_Q2.xlsx`
- Destination: External file-sharing service
- File size: 88 MB
- Time: 4:52 PM
- User role: Finance team
- Business context: Quarter-end reporting period

### Escalation Decision
Escalate to the user's manager or data owner for business validation, not necessarily full incident response yet.

### Who to Notify
- Finance data owner or manager
- DLP team or Tier 2 SOC
- Compliance team, depending on policy

### Escalation Message Example
```
Priority: Medium
Issue: DLP validation needed for external file upload

DLP alert observed for finance.analyst@company.com uploading Investor_Redemption_Report_Q2.xlsx, 88 MB, to an external file-sharing service at 16:52. User is in Finance and quarter-end reporting is active, so this may be legitimate business activity. Destination is not on the standard approved vendor list visible to SOC.

Requested validation:
- Confirm whether the upload was approved business activity
- Confirm whether the destination service/vendor is authorized
- Advise whether file removal or access restriction is required
```

### Why This Is the Right Escalation
Not every alert goes directly to emergency response. Some require business validation because the security team cannot determine legitimacy from logs alone.

