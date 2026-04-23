# Triage Scenario Analysis

This document provides detailed triage analysis for the scenarios outlined in `02_2_Triage_Scenarios.md`. Each analysis includes initial assessment, validation steps, determination, and recommended actions.

## Scenario 1: Multiple Failed Login Attempts

### Triage Analysis
- **Initial Assessment**: Review the source IP address. Check if it's from a known corporate network, VPN, or external location. Verify the target account(s) affected.
- **Validation Steps**:
  - Query SIEM for related logs (e.g., successful logins from the same IP, user behavior).
  - Check threat intelligence for the IP (e.g., is it blacklisted?).
  - Correlate with user reports of login issues.
- **Determination**: Likely a true positive if the IP is external and not associated with legitimate access. Could be brute-force attack or credential stuffing.
- **Recommended Actions**:
  - Block the IP at the firewall if malicious.
  - Notify the affected user to change passwords.
  - Escalate to incident response if multiple accounts are targeted.

## Scenario 2: Unusual Outbound Traffic

### Triage Analysis
- **Initial Assessment**: Identify the source server, destination domain, and type/volume of traffic.
- **Validation Steps**:
  - Confirm the domain's reputation using threat intelligence tools.
  - Check server logs for processes initiating the connection.
  - Review firewall/proxy logs for similar traffic patterns.
- **Determination**: True positive if the domain is confirmed malicious and traffic is unauthorized.
- **Recommended Actions**:
  - Isolate the affected server.
  - Scan for malware.
  - Block the domain in DNS/firewall.
  - Investigate for data exfiltration.

## Scenario 3: High CPU Usage Alert

### Triage Analysis
- **Initial Assessment**: Verify the server's role and normal usage patterns. Check for recent changes or deployments.
- **Validation Steps**:
  - Log into the server to check running processes (e.g., via Task Manager or top).
  - Review system logs for errors or unusual activity.
  - Correlate with network traffic or user sessions.
- **Determination**: Could be true positive (e.g., cryptomining malware) or false positive (legitimate high-load process). True if no authorized activity explains it.
- **Recommended Actions**:
  - If malicious, isolate and scan the server.
  - If benign, optimize the application or schedule appropriately.
  - Monitor for recurrence.

## Scenario 4: Anomalous File Creation

### Triage Analysis
- **Initial Assessment**: Confirm the user account's permissions and normal behavior. Check the files created (names, hashes).
- **Validation Steps**:
  - Scan files with antivirus or submit to sandbox.
  - Review user activity logs (e.g., login times, other actions).
  - Check for privilege escalation attempts.
- **Determination**: True positive if files are malicious or unauthorized. False if legitimate admin task.
- **Recommended Actions**:
  - Quarantine/remove malicious files.
  - Revoke elevated privileges if abused.
  - Investigate user account compromise.

## Scenario 5: Suspicious Process with Elevated Privileges

### Triage Analysis
- **Initial Assessment**: Note that svchost.exe is a legitimate Windows process, but check for anomalies (e.g., unusual parent process, network connections).
- **Validation Steps**:
  - Use tools like Process Explorer to inspect the process details.
  - Check network connections via netstat or firewall logs.
  - Verify against known good hashes or signatures.
- **Determination**: Likely true positive if the process is masquerading or connecting to suspicious IPs.
- **Recommended Actions**:
  - Terminate the suspicious process.
  - Scan the system for malware.
  - Update and patch the system.

## Scenario 6: Phishing Email with Malicious Attachment

### Triage Analysis
- **Initial Assessment**: Review email headers, sender reputation, and attachment details.
- **Validation Steps**:
  - Analyze the attachment in a sandbox environment.
  - Check sender domain for spoofing.
  - Search for similar emails in the organization.
- **Determination**: True positive phishing attempt.
- **Recommended Actions**:
  - Quarantine the email.
  - Notify recipients not to open.
  - Report to phishing response team.
  - Educate users on phishing awareness.

## Scenario 7: VPN Connection from Unusual Location

### Triage Analysis
- **Initial Assessment**: Verify user's location and travel status. Check IP geolocation accuracy.
- **Validation Steps**:
  - Correlate with user's calendar or travel records.
  - Review VPN logs for authentication method (e.g., MFA).
  - Check for concurrent sessions from legitimate locations.
- **Determination**: True positive if user is not traveling and IP is suspicious.
- **Recommended Actions**:
  - Force logout and require password change.
  - Enable MFA if not already.
  - Investigate for account compromise.

## Scenario 8: Large Data Transfer to External Storage

### Triage Analysis
- **Initial Assessment**: Identify the user, data type, and destination service.
- **Validation Steps**:
  - Review data classification (is it sensitive?).
  - Check user's permissions and intent (e.g., via interview).
  - Monitor for similar activity.
- **Determination**: True positive if unauthorized data exfiltration.
- **Recommended Actions**:
  - Block the transfer and quarantine data.
  - Investigate user's device.
  - Escalate to legal/HR if policy violation.

## Scenario 9: Repeated Access to Sensitive Files

### Triage Analysis
- **Initial Assessment**: Confirm file permissions and user's access level.
- **Validation Steps**:
  - Check audit logs for access patterns.
  - Interview the user about the activity.
  - Review for insider threat indicators.
- **Determination**: True positive if unauthorized access.
- **Recommended Actions**:
  - Revoke access.
  - Log security incident.
  - Monitor user activity closely.

## Scenario 10: Malware Signature Match

### Triage Analysis
- **Initial Assessment**: Isolate the device immediately to prevent spread.
- **Validation Steps**:
  - Confirm the signature with updated definitions.
  - Check for encryption or file changes.
  - Review recent user activity.
- **Determination**: True positive ransomware infection.
- **Recommended Actions**:
  - Disconnect from network.
  - Run full scan and removal.
  - Restore from backup if needed.
  - Escalate to incident response.

## Scenario 11: Unusual Network Scan

### Triage Analysis
- **Initial Assessment**: Identify the source workstation and scan targets.
- **Validation Steps**:
  - Check installed software on the workstation.
  - Review user permissions.
  - Correlate with other alerts.
- **Determination**: True positive if unauthorized scanning (potential reconnaissance).
- **Recommended Actions**:
  - Isolate the workstation.
  - Investigate for malware or misuse.
  - Update network segmentation.

## Scenario 12: Account Lockout Storm

### Triage Analysis
- **Initial Assessment**: Check for coordinated attack or system issue.
- **Validation Steps**:
  - Review authentication logs for patterns.
  - Verify account lockout policies.
  - Check for brute-force tools in use.
- **Determination**: True positive if external IPs involved.
- **Recommended Actions**:
  - Implement rate limiting.
  - Notify users to secure accounts.
  - Monitor for further attacks.

## Scenario 13: Unexpected Service Startup

### Triage Analysis
- **Initial Assessment**: Identify the service and communication details.
- **Validation Steps**:
  - Check service configuration.
  - Review startup logs.
  - Test service legitimacy.
- **Determination**: True positive if unauthorized.
- **Recommended Actions**:
  - Stop and disable the service.
  - Scan for backdoors.
  - Patch vulnerabilities.

## Scenario 14: Privilege Escalation Attempt

### Triage Analysis
- **Initial Assessment**: Confirm the exploit and vulnerability.
- **Validation Steps**:
  - Check patch levels.
  - Review access logs.
  - Test for successful escalation.
- **Determination**: True positive exploit attempt.
- **Recommended Actions**:
  - Apply patches immediately.
  - Audit domain controller access.
  - Escalate to security team.

## Scenario 15: Data Exfiltration via Email

### Triage Analysis
- **Initial Assessment**: Verify the email content and sender.
- **Validation Steps**:
  - Check password change logs.
  - Interview the account owner.
  - Assess data sensitivity.
- **Determination**: True positive if unauthorized.
- **Recommended Actions**:
  - Quarantine the email.
  - Secure the account.
  - Investigate for breach.