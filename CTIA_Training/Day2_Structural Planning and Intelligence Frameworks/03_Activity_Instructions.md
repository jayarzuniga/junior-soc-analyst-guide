# Step-by-Step Student Instructions

## Step 1

Read the **SILENTBANKER** case study in its entirety. Do not skip any line.

Highlight or note any action that involves:

- a tool
- a command
- a network connection
- a file operation

## Step 2

Open the **MITRE ATT&CK Matrix Template** from File 2 above.

Create a new document and copy the entire table exactly.

## Step 3: Complete the MITRE ATT&CK Matrix Row by Row

- For each **Tactic** in the left column, scan the case study for evidence.
- Find the matching **Technique** from File 3, the Technique Reference List.
- Write the **Technique ID** such as `T1566.001` and the **Technique Name** exactly as shown.
- Under **Specific Evidence**, copy the **exact sentence or phrase** from the case study.

**Critical Rule:** If you cannot find evidence for a tactic, leave that row blank. Do not invent evidence.

**Minimum requirement:** Fill at least **12 of the 14 tactics**. You will find evidence for most of them.

## Step 3.1: Specific Guidance for Each Tactic

| Tactic | Where to Look in Case Study |
| --- | --- |
| Reconnaissance | Look for any probe before the email. This may be missing, so leave blank if none is present. |
| Resource Development | Look for domain registration or infrastructure setup. This may be missing. |
| Initial Access | April 1, 09:15 - the email with attachment |
| Execution | April 1, 09:23 and 09:25 - PowerShell and scheduled task |
| Persistence | April 1, 09:23 - scheduled task |
| Privilege Escalation | Look for privilege increase. This may be implicit in the domain admin query. |
| Defense Evasion | April 1, 09:26 and April 12, 02:30 - disabling Defender and clearing history |
| Credential Access | April 2, 02:22 - Mimikatz download and use |
| Discovery | April 2, 02:15 and April 11, 04:30 - domain group query and file scanning |
| Lateral Movement | April 2, 02:35 - authentication to FS01 |
| Collection | April 12, 01:15 - compressing files |
| Command and Control | April 11, 03:00 - HTTPS beacon |
| Exfiltration | April 12, 02:00 - HTTPS `POST` of `data.zip` |
| Impact | April 12, 02:30 - `del /f` command for partial data destruction |

## Step 4

Open the **Diamond Model Diagram Template** from File 4.

Create a new document and reproduce the diagram structure.

## Step 5: Complete Each Corner of the Diamond Model

### Adversary Corner

- Based on the case study, write what you can infer about the adversary:
  `Unknown actor, likely financially motivated, targeting banking sector`
- Write an alias if one exists.
  No alias is given, so write:
  `Unidentified, track as SILENTBANKER-operator`

### Capability Corner

- Malware name: `SILENTBANKER`
- Technique: `Multi-stage malware with credential theft and exfiltration`
- File hash: `a1b2c3d4e5f6789012345678901234ab`

### Infrastructure Corner

- IP: `185.143.223.115`
- Domain: `rbmsupport.com`
- Port/protocol: `HTTPS (443)`, `HTTP (80 for initial download)`

### Victim Corner

- Organization: `Regional Bank of Midlands (RBM)`
- Sector: `Financial Services`
- Targeted data: files containing `account`, `routing`, `SWIFT`

## Step 6: Complete the Diamond Model Meta-Features

- **Timestamp:** `2026-04-01` to `2026-04-15`
- **Phase:** `Actions on Objectives` (exfiltration phase)
- **Result:** `2.4 GB of sensitive data exfiltrated`
- **Direction:** `Victim (RBM) to Adversary (185.143.223.115)` - data outbound

## Step 7: Complete the Kill Chain Mapping

Add this as a text list below your Diamond diagram.

Write each Kill Chain phase and the matching evidence:

| Kill Chain Phase | Evidence from Case Study |
| --- | --- |
| Reconnaissance | Not explicitly observed (assumed) |
| Weaponization | Creation of `SecurityPatch.exe` (not observed, assumed) |
| Delivery | Email with attachment on April 1, 09:15 |
| Exploitation | User double-clicking `.exe` on April 1, 09:22 |
| Installation | Writing to `svchost.exe` and creating scheduled task on April 1, 09:23 |
| Command and Control | HTTPS beacon to `185.143.223.115:443` starting April 11 |
| Actions on Objectives | Data discovery, collection, and exfiltration from April 11 to April 15 |

> Insert here

> Insert here

## Step 9: Final Review

Verify the following before submitting:

- MITRE matrix has a minimum of **12 filled tactics**
- Each filled tactic has **Technique ID**, **Technique Name**, and an **exact evidence quote**
- Diamond diagram has all **4 corners** filled
- Diamond meta-features have all **4 fields** filled
- Kill Chain mapping has all **7 phases**, even if some say `not observed`
- Cross-mapping table has at least **4 rows**
