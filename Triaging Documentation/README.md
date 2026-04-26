# Triaging Documentation

## Purpose
This folder contains documentation for SOC triage workflows, examples, and notes. It is intended to grow continuously as we practice and document more cases.

## Starting guide
Use this guide to learn how to triage alerts step by step, with a focus on web reconnaissance and Security Onion observations.

### 1. Identify the alert
- Note the alert name, signature ID, category, and severity.
- Example: `GPL WEB_SERVER 403 Forbidden`, SID `2101201`, category `Attempted Information Leak`, severity `2`.

### 2. Understand the traffic flow
- Determine source IP, destination IP, source port, and destination port.
- Identify which host is the server and which is the client.
- Example: `src_ip` = web server, `dest_ip` = scanning client for a `to_client` HTTP response alert.

### 3. Inspect the payload and metadata
- Look for HTTP status codes, requested URIs, and protocol details.
- In reconnaissance cases, the payload often contains many `404 Not Found` or `403 Forbidden` responses.
- Check `flowbits` or `metadata` for additional context.

### 4. Correlate with known tools or activity
- Compare the alert against actions you performed or expected behavior in the lab.
- Example: directory brute-force tools like `gobuster` or `dirb` generate many sequential HTTP requests and 404 responses.

### 5. Determine the alert type
Classify the activity as one of:
- Reconnaissance / scanning
- Exploitation attempt
- Credential abuse
- Data exfiltration
- Lateral movement

### 6. Validate authorization
- Confirm whether the source host is authorized to perform testing.
- In a lab, authorized scanner traffic is expected; in a real environment, treat it as suspicious if not approved.

### 7. Decide next action
- If authorized lab activity: document it and monitor for follow-up events.
- If unauthorized: escalate or investigate further.
- Look for subsequent alerts from the same source or targeting the same destination.

### 8. Document conclusions
Capture the following in your triage notes:
- Event type
- Source and destination
- Evidence from alerts/logs
- Assessment (e.g., reconnaissance detected)
- Recommended action

## Next steps
Add new files for specific alert types and real-world examples, such as:
- `HTTP Reconnaissance triage`
- `SSH brute force triage`
- `Web exploit triage`
- `Event context enrichment`

---

This documentation is intended to expand continuously as new triage cases are encountered.