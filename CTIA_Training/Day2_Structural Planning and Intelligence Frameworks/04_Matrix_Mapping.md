# Activity Overview

**Time Allocation:** 120 minutes

**Deliverable:**

- Completed MITRE ATT&CK Matrix with a minimum of 12 techniques
- Diamond Model diagram with all 4 core features and meta-features
- Framework cross-mapping table

**Skills Practiced:** Threat actor behavior mapping, framework integration, intrusion analysis

## File 1: Malware Case Study - SHADOWBYTE Ransomware Intrusion

## Case Study: SHADOWBYTE Ransomware Incident

| Field | Value |
| --- | --- |
| Incident ID | `IR-2026-089` |
| Date of Attack | `2026-04-10` to `2026-04-18` |
| Target | Pacifica General Hospital (PGH) - 450-bed facility |
| Sector | Healthcare |

### Attack Timeline

As reconstructed from logs and EDR:

| Date and Time | Event |
| --- | --- |
| 2026-04-10 08:45 | An HR administrator at PGH receives an email from `resume-submissions@jobs-portal.net` with subject `Application: Senior IT Analyst Position - John Vasquez`. Attachment: `John_Vasquez_Resume.zip` |
| 2026-04-10 08:52 | Administrator extracts the zip file. Inside is `John_Vasquez_Resume.js` (JavaScript file). Windows SmartScreen shows no warning. |
| 2026-04-10 08:53 | User double-clicks the `.js` file. A PowerShell window flashes briefly and disappears. No visible change occurs. |
| 2026-04-10 08:54 | The JavaScript executes PowerShell to download from `http://5.188.86.45/update.ps1`. Script writes file to `C:\Users\Public\svhost.exe` (note: misspelled `svchost`). |
| 2026-04-10 08:55 | Malware modifies registry key `HKLM\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection\DisableRealtimeMonitoring` to value `1` and disables Defender. |
| 2026-04-10 08:56 | Malware creates scheduled task named `AdobeUpdateTask` to run `svhost.exe` every 6 hours. |
| 2026-04-10 09:00 | Malware runs `net localgroup administrators /add temp_admin` and `net user temp_admin P@ssw0rd123! /add`, creating a new local admin account. |
| 2026-04-10 09:15 | Malware uses BloodHound, a legitimate AD exploration tool, to map domain structure: `SharpHound.exe -c All --domain pacifica.local` |
| 2026-04-10 to 2026-04-12 | No logs. Malware dormant during weekend. |
| 2026-04-13 01:30 | Malware uses impacket, a Python-based tool, to move laterally to file server `FS02` at `10.10.20.15` using stolen domain admin credentials. |
| 2026-04-13 01:45 | On `FS02`, malware runs `vssadmin delete shadows /all /quiet`, deleting all volume shadow copies and preventing recovery. |
| 2026-04-13 02:00 | Malware begins encrypting files with extensions `.dcm`, `.pdf`, `.xslx`, and `.mdb`. It uses AES-256 encryption and appends extension `.shadowbyte` to encrypted files. |
| 2026-04-13 02:30 | Malware drops ransom note `README_TO_DECRYPT.txt` in every folder: `We have encrypted your patient records and medical imaging data. Pay 75 Bitcoin (value ~$2.5M USD) to wallet address 1A2b3C4d5E6f7G8h9I0j to receive decryption key. You have 72 hours. Do not contact law enforcement.` |
| 2026-04-13 03:00 | Malware exfiltrates `15 GB` of unencrypted patient data, as extortion leverage, to `5.188.86.45` via HTTPS `POST` before encryption completes. |
| 2026-04-13 05:00 | Hospital staff arrive to find files inaccessible. Ransom note displayed on `FS02` and 40+ workstations. |
| 2026-04-13 06:30 | Hospital initiates incident response. FBI Cyber Task Force notified. |
| 2026-04-14 to 2026-04-18 | Recovery from backups takes 36 hours. About `8 GB` of data was exfiltrated before containment was confirmed. No ransom was paid. |

### Technical Indicators

- Domain: `jobs-portal.net` (registered `2026-04-05` via NameCheap)
- IP: `5.188.86.45` (hosted in Russia, known ransomware infrastructure)
- File hash: `John_Vasquez_Resume.js`  
  SHA256: `4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b`
- PowerShell download URL: `http://5.188.86.45/update.ps1`
- Encrypted file extension: `.shadowbyte`
- Bitcoin wallet: `1A2b3C4d5E6f7G8h9I0j`
- Ransomware family: `ShadowByte` (new variant of Ryuk/Ragnar Locker family)

## File 2: MITRE ATT&CK Matrix Template - SHADOWBYTE

## MITRE ATT&CK Matrix - SHADOWBYTE Ransomware

Fill in specific Technique ID and Description for each tactic observed.

| Tactic | Technique ID | Technique Name | Specific Evidence from Case Study |
| --- | --- | --- | --- |
| Reconnaissance | [ID] | [Name] | [Quote exact evidence] |
| Resource Development | [ID] | [Name] | [Quote exact evidence] |
| Initial Access | [ID] | [Name] | [Quote exact evidence] |
| Execution | [ID] | [Name] | [Quote exact evidence] |
| Persistence | [ID] | [Name] | [Quote exact evidence] |
| Privilege Escalation | [ID] | [Name] | [Quote exact evidence] |
| Defense Evasion | [ID] | [Name] | [Quote exact evidence] |
| Credential Access | [ID] | [Name] | [Quote exact evidence] |
| Discovery | [ID] | [Name] | [Quote exact evidence] |
| Lateral Movement | [ID] | [Name] | [Quote exact evidence] |
| Collection | [ID] | [Name] | [Quote exact evidence] |
| Command and Control | [ID] | [Name] | [Quote exact evidence] |
| Exfiltration | [ID] | [Name] | [Quote exact evidence] |
| Impact | [ID] | [Name] | [Quote exact evidence] |

**Note:** Not all tactics may be present. Leave blank if no evidence exists.  
**Minimum required:** 12 techniques across all tactics.

## File 3: Technique Reference List

Use this list to match evidence to Technique IDs.

### MITRE ATT&CK v14 - Focus on Ransomware TTPs

| Tactic | Technique ID | Technique Name | Description Match |
| --- | --- | --- | --- |
| Initial Access | T1566.001 | Phishing: Spearphishing Attachment | Email with malicious attachment (`.zip` containing `.js`) |
| Execution | T1059.005 | Command and Scripting Interpreter: Visual Basic/JScript | JavaScript (`.js`) file execution |
| Execution | T1059.001 | Command and Scripting Interpreter: PowerShell | PowerShell command execution |
| Persistence | T1053.005 | Scheduled Task/Job: Scheduled Task | `AdobeUpdateTask` scheduled task |
| Privilege Escalation | T1136.001 | Create Account: Local Account | `net user` command creating `temp_admin` |
| Defense Evasion | T1562.001 | Impair Defenses: Disable or Modify Tools | Disabling Windows Defender via registry |
| Defense Evasion | T1490 | Inhibit System Recovery | `vssadmin delete shadows` prevents recovery |
| Credential Access | T1552.001 | Unsecured Credentials: Credentials in Files | BloodHound and impacket for credential theft |
| Discovery | T1087.002 | Account Discovery: Domain Account | BloodHound enumeration of domain |
| Discovery | T1482 | Domain Trust Discovery | `SharpHound.exe` mapping domain structure |
| Lateral Movement | T1021.002 | Remote Services: SMB/Windows Admin Shares | impacket tool for lateral movement |
| Collection | T1005 | Data from Local System | Encryption of local files |
| Command and Control | T1071.001 | Application Layer Protocol: Web Protocols | HTTPS `POST` to `5.188.86.45` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | HTTPS `POST` of patient data before encryption |
| Impact | T1486 | Data Encrypted for Impact | AES-256 encryption and `.shadowbyte` extension |
| Impact | T1485 | Data Destruction | `vssadmin delete shadows` prevents system recovery |
| Impact | T1491 | Defacement: Internal Defacement | Ransom note `README_TO_DECRYPT.txt` in every folder |
| Resource Development | T1583.001 | Acquire Infrastructure: Domains | `jobs-portal.net` registered `2026-04-05` |
| Resource Development | T1583.003 | Acquire Infrastructure: Virtual Private Server | `5.188.86.45` hosted in Russia |

## File 4: Diamond Model Diagram Template - SHADOWBYTE

## Diamond Model - SHADOWBYTE Ransomware Incident

```text
                       +---------------------------------+
                       |            ADVERSARY            |
                       |                                 |
                       | [Who is the actor?]            |
                       | [What is the group name?]      |
                       | [What is motivation?]          |
                       +---------------+-----------------+
                                       |
          +----------------------------+----------------------------+
          |                                                         |
          v                                                         v
+-------------------------+                           +-------------------------+
|       CAPABILITY        |                           |     INFRASTRUCTURE      |
|                         |<------------------------->|                         |
| [What malware family?]  |                           | [What IP/domain?]       |
| [What techniques?]      |                           | [What hosting country?] |
| [What file hashes?]     |                           | [What wallet address?]  |
+------------+------------+                           +------------+------------+
             |                                                     |
             |                                                     |
             +------------------------+  +-------------------------+
                                      |  |
                                      v  v
                           +-------------------------+
                           |         VICTIM          |
                           |                         |
                           | [What organization?]    |
                           | [What sector?]          |
                           | [What data was stolen?] |
                           +-------------------------+
```

### Meta-Features

- **Timestamp (When):** [Start date] to [End date]
- **Phase (Stage of attack):** [Kill Chain phase at peak]
- **Result (What happened):** [Outcome - encryption, ransom, data theft]
- **Direction (Data flow):** [From victim to adversary / adversary to victim]

### Kill Chain Mapping

Add to the Diamond Model:

`Reconnaissance -> Weaponization -> Delivery -> Exploitation -> Installation -> C2 -> Actions`

Map each phase to specific evidence from the case study.

## File 5: Framework Cross-Mapping Table Template

## Framework Cross-Mapping Table - SHADOWBYTE

| Diamond Element | MITRE Tactic | Kill Chain Phase | Specific Evidence |
| --- | --- | --- | --- |
| [Element 1] | [Tactic] | [Phase] | [Evidence quote] |
| [Element 2] | [Tactic] | [Phase] | [Evidence quote] |
| [Element 3] | [Tactic] | [Phase] | [Evidence quote] |
| [Element 4] | [Tactic] | [Phase] | [Evidence quote] |
| [Element 5] | [Tactic] | [Phase] | [Evidence quote] |

**Minimum required:** 5 rows.
