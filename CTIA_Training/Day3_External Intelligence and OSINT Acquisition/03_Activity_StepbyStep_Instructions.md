# Step-by-Step Student Instructions

## Step 1: Read the Relevance Filtering Rules (File 6)

Memorize these three critical filters:

- Date: Only IoCs from `2026-04-16` to `2026-04-23` (last 7 days).
- Type: IP addresses and domains ONLY (NO file hashes).
- Family: SilentBanker or banking-related threats (NOT generic phishing or fake alerts).

## Step 2: Read File 1 (abuse.ch Feed)

Extract every IP address and domain. Write them in a list. Then apply filters:

- Check date: All entries have dates. Are they within the last 7 days? (Today is `2026-04-23`.)
- Check type: IPs and domains only. All are URLs, but you extract the host, for example `185.143.223.115` from `http://185.143.223.115/payload.exe`.
- Check family: Look at the `threat` column. Keep only `SilentBanker` and `BankerTrojan`.

## Step 3: Read File 2 (Security Blog)

Extract every IP and domain from the article. Apply filters:

- Date: Article published `2026-04-22` -> WITHIN 7 days (KEEP by date).
- Type: Domains and IPs only (ignore the SHA256 hashes completely).
- Family: All IoCs are explicitly SilentBanker -> KEEP.

## Step 4: Read File 3 (Social Media)

Extract every IP and domain from all posts. Apply filters:

- Date: Posts from `2026-04-23`, `2026-04-22`, `2026-04-21` -> all WITHIN 7 days.
- Type: Extract IPs and domains (ignore the MD5 hash `a1b2c3d4e5f6789012345678901234ab`).
- Family: All posts mention SilentBanker -> KEEP.

## Step 5: Read File 4 (Sandbox Report)

Extract every IP and domain. Apply filters:

- Date: Report dated `2026-04-23` -> WITHIN 7 days.
- Type: IPs and domains only.
- Family: SilentBanker confirmed -> KEEP.

Special note:

- `ocsp.digicert.com` is marked as legitimate -> EXCLUDE this (false positive).

## Step 6: Read File 5 (RSS Aggregator)

Extract every IP and domain from all 4 RSS items. Apply filters carefully:

| RSS Item | Date | IoCs | Family | Decision |
| --- | --- | --- | --- | --- |
| Item 1 (ThreatPost) | 2026-04-22 | `corona-vaccine-update.com`, `193.42.33.90` | Phishing/Generic | EXCLUDE (not banking-related) |
| Item 2 (Unit 42) | 2026-04-21 | `rbm-updates.com`, `secure-banking-portal.eu`, `185.143.223.117`, `185.143.223.118`, `[hash]` | SilentBanker | KEEP (IPs and domains only, ignore hash) |
| Item 3 (SANS ISC) | 2026-04-20 | `185.143.223.115`, `windows-defender-alert.com` | SilentBanker/FakeAlert | KEEP the IP, EXCLUDE the domain (fake alert, not banking) |
| Item 4 (CISA) | 2026-04-19 | `185.143.223.115`, `91.243.45.50`, `45.155.205.100`, `bank-verification.org`, `swift-update.net`, `[hash]` | SilentBanker | KEEP (IPs and domains only, ignore hash) |

## Step 7: Open the Filtered Output CSV Template (File 8)

Create a new document and copy the entire table.

## Step 8: Fill One Row Per IoC

For each IoC you identified, fill one row in the table.

Example of a correctly filled row:

| IoC Value | Type | Source Feed | Threat Family | Date Observed | Keep/Exclude | Exclusion Reason |
| --- | --- | --- | --- | --- | --- | --- |
| 185.143.223.115 | IP | abuse.ch | SilentBanker | 2026-04-23 | Keep | N/A |

## Step 9: Create the "RELEVANT IoCs (KEPT) - Summary List"

At the bottom of your CSV, write only the IoCs marked `Keep` in the table above. Format as one per line:

```text
RELEVANT IoCs (KEPT):
185.143.223.115
185.143.223.116
185.143.223.117
185.143.223.118
45.155.205.88
45.155.205.100
91.243.45.12
91.243.45.50
193.42.33.88
banking-update-service.com
swift-message-check.net
rbm-portal.org
rbm-updates.com
secure-banking-portal.eu
bank-verification.org
swift-update.net
customer-support-portal.xyz
secure-message-alert.info
microsoft-security-upgrade.com
adobe-flash-update-required.net
```

## Step 10: Create the "EXCLUDED IoCs (FILTERED OUT) - Summary List"

Add excluded IoCs and explain why each one was filtered out:

```text
EXCLUDED IoCs (FILTERED OUT):
85.209.11.22 - Reason: Emotet family, not banking-related (excluded by family filter)
45.155.205.33 - Reason: Office365 phishing, not banking trojan
corona-vaccine-update.com - Reason: Phishing, not banking-related
193.42.33.90 - Reason: Generic threat, no banking association
windows-defender-alert.com - Reason: Fake alert, not legitimate banking threat
ocsp.digicert.com - Reason: Legitimate domain, false positive
[hash values] - Reason: File hashes excluded by type filter (IP/domain only)
```

## Step 11: Verify Your Counts

- Total IoCs extracted from all 5 feeds: Approximately `35-40`
- Kept IoCs: Approximately `20-25`
- Excluded IoCs: Approximately `10-15`

## Step 12: Final Review

Verify the following:

- You processed ALL 5 feeds (none skipped).
- You extracted IPs AND domains (no hashes, no URLs with paths).
- You applied the date filter (only `2026-04-16` to `2026-04-23`).
- You applied the family filter (SilentBanker/banking only).
- Your CSV has a row for EVERY IoC (both kept AND excluded).
- Every excluded IoC has an exclusion reason.
- Your summary lists match your table.

> Insert additional notes or instructor guidance here if needed.
