# OSINT (Open Source Intelligence) & Indicator Management

## OSINT Definition

### Open Source Intelligence (OSINT)

Intelligence derived from publicly available sources that any person can legally access without credentials or special permissions.

## Five Categories of OSINT Feeds You Will Use Today

### OSINT Feed Types

| Feed Type | Description | Example Source |
| --- | --- | --- |
| Threat Intelligence Feeds | Published lists of known malicious IPs, domains, hashes, and other IoCs. | abuse.ch, Feodo Tracker |
| Security Blogs | Written analysis, research, and reports with embedded IoCs and contextual insights. | Krebs on Security, Unit 42 |
| Social Media | Platforms where security researchers and organizations share real-time threat information. | @VK_Intel, @DrWeb (Twitter/X) |
| Public Sandbox Reports | Automated malware analysis outputs, including behavior, network traffic, and extracted IoCs. | Any.Run, Triage, Joe Sandbox |
| RSS/ATOM Feeds | Syndicated content aggregating updates from multiple blogs, feeds, and sources. | Blog aggregators, RSS readers |

## Indicator of Compromise (IoC)

### Definition

A piece of forensic data that identifies potentially malicious activity.

### Common IoC Types

- IP addresses (IPv4/IPv6): `185.143.223.115`
- Domains: `malicious-site.com`
- URLs: `http://bad.com/payload.exe`
- File hashes (MD5, SHA1, SHA256): `a1b2c3d4e5f6789012345678901234ab`
- Email addresses/domains: `phisher@fake-domain.net`

### Note

IoCs are used to detect, block, or investigate malicious activity within networks and systems.

## Relevance Filtering

### Definition

The process of removing IoCs that do not match your intelligence requirements, ensuring only actionable and relevant data is retained.

### Common Filtering Criteria

| Filter Type | Description | Example |
| --- | --- | --- |
| Geographic | Exclude IoCs from countries outside your threat model. | Ignore IPs from Russia if your focus is on APAC threats. |
| Sector | Exclude IoCs targeting unrelated industries. | Ignore healthcare malware if your sector is finance. |
| Date | Exclude outdated IoCs based on recency requirements. | Ignore IoCs older than 30 days. |
| Type | Exclude IoC types not relevant to your current needs. | Ignore file hashes if your focus is on network-level IPs and domains. |

### Purpose

- Reduces noise and false positives.
- Focuses resources on relevant threats.
- Improves efficiency of detection and response efforts.
