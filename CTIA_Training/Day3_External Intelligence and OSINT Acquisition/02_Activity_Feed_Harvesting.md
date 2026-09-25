# Activity Overview

## Deliverable

- A fully configured "harvester" script that pulls from 5 simulated feeds (provided as text files below).
- A filtered output CSV file containing only relevant IoCs.
- A relevance audit log justifying each filtered item.

## Skills Practiced

OSINT feed harvesting, automated data extraction, IoC filtering, relevance assessment.

## Infographic Placeholder

> Insert infographic here: a three-step pipeline showing how raw threat intelligence feeds are converted into actionable indicators.

---

## File 1: Simulated OSINT Feed #1 - abuse.ch URLhaus Feed

Copy this entire block. This simulates a real API response.

```text
# FEED: abuse.ch URLhaus
# SOURCE URL: https://urlhaus.abuse.ch/downloads/csv/
# FORMAT: CSV (first line is headers)
# TIMESTAMP: 2026-04-23 08:00:00 UTC

id,dateadded,url,url_status,threat,tags
1,2026-04-23 07:15:00,http://185.143.223.115/payload.exe,online,malware_download,SilentBanker
2,2026-04-23 06:30:00,https://update-windows-defender.com/setup.exe,online,malware_download,RedLineStealer
3,2026-04-22 23:45:00,http://85.209.11.22/doc.scr,online,malware_download,Emotet
4,2026-04-22 18:20:00,https://paypal-verification-secure.com/verify,online,phishing,PayPalPhish
5,2026-04-22 12:00:00,http://45.155.205.33/office365-login.html,online,phishing,Office365
6,2026-04-21 09:30:00,https://zoom-us-download.com/ZoomInstaller.exe,offline,malware_download,FakeZoom
7,2026-04-20 22:15:00,http://193.42.33.88/banking.scr,online,malware_download,BankerTrojan
8,2026-04-20 14:00:00,https://docusign-secure-docs.com/invoice.pdf.exe,online,malware_download,DocuSignPhish
```

## File 2: Simulated OSINT Feed #2 - Security Blog (Krebs-like)

Simulates a blog post with embedded IoCs.

```text
# FEED: Security Blog - "The Security Ledger"
# SOURCE URL: https://securityledger.example.com/2026/04/silentbanker-analysis/
# ARTICLE TITLE: "SilentBanker Malware Returns with New Infrastructure"
# PUBLISHED: 2026-04-22

In a new wave of attacks targeting financial institutions, researchers have observed the
SilentBanker malware family using updated command and control infrastructure.

The following indicators have been confirmed:

DOMAINS:
- banking-update-service[.]com (registered 2026-04-15)
- swift-message-check[.]net (registered 2026-04-18)
- rbm-portal[.]org (typosquat of victim domain)

IP ADDRESSES:
- 185.143.223.115 (Belarus, bulletproof hoster)
- 45.155.205.88 (Netherlands, known abuse contact)
- 91.243.45.12 (Russia, previously hosting Cobalt Strike)

FILE HASHES (SHA256):
- 3f5c9e2a1b4d8f7e6c3a9b2d4f1e8c7a6b5d4f3e2c1a9b8c7d6e5f4a3b2c1d0 (SilentBanker loader)
- 7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8 (credential stealer module)

MITRE TAGS: T1566.001, T1059.001, T1071.001
```

## File 3: Simulated OSINT Feed #3 - Social Media (Twitter/X)

Simulates researcher posts.

```text
# FEED: Twitter/X Security Researcher Posts
# SOURCE URL: https://twitter.com/search?q=silentbanker%20ioc
# DATE RANGE: 2026-04-20 to 2026-04-23

@MalwareHunter_99 (2026-04-23 02:30 UTC):
"Just saw SilentBanker using new IP: 185.143.223.116. Same pattern as previous. Block it."
[LINKED IOCS: IP 185.143.223.116]

@ThreatIntelBot (2026-04-22 19:45 UTC):
"SilentBanker C2 domains observed in past 24h:
- customer-support-portal[.]xyz
- secure-message-alert[.]info
Both resolve to 185.143.223.115"
[LINKED IOCS: domains, IP]

@DFIR_Research (2026-04-22 12:00 UTC):
"Interesting finding: SilentBanker now using Discord CDN for staging. Hash:
a1b2c3d4e5f6789012345678901234ab (MD5) - matches old sample but new delivery."
[LINKED IOCS: MD5 hash]

@SecurityBleep (2026-04-21 08:15 UTC):
"Fake update campaign delivering SilentBanker. Domains:
- microsoft-security-upgrade[.]com
- adobe-flash-update-required[.]net"
[LINKED IOCS: domains]
```

## File 4: Simulated OSINT Feed #4 - Public Sandbox (Any.Run-like)

Simulates automated analysis report.

```text
# FEED: Malware Sandbox Report
# SOURCE URL: https://app.any.run/submissions/2026-04-23-silentbanker
# ANALYSIS ID: 8842a1b3-c4d5-4e6f-8a9b-0c1d2e3f4a5b
# STATUS: Completed
# MALWARE FAMILY: SilentBanker

=== NETWORK TRAFFIC ===
Destination IPs:
- 185.143.223.115:443 (HTTPS, C2 beacon, 142 packets)
- 8.8.8.8:53 (DNS query for banking-update-service.com)
- 185.143.223.116:443 (HTTPS, backup C2, 12 packets)
- 45.155.205.88:80 (HTTP GET /config.dat)

DNS Queries:
- banking-update-service.com -> A 185.143.223.115
- swift-message-check.net -> A 185.143.223.116
- ocsp.digicert.com -> A 93.184.220.29 (legitimate, false positive)

=== FILE SYSTEM ACTIVITY ===
Created Files:
- C:\Users\Public\svchost.exe (MD5: a1b2c3d4e5f6789012345678901234ab)
- C:\Windows\Temp\config.dat (SHA256: 3f5c9e2a1b4d8f7e6c3a9b2d4f1e8c7a6b5d4f3e2c1a9b8c7d6e5f4a3b2c1d0)

=== REGISTRY MODIFICATIONS ===
- HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\WindowsUpdate (persistence)

=== PROCESS TREE ===
- powershell.exe (PID 4421) -> Invoke-WebRequest to 185.143.223.115
- cmd.exe (PID 4489) -> net group "Domain Admins" /domain

=== YARA RULES MATCHED ===
- rule SilentBanker_Loader (score: 95)
- rule Banker_CredStealer (score: 88)
```

## File 5: Simulated OSINT Feed #5 - RSS Aggregator

Simulates multiple small feeds combined.

```text
# FEED: RSS Security Aggregator
# SOURCE URL: https://security-rss.example.com/combined
# LAST FETCH: 2026-04-23 09:00:00 UTC

=== ITEM 1 (from ThreatPost RSS) ===
Title: "New Banking Trojan Uses COVID-19 Lures"
Date: 2026-04-22
IoC mentions: corona-vaccine-update[.]com, 193.42.33.90

=== ITEM 2 (from Unit 42 Blog RSS) ===
Title: "SilentBanker: What's New in Q2 2026"
Date: 2026-04-21
IoC mentions:
- Domains: rbm-updates[.]com, secure-banking-portal[.]eu
- IPs: 185.143.223.117, 185.143.223.118
- Hashes: 9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e

=== ITEM 3 (from SANS ISC Diary) ===
Title: "Diary: SilentBanker Infections Increasing"
Date: 2026-04-20
IoC mentions:
- URL: http://185.143.223.115/update.bin
- Domain: windows-defender-alert[.]com
- Note: "False positive potential for microsoft.com subdomains"

=== ITEM 4 (from CISA Alerts RSS) ===
Title: "AA26-113A: SilentBanker Malware"
Date: 2026-04-19
IoC mentions:
- IPs: 185.143.223.115, 91.243.45.50, 45.155.205.100
- Domains: bank-verification[.]org, swift-update[.]net
- Hashes: 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
```

## File 6: Relevance Filtering Rules

These are your intelligence requirements for today.

```text
INTELLIGENCE REQUIREMENTS (Filtering Rules)
Target Sector: Financial Services / Banking
Geographic Focus: Global, but prioritize IoCs associated with Eastern Europe (Russia, Belarus, Ukraine)
Time Window: Only IoCs first observed in the last 7 days (from 2026-04-16 to 2026-04-23)
IoC Types Required: IP addresses and domains ONLY (exclude file hashes for this harvest)
Threat Family: SilentBanker (primary), any banking trojan (secondary)
Exclude: Phishing IoCs (unless banking-related), false positives, legitimate domains
```

## File 7: Harvester Script (Python)

Copy this entire script. You will run this manually (no actual Python execution needed - you will simulate the output by hand).

```python
# HARVESTER SCRIPT - OSINT Feed Aggregator
# This script simulates pulling and filtering IoCs from 5 OSINT feeds.
# For this activity, you will manually execute the logic described below.

import re
import csv
from datetime import datetime, timedelta

# Configuration
CUTOFF_DATE = datetime(2026, 4, 16)  # Only IoCs from last 7 days
REQUIRED_IOC_TYPES = ['ip', 'domain']  # Exclude hashes
TARGET_FAMILIES = ['SilentBanker', 'BankerTrojan', 'banking']

# Function to extract IP addresses from text
def extract_ips(text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ip_pattern, text)

# Function to extract domains from text (simplified)
def extract_domains(text):
    domain_pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}\b'
    return re.findall(domain_pattern, text)

# Function to check relevance based on family keywords
def is_relevant(family_text):
    for keyword in TARGET_FAMILIES:
        if keyword.lower() in family_text.lower():
            return True
    return False

# Feed processing simulation
all_iocs = []

# FEED 1: abuse.ch CSV
feed1_data = """185.143.223.115,SilentBanker
85.209.11.22,Emotet
45.155.205.33,Office365
193.42.33.88,BankerTrojan"""

# FEED 2: Security Blog
feed2_data = """185.143.223.115,SilentBanker
45.155.205.88,SilentBanker
91.243.45.12,SilentBanker
banking-update-service.com,SilentBanker
swift-message-check.net,SilentBanker
rbm-portal.org,SilentBanker"""

# FEED 3: Social Media
feed3_data = """185.143.223.116,SilentBanker
customer-support-portal.xyz,SilentBanker
secure-message-alert.info,SilentBanker
microsoft-security-upgrade.com,SilentBanker
adobe-flash-update-required.net,SilentBanker"""

# FEED 4: Sandbox Report
feed4_data = """185.143.223.115,SilentBanker
185.143.223.116,SilentBanker
45.155.205.88,SilentBanker
banking-update-service.com,SilentBanker
swift-message-check.net,SilentBanker"""

# FEED 5: RSS Aggregator
feed5_data = """corona-vaccine-update.com,Phishing
193.42.33.90,Generic
rbm-updates.com,SilentBanker
secure-banking-portal.eu,SilentBanker
185.143.223.117,SilentBanker
185.143.223.118,SilentBanker
windows-defender-alert.com,FakeAlert
bank-verification.org,SilentBanker
swift-update.net,SilentBanker
91.243.45.50,SilentBanker
45.155.205.100,SilentBanker"""

# Process each feed and filter
# [STUDENT: You will manually perform these filtering steps below]
```

## File 8: Filtered Output CSV Template

Copy this table for your final deliverable.

### FILTERED IoCs - RELEVANT ONLY

Target: Financial Services / Banking  
Date Range: 2026-04-16 to 2026-04-23  
IoC Types: IP and Domain only

| IoC Value | Type | Source Feed | Threat Family | Date Observed | Keep/Exclude | Exclusion Reason (if excluded) |
| --- | --- | --- | --- | --- | --- | --- |
| [IP/Domain] | [IP/Domain] | [Feed name] | [Family] | [Date] | [Keep/Exclude] | [If exclude, why] |

### RELEVANT IoCs (KEPT) - Summary List

[Write each kept IoC on a new line]

### EXCLUDED IoCs (FILTERED OUT) - Summary List

[Write each excluded IoC with reason]
