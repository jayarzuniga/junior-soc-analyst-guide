# Step-by-Step Student Instructions

## Step 1: Read the Relevance Filtering Rules (File 6)

Memorize these critical filters:

- Date: Only IoCs from `2026-04-21` to `2026-04-28` (last 7 days).
- Type: IP addresses, Domains, URLs, File Hashes (SHA256), and Bitcoin wallets.
- Family: MedLock or healthcare-targeting ransomware (NOT generic phishing).

## Step 2: Read File 1 (AlienVault OTX Feed)

Extract every IP, domain, URL, and hash. Write them in a list. Then apply filters:

- Check date: All entries have created timestamps. Are they within the last 7 days? (Today is `2026-04-28`.)
- Check type: Extract IPs, domains, URLs, hashes.
- Check family: Look at `tags` column. Keep only entries with `MedLock` or `Healthcare`.
- Check TLP: `TLP:amber` and `TLP:green` are acceptable; `TLP:red` would be excluded.

## Step 3: Read File 2 (Security Blog - CyberHealth News)

Extract every IP, domain, hash, and email. Apply filters:

- Date: Article published `2026-04-28` -> WITHIN 7 days (KEEP by date).
- Type: Domains, IPs, hashes, emails (emails are valid IoCs).
- Family: Explicitly MedLock ransomware -> KEEP.

## Step 4: Read File 3 (Social Media / Twitter)

Extract every IP, domain, hash, Bitcoin wallet, and filename. Apply filters:

- Date: Posts from `2026-04-25` to `2026-04-28` -> all WITHIN 7 days.
- Type: Extract IPs, domains, hashes, Bitcoin wallets, filenames.
- Family: All posts mention MedLock or healthcare -> KEEP (with appropriate confidence).

## Step 5: Read File 4 (Public Sandbox - Triage)

Extract every IP, domain, hash, and filename. Apply filters:

- Date: Report dated `2026-04-28` -> WITHIN 7 days.
- Type: IPs, domains, hashes, filenames.
- Family: MedLock confirmed -> KEEP.

Special note:

- `ocsp.digicert.com` and `update.microsoft.com` are marked as false positives -> EXCLUDE.

## Step 6: Read File 5 (RSS Aggregator)

Extract every IP, domain, hash, and Bitcoin wallet from all 4 RSS items. Apply filters carefully:

| RSS Item | Date | IoCs | Family | Decision |
| --- | --- | --- | --- | --- |
| Item 1 (The DFIR Report) | 2026-04-27 | `medlock-c2.biz`, `healthcare-update-portal.org`, `patient-billing-notice.com`, `5.188.88.99`, `5.188.88.100`, `185.165.29.45`, SHA256 hash | MedLock | KEEP all |
| Item 2 (CISA Alerts) | 2026-04-26 | `5.188.88.99`, `185.165.29.50` (NEW), `med-portal-security.com`, `hospital-billing-update.org`, Bitcoin wallet (`3J98t1WpE...`) | MedLock | KEEP all |
| Item 3 (SANS ISC) | 2026-04-25 | `hr-services-portal.net`, `employee-verification-system.com`, `5.188.88.99` | MedLock | KEEP; note `teams.microsoft.com` false positive |
| Item 4 (SecurityWeek) | 2026-04-24 | `3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy` (BTC), `1A2b3C4d5E6f7G8h9I0jK1l2M3n4O5p` (BTC), `medlock-backup-c2.net`, `healthcare-data-encrypted.org` | MedLock | KEEP all |

## Step 7: Open the Filtered Output CSV Template (File 8)

Create a new document and copy the entire table.

## Step 8: Fill One Row Per IoC

For each IoC you identified, fill one row in the table.

Example of a correctly filled row:

| IoC Value | Type | Source Feed | Threat Family | Date Observed | Keep/Exclude | Exclusion Reason |
| --- | --- | --- | --- | --- | --- | --- |
| 5.188.88.99 | IP | AlienVault OTX | MedLock | 2026-04-28 | Keep | N/A |

## Step 9: Create the "RELEVANT IoCs (KEPT) - Summary List"

Expected kept IoCs by type:

```text
RELEVANT IoCs (KEPT) - MEDLOCK RANSOMWARE:

IP ADDRESSES:
5.188.88.99
5.188.88.100
185.165.29.45
185.165.29.50

DOMAINS:
medlock-c2.biz
healthcare-update-portal.org
patient-portal-verify.net
hr-services-portal.net
employee-verification-system.com
med-portal-security.com
hospital-billing-update.org
patient-billing-notice.com
health-portal-update.com
payroll-verification.com
benefits-election.org
medlock-backup-c2.net
healthcare-data-encrypted.org

URLS:
http://5.188.88.99/medlock_loader.bin

FILE HASHES (SHA256):
8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6 (MedLock loader)
1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a (MedLock encryptor)

BITCOIN WALLETS:
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
1A2b3C4d5E6f7G8h9I0jK1l2M3n4O5p

FILENAMES:
HOW_TO_RECOVER_FILES.txt
medlock.exe
medlock_loader.bin
```

## Step 10: Create the "EXCLUDED IoCs (FILTERED OUT) - Summary List"

Add excluded IoCs with reasons:

```text
EXCLUDED IoCs (FILTERED OUT):

ocsp.digicert.com - Reason: Legitimate certificate validation domain (false positive)
update.microsoft.com - Reason: Legitimate Microsoft update domain (false positive)
teams.microsoft.com - Reason: Legitimate Microsoft Teams domain (false positive)
[Any generic phishing domains without healthcare connection] - Reason: Not healthcare-specific
[Any IoCs with dates before 2026-04-21] - Reason: Outside 7-day window
pulse_004 (Ryuk Variant Detection) - Reason: Ryuk family, not MedLock (unless tagged with healthcare)
```

## Step 11: Verify Your Counts

- Total IoCs extracted from all 5 feeds: Approximately `40-50`
- Kept IoCs: Approximately `25-35`
- Excluded IoCs: Approximately `10-15`

## Step 12: Final Review

Verify the following:

- You processed ALL 5 feeds (none skipped).
- You extracted IPs, domains, URLs, hashes, Bitcoin wallets, and filenames.
- You applied the date filter (only `2026-04-21` to `2026-04-28`).
- You applied the family filter (MedLock/healthcare ransomware only).
- You identified and excluded false positives (`ocsp.digicert.com`, `update.microsoft.com`).
- Your CSV has a row for EVERY IoC (both kept AND excluded).
- Every excluded IoC has an exclusion reason.
