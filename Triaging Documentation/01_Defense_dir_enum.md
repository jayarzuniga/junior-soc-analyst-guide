# 01_Defense_dir_enum

## Step-by-step triage documentation
This document explains a structured process for triaging a directory enumeration alert in Security Onion.

### Step 1: Intake the alert
1. Read the alert metadata.
   - Signature: `GPL WEB_SERVER 403 Forbidden`
   - SID: `2101201`
   - Category: `Attempted Information Leak`
   - Severity: `2`
2. Record the source and destination.
   - Source IP: `192.168.56.10` (scanner/client)
   - Destination IP: `192.168.56.20` (web server)
3. Note the flow direction.
   - `to_client` means the web server is responding back to the scanner.

### Step 2: Identify the classification
1. Match the alert to a known attack class.
   - This alert is triggered by HTTP responses with `403` / `404`.
   - It is commonly associated with web path scanning.
2. Assign the case name.
   - Classification: `dir enum`
   - Label: directory enumeration / web reconnaissance

### Step 3: Review the payload and context
1. Inspect the HTTP payload or PCAP.
   - Look for repeated requests to different URIs.
   - Confirm the response codes in the alert payload.
2. Note whether the payload contains estimated scanned paths.
   - Example: `/ppt`, `/pr`, `/pr0n`, `/preload`, `/premium`, `/prepaid`, `/presentation`, `/preserve`, `/press`
3. Check for related metadata.
   - `flowbits`: `http.dottedquadhost` can indicate host identification behavior.

### Step 4: Correlate with known attacker tools
1. Compare the behavior with scanning tools.
   - Many sequential 404/403 responses are typical of `gobuster` or `dirb`.
2. Use log searches to confirm the tool pattern.
   - Search for many HTTP GET requests from the same source IP.
   - Look for user-agent strings or repeated path guesses.

### Step 5: Verify authorization and scope
1. Determine whether this is expected lab activity.
   - Is the source IP a Kali lab machine?
   - Is the destination a known Metasploitable web server?
2. If the test is authorized, document it as benign reconnaissance.
3. If unauthorized, escalate to a higher tier.

### Step 6: Decide the response
1. If authorized lab activity:
   - Mark as `accepted` or `monitor`.
   - Document the test and continue observing for follow-up.
2. If unauthorized:
   - Escalate to incident response.
   - Investigate whether further scanning or exploitation occurs.
3. In either case, search for follow-up alerts.
   - Look for `web exploit`, `cred brute`, or other suspicious activity from the same source.

### Step 7: Document your findings
Create a triage note with:
- Event type: `dir enum`
- Source: scanning client IP
- Destination: web server IP
- Evidence: repeated 404/403 HTTP responses and probed URIs
- Assessment: directory enumeration detected
- Recommendation: monitor for exploitation and verify authorization

### Step 8: Improve detection
1. Add or tune detection rules for directory enumeration if needed.
2. Use the case to teach how web path scanning appears in logs.
3. Save the alert as a lab example for future triage practice.

---

This defense document is a step-by-step guide for triaging directory enumeration alerts.