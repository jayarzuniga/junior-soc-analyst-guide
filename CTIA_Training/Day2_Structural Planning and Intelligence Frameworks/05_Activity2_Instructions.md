# Step-by-Step Student Instructions

## Step 1

Read the **SHADOWBYTE** case study in its entirety.

Note that this is a **healthcare ransomware attack**. It involves a different sector and different adversary behavior than the SILENTBANKER case.

## Step 2

Open the **MITRE ATT&CK Matrix Template** from File 2.

Create a new document and copy the entire table exactly.

## Step 3: Complete the MITRE ATT&CK Matrix Row by Row

### Specific Guidance for the SHADOWBYTE Case Study

| Tactic | Where to Look in Case Study |
| --- | --- |
| Reconnaissance | Look for any probe before the email. This may be missing, so leave blank. |
| Resource Development | Domain registration on `2026-04-05` and Russian VPS hosting |
| Initial Access | April 10, 08:45 - email with `.zip` attachment |
| Execution | April 10, 08:53 - `.js` file and flashing PowerShell window |
| Persistence | April 10, 08:56 - `AdobeUpdateTask` scheduled task |
| Privilege Escalation | April 10, 09:00 - `net user` commands creating `temp_admin` account |
| Defense Evasion | April 10, 08:55 for Defender disablement, and April 13, 01:45 for `vssadmin delete shadows` |
| Credential Access | April 10, 09:15 for BloodHound enumeration, and April 13 for impacket usage |
| Discovery | April 10, 09:15 - `SharpHound.exe` domain mapping |
| Lateral Movement | April 13, 01:30 - impacket moving to `FS02` |
| Collection | April 13, 02:00 - AES-256 encryption of files |
| Command and Control | April 13, 03:00 - HTTPS `POST` to `5.188.86.45` |
| Exfiltration | April 13, 03:00 - `15 GB` of patient data exfiltrated |
| Impact | Encryption with `.shadowbyte`, ransom note deployment, and `vssadmin` deletion |

**Minimum technique count:** Fill at least **12 tactics**. You will find evidence for most of them.

## Step 4

Open the **Diamond Model Diagram Template** from File 4.

Create a new document and reproduce the diagram structure.

## Step 5: Complete Each Corner of the Diamond Model

### Adversary Corner

- Actor: `Unknown ransomware operator`
- Affiliation: `Likely affiliated with the Ryuk/Ragnar Locker family`
- Motivation: `Financial`, based on the `75 Bitcoin` or about `$2.5M USD` ransom demand

### Capability Corner

- Malware family: `ShadowByte` (new variant)
- Techniques: `JavaScript download cradle`, `PowerShell`, `BloodHound`, `impacket`, `AES-256 encryption`
- Hash: SHA256 of the `.js` file  
  `4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b`

### Infrastructure Corner

- Domain: `jobs-portal.net` (registered `2026-04-05`, via NameCheap)
- IP: `5.188.86.45` (Russia)
- Bitcoin wallet: `1A2b3C4d5E6f7G8h9I0j`

### Victim Corner

- Organization: `Pacifica General Hospital (PGH)`
- Sector: `Healthcare`
- Data impacted: `Patient records`, `medical imaging (.dcm)`, `databases`, and `15 GB` exfiltrated

## Step 6: Complete the Diamond Model Meta-Features

- **Timestamp:** `2026-04-10` to `2026-04-18`
- **Phase:** `Impact / Encryption` (final phase)
- **Result:** `40+ workstations encrypted`, `8 GB data exfiltrated`, `no ransom paid`, `recovery from backups`
- **Direction:** `Victim (PGH) to Adversary (5.188.86.45)` for exfiltration, and `Adversary to Victim` for encryption and local destruction

## Step 7: Complete the Kill Chain Mapping

| Kill Chain Phase | Evidence from Case Study |
| --- | --- |
| Reconnaissance | Not explicitly observed (assumed) |
| Weaponization | Creation of `John_Vasquez_Resume.zip` and `.js` file (not observed, assumed) |
| Delivery | Email with resume attachment on April 10, 08:45 |
| Exploitation | User double-clicking the `.js` file on April 10, 08:53 |
| Installation | `svhost.exe` written and `AdobeUpdateTask` scheduled task created |
| Command and Control | HTTPS `POST` to `5.188.86.45` for exfiltration and payload retrieval |
| Actions on Objectives | Encryption of files, ransom note deployment, and data exfiltration |

## Step 8: Complete the Framework Cross-Mapping Table

Minimum required: **5 rows**

| Diamond Element | MITRE Tactic | Kill Chain Phase | Specific Evidence |
| --- | --- | --- | --- |
| Capability: JavaScript execution | Execution (`T1059.005`) | Exploitation | `User double-clicks the .js file` |
| Capability: PowerShell download | Execution (`T1059.001`) | Installation | `JavaScript executes PowerShell to download from http://5.188.86.45/update.ps1` |
| Infrastructure: `5.188.86.45` | Command and Control (`T1071.001`) | Command and Control | `exfiltrates 15 GB of patient data to 5.188.86.45 via HTTPS POST` |
| Victim: Pacifica General Hospital | Impact (`T1486`) | Actions on Objectives | `AES-256 encryption. Appends extension .shadowbyte` |
| Capability: `vssadmin` | Defense Evasion (`T1490`) | Actions on Objectives | `vssadmin delete shadows /all /quiet - deletes all volume shadow copies` |

## Step 9: Final Review

Verify the following:

- MITRE matrix has a minimum of **12 filled tactics**
- Each filled tactic has **Technique ID**, **Technique Name**, and an **exact evidence quote**
- Diamond diagram has all **4 corners** filled
- Diamond meta-features have all **4 fields** filled
- Kill Chain mapping has all **7 phases**, even if some say `not observed`
- Cross-mapping table has at least **5 rows**
