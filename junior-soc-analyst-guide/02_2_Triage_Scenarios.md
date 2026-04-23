# Triage Scenarios

This document contains real-world triage scenarios for junior SOC analysts to practice. Each scenario describes an alert or incident that requires triage. The answers and analysis for these scenarios are provided in `02_3_Triage_Scenario_Analysis.md`.

## Scenario 1: Multiple Failed Login Attempts
An alert is triggered for multiple failed login attempts (over 10) from a single IP address to a corporate VPN portal within a 5-minute window.

## Scenario 2: Unusual Outbound Traffic
SIEM detects unusual outbound traffic from an internal server to a known malicious domain listed in threat intelligence feeds.

## Scenario 3: High CPU Usage Alert
A monitoring alert shows high CPU usage (over 90%) on a critical application server during off-hours, with no scheduled maintenance or backups running.

## Scenario 4: Anomalous File Creation
Endpoint detection alerts on the creation of multiple executable files in the Windows System32 directory by a user account that typically doesn't perform administrative tasks.

## Scenario 5: Suspicious Process with Elevated Privileges
A process named "svchost.exe" is running with elevated privileges and is communicating with an external IP address not associated with any known business applications.

## Scenario 6: Phishing Email with Malicious Attachment
An email is received from an external sender with a subject line "Invoice Update" containing an attachment named "invoice.pdf.exe" that is flagged by email security gateway.

## Scenario 7: VPN Connection from Unusual Location
A user logs into the VPN from an IP address geolocated to a country where the company has no operations, at a time when the user is known to be in the office.

## Scenario 8: Large Data Transfer to External Storage
Network logs show a large data transfer (several GB) from a user's workstation to an external cloud storage service that is not approved for corporate use.

## Scenario 9: Repeated Access to Sensitive Files
System logs indicate repeated access attempts to sensitive HR files by an employee who does not have authorization for those documents.

## Scenario 10: Malware Signature Match
An endpoint antivirus alert detects a malware signature match for a known ransomware variant on a user's laptop.

## Scenario 11: Unusual Network Scan
Internal network monitoring detects port scanning activity originating from a workstation that is not authorized for network scanning tools.

## Scenario 12: Account Lockout Storm
Multiple user accounts are being locked out simultaneously across different departments, triggered by failed login attempts from various IP addresses.

## Scenario 13: Unexpected Service Startup
A critical service on a server starts automatically without any scheduled task or manual intervention, and begins communicating with unknown external hosts.

## Scenario 14: Privilege Escalation Attempt
Logs show an attempt to escalate privileges using a known exploit against a vulnerable application running on a domain controller.

## Scenario 15: Data Exfiltration via Email
An alert flags an email sent to an external address containing a large attachment with sensitive company data, sent from an account that recently had its password changed.