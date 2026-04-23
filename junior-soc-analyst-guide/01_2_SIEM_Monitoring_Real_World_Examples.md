# SIEM Monitoring Real-World Examples

These examples mirror the kinds of alerts a Junior SOC Analyst may see during daily monitoring. The goal is to practice reading the alert, checking surrounding evidence, and deciding what should happen next.

---

## Example 1: Repeated MFA Pushes Followed by Successful Login

### Scenario
A SIEM correlation rule triggers because a user received 12 MFA push requests in 8 minutes, followed by a successful login from a new device.

### Alert Details
- Alert source: SIEM identity correlation rule
- User: finance.ap.manager@company.com
- First event: 9:14 PM local time
- Successful login: 9:22 PM local time
- Source IP location: Different state from the user's normal location
- Device: New Windows workstation, not previously seen for this user
- Authentication method: Password plus MFA push approval

### What the Analyst Checks
1. Review the user's normal login pattern for the last 30 days.
2. Check whether the user usually works after hours.
3. Compare the source IP against known VPN, office, and travel locations.
4. Look for mailbox rule changes, file downloads, or privilege changes after login.
5. Check whether other users received MFA push bursts from the same source IP.

### Realistic Findings
- The user normally logs in between 7:30 AM and 6:00 PM.
- No approved travel record exists for the user.
- The IP is from a residential internet provider, not the company VPN.
- After login, the account accessed email and opened several finance folders in SharePoint.
- No mailbox forwarding rule was created yet.

### Decision
Treat as suspicious and escalate to identity/security operations. The pattern may indicate MFA fatigue where the user accidentally approved a malicious login.

### Ticket Notes Example
```
Observed 12 MFA push attempts for finance.ap.manager@company.com between 21:14 and 21:22, followed by successful login from new device and unusual residential IP. User normally authenticates from corporate VPN during business hours. Post-login activity includes access to email and finance SharePoint folders. No mailbox forwarding rule observed at time of review. Recommend account containment, user confirmation, session revocation, and password reset.
```

---

## Example 2: Endpoint Alert for Suspicious PowerShell

### Scenario
An endpoint tool sends an alert to the SIEM after PowerShell starts with encoded command-line content on a user's laptop.

### Alert Details
- Host: LAP-2044
- User: operations.coordinator@company.com
- Process: powershell.exe
- Parent process: winword.exe
- Event time: 10:36 AM
- Severity: High
- Detection reason: Office application spawned script interpreter

### What the Analyst Checks
1. Confirm whether the parent process really was Microsoft Word.
2. Review file name and location of the opened document.
3. Check whether the file came from email, browser download, or shared drive.
4. Look for network connections immediately after PowerShell executed.
5. Check if the endpoint tool blocked or allowed the activity.

### Realistic Findings
- Word opened a document named `Updated_Invoice_April.docm`.
- The document came from an external email sender.
- PowerShell attempted to connect to an unknown external domain.
- Endpoint protection blocked the child process and quarantined the document.
- No second-stage process was observed after the block.

### Decision
Escalate as attempted malware delivery through a malicious document. Even if blocked, the email may have reached other users.

### Ticket Notes Example
```
Endpoint alert on LAP-2044 shows WINWORD.EXE spawning POWERSHELL.EXE after user opened Updated_Invoice_April.docm from external email. PowerShell attempted outbound connection to unknown external domain. EDR reports process blocked and document quarantined. No confirmed payload execution observed. Recommend phishing mailbox search for same sender/attachment and user awareness follow-up.
```

---

## Example 3: Spike in Failed VPN Logins

### Scenario
The SIEM dashboard shows a sudden increase in failed VPN logins across many accounts.

### Alert Details
- Time window: 2:00 AM to 2:45 AM
- Failed logins: 480
- Affected accounts: 62
- Source IPs: 4 external IP addresses
- Successful logins: 0 from the suspicious IPs
- Target system: VPN gateway

### What the Analyst Checks
1. Determine if the same source IPs are rotating across many usernames.
2. Check whether any account eventually had a successful login.
3. Identify whether targeted users share a department or naming pattern.
4. Compare source IPs with threat intelligence and known scanners.
5. Confirm whether account lockouts occurred.

### Realistic Findings
- Usernames are common corporate email formats.
- No successful authentication occurred.
- Five accounts were temporarily locked.
- The IPs are not company infrastructure.
- Attempts stopped after automated blocking was applied by the VPN control.

### Decision
Document as password spraying or credential stuffing attempt. Escalate if a successful login appears, if executive accounts were targeted, or if lockouts affect business operations.

### Ticket Notes Example
```
Detected broad VPN authentication failures: 480 attempts against 62 users from 4 external IPs between 02:00 and 02:45. No successful logins from suspicious sources. Five temporary lockouts observed. Pattern is consistent with password spraying. VPN control applied automated block. Recommend monitoring for reattempts, confirming lockout impact, and reviewing targeted account list for privileged users.
```

