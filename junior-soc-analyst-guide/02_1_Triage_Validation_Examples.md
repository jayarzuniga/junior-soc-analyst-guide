# Triage Validation Real-World Examples

This document provides multiple real-world examples of performing triage validation on security alerts, following the step-by-step process outlined in the triage validation guide.

## Example 1: Suspicious Email Attachment Alert

### Scenario
An email security gateway alerts on a message containing a suspicious attachment (.exe file) sent to a finance department user.

### Step 1: Receive and Initial Assessment
- Alert received from email security tool at 2:15 PM
- Alert title: "Malicious Attachment Detected"
- Description: Suspicious .exe file attached to email from external sender
- No duplicate alerts in the last 24 hours
- This alert type has been seen before in phishing campaigns

### Step 2: Gather Contextual Information
- Affected user: john.doe@company.com (Finance Analyst)
- System: User's corporate laptop (Windows 10, asset ID: LAP-12345)
- User role: Finance department, handles sensitive financial data
- Last login: 8:30 AM today from office IP
- System is actively monitored with endpoint protection
- Asset owner: IT Department, criticality: High (handles financial data)

### Step 3: Understand the Alert Details
- Email sender: external@competitor-company.com
- Subject: "Q4 Financial Report Update"
- Attachment: "Q4_Report_Update.exe" (SHA256: a1b2c3d4...)
- Email gateway flagged based on file type and sender reputation
- No other suspicious indicators in the email content

### Step 4: Check for False Positive Indicators
- This is not a known legitimate activity; .exe attachments are generally blocked
- No maintenance window or admin changes noted
- User does not normally receive executable files
- Attachment not whitelisted; company policy prohibits .exe files in emails
- Software is not authorized; this appears to be potential malware

### Step 5: Validate Against Business Context
- Business activity: Normal workday, no special events
- User should not be receiving executable files from external competitors
- Timing is during work hours, but content is suspicious
- Does not align with normal behavior (finance analysts receive PDFs/reports, not executables)
- Asset location: Office network, expected access

### Step 6: Document Triage Assessment
- Checked email headers, user reports, attachment analysis
- Found: Suspicious sender, unauthorized file type, potential phishing attempt
- Classification: **True Positive** - Legitimate security concern
- Confidence level: High (85%)
- Next action: Escalate to incident response team for malware analysis

### Step 7: Make Triage Decision
- Escalation needed: High severity due to potential malware infection
- Priority: High
- Assigned to: Malware Analysis Team

---

## Example 2: Failed Login Attempts from Unusual Location

### Scenario
SIEM alert for multiple failed login attempts to a user's account from an IP address in Russia, while the user is known to be in the US office.

### Step 1: Receive and Initial Assessment
- Alert received from SIEM at 3:45 AM
- Alert title: "Multiple Failed Authentication Attempts"
- Description: 15 failed login attempts to user account from IP 185.123.45.67
- No duplicate alerts for this user in last 7 days
- Similar alerts have been seen in past brute force attacks

### Step 2: Gather Contextual Information
- Affected user: sarah.smith@company.com (Marketing Manager)
- System: Active Directory domain authentication
- User role: Marketing department, standard user access
- Last successful login: Yesterday at 5:30 PM from office IP (192.168.1.100)
- User is actively employed and system monitored
- Asset owner: IT Department, criticality: Medium

### Step 3: Understand the Alert Details
- Source IP: 185.123.45.67 (Russia, known malicious IP range)
- Target account: sarah.smith@company.com
- Failed attempts: 15 total, over 10-minute period
- Authentication method: VPN login attempts
- No successful logins from this IP

### Step 4: Check for False Positive Indicators
- Not a known legitimate activity; user is in US timezone
- No admin changes or maintenance noted
- User behavior: Sarah is not traveling and doesn't have international access needs
- IP not whitelisted; company blocks known malicious ranges
- Not authorized software or activity

### Step 5: Validate Against Business Context
- Business activity: Off-hours, normal operations
- User should not be accessing from Russia; no business travel planned
- Timing is suspicious (3 AM US time = 10 AM Russia time)
- Does not align with normal behavior (user typically logs in during business hours)
- Asset location: Remote access attempt, but from unexpected geography

### Step 6: Document Triage Assessment
- Checked user location, login history, IP geolocation
- Found: Failed attempts from known malicious IP, user not traveling
- Classification: **True Positive** - Potential account compromise attempt
- Confidence level: High (90%)
- Next action: Disable account temporarily, notify user

### Step 7: Make Triage Decision
- Escalation needed: Medium severity, potential credential theft
- Priority: Medium
- Assigned to: Identity Protection Team

---

## Example 3: Endpoint Malware Detection

### Scenario
Endpoint detection and response (EDR) tool alerts on suspicious process activity on a developer's workstation.

### Step 1: Receive and Initial Assessment
- Alert received from EDR tool at 11:20 AM
- Alert title: "Suspicious Process Execution"
- Description: Unknown process "svchost.exe" spawning from unusual location
- Duplicate of similar alert from same system 2 days ago
- This type of alert common with malware infections

### Step 2: Gather Contextual Information
- Affected system: DEV-WKS-001 (Developer workstation)
- User: mike.johnson@company.com (Software Developer)
- User role: Development team, has admin rights on dev machines
- Last login: 8:45 AM today from office
- System monitored with full EDR coverage
- Asset owner: Development Department, criticality: High (contains source code)

### Step 3: Understand the Alert Details
- Process: svchost.exe (legitimate Windows process)
- Unusual behavior: Spawned from C:\Users\mike\AppData\Temp\
- Command line: svchost.exe -k netsvcs -p -s Schedule
- File hash: Matches known malware family
- Network connections: Attempting outbound to C2 server

### Step 4: Check for False Positive Indicators
- Process name is legitimate, but location and behavior suspicious
- Developer was not performing admin tasks at that time
- No maintenance window active
- User behavior: Mike reports no unusual activity
- Process not whitelisted for that location
- Software not authorized in temp directory

### Step 5: Validate Against Business Context
- Business activity: Normal development work
- User should not be running services from temp directory
- Timing during work hours, but suspicious execution
- Does not align with normal development activities
- Asset location: Office network, expected

### Step 6: Document Triage Assessment
- Checked process details, file analysis, network logs
- Found: Malware masquerading as legitimate process, C2 communication
- Classification: **True Positive** - Active malware infection
- Confidence level: High (95%)
- Next action: Isolate system, begin malware analysis

### Step 7: Make Triage Decision
- Escalation needed: High severity, active compromise
- Priority: Critical
- Assigned to: Incident Response Team

---

## Example 4: Unusual Data Transfer

### Scenario
Data Loss Prevention (DLP) alert for large outbound data transfer from a user's workstation.

### Step 1: Receive and Initial Assessment
- Alert received from DLP tool at 4:30 PM
- Alert title: "Large Data Exfiltration Attempt"
- Description: 2GB of sensitive files transferred to external USB device
- No recent duplicates for this user
- Similar alerts seen in past data theft incidents

### Step 2: Gather Contextual Information
- Affected user: lisa.brown@company.com (HR Manager)
- System: HR-LAP-567 (HR Department laptop)
- User role: Human Resources, handles sensitive employee data
- Last login: 8:00 AM today from office
- System monitored with DLP and endpoint protection
- Asset owner: HR Department, criticality: High (PII data)

### Step 3: Understand the Alert Details
- Data type: Employee records, salary information (2GB total)
- Destination: External USB drive (not company-issued)
- Transfer method: Direct file copy to removable media
- Files affected: 500+ HR documents
- No encryption or unusual protocols used

### Step 4: Check for False Positive Indicators
- Not known legitimate activity; large data transfers to USB are restricted
- No admin changes or maintenance noted
- User behavior: Lisa denies performing the transfer
- USB device not approved or whitelisted
- Activity not authorized for HR data handling

### Step 5: Validate Against Business Context
- Business activity: End of quarter, but no mass data exports planned
- User should not be transferring bulk HR data to external devices
- Timing is after hours for some regions, but suspicious
- Does not align with normal HR operations (data stays on secure servers)
- Asset location: Office network, but external device introduced

### Step 6: Document Triage Assessment
- Checked user interviews, system logs, data access records
- Found: Unauthorized data transfer, potential insider threat
- Classification: **Suspicious** - Needs further investigation
- Confidence level: Medium (60%)
- Next action: Interview user, review access logs

### Step 7: Make Triage Decision
- Escalation needed: High severity, potential data breach
- Priority: High
- Assigned to: Data Protection Team

---

## Example 5: Privileged Account Activity

### Scenario
Identity management system alerts on unusual activity from a domain administrator account.

### Step 1: Receive and Initial Assessment
- Alert received from IAM tool at 1:15 AM
- Alert title: "Privileged Account Anomalous Behavior"
- Description: Domain admin account accessing multiple systems simultaneously
- No duplicates in last month
- Rare alert type, usually indicates compromise

### Step 2: Gather Contextual Information
- Affected account: domain.admin@company.com (Domain Administrator)
- Systems accessed: 15 different servers across network
- Account owner: IT Operations team (shared account)
- Last use: 6:00 PM yesterday by authorized admin
- Account is highly privileged, monitored closely
- Asset criticality: Critical (domain control)

### Step 3: Understand the Alert Details
- Activity: Simultaneous logins to multiple servers
- Source IPs: Various internal IPs, but unusual pattern
- Actions: User enumeration, file access, configuration changes
- Duration: 45-minute session
- No MFA bypass detected

### Step 4: Check for False Positive Indicators
- Not known legitimate activity; admins don't work off-hours without approval
- No scheduled maintenance or approved changes
- Account behavior: Unusual for off-hours bulk access
- Activity not whitelisted for this time
- Not authorized software or emergency access

### Step 5: Validate Against Business Context
- Business activity: Off-hours, no emergency maintenance planned
- Account should not be used without change management approval
- Timing is highly suspicious (1 AM)
- Does not align with normal admin behavior (individual system access)
- Asset location: Internal network, but pattern indicates compromise

### Step 6: Document Triage Assessment
- Checked access logs, change management records, user notifications
- Found: Unauthorized off-hours access, lateral movement pattern
- Classification: **True Positive** - Privileged account compromise
- Confidence level: High (85%)
- Next action: Immediate account lockdown, incident declaration

### Step 7: Make Triage Decision
- Escalation needed: Critical severity, domain compromise risk
- Priority: Critical
- Assigned to: Incident Response Team

---

These examples demonstrate how the triage validation process applies to different types of security alerts in real-world scenarios. Each example shows the systematic approach to gathering information, eliminating false positives, and making informed decisions about alert handling.