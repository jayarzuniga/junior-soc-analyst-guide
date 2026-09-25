# Internal Data Sources for Cyber Threat Intelligence (CTI)

## Source Types & Key Fields

### Internal Data Sources for CTI

| Source Type | Description | Typical Data Format | Key Fields for CTI |
| --- | --- | --- | --- |
| SIEM (Security Information & Event Management) | Aggregated logs with correlation and alerting | JSON, CEF, Syslog | Source IP, Dest IP, Username, Event ID, Timestamp |
| Firewall Logs | Network traffic and block/allow decisions | CSV, Syslog, NetFlow | Source/Destination IP, Port, Protocol, Action |
| EDR (Endpoint Detection & Response) | Endpoint process, file, and user activity | JSON, XML | Process Name, Command Line, File Hash, Parent Process |
| Internal Incident Reports | Human-written investigation notes and findings | PDF, DOCX, plain text | IoCs, Timeline, Remediation Steps |

## SIEM Query Concepts You Will Use

### 1. Time Range Filter

Restrict logs to the incident timeframe.

Example:

```text
@timestamp >= "2026-04-01" AND @timestamp <= "2026-04-15"
```

### 2. Field Extraction

Pull specific values for analysis.

Example:

```sql
SELECT source_ip, destination_ip, domain FROM logs
```

### 3. Deduplication

Remove duplicate values for cleaner results.

Example:

```sql
SELECT unique(source_ip) FROM logs
-- or --
SELECT distinct(domain) FROM logs
```

### 4. Filtering

Exclude known-good values to reduce noise.

Example:

```text
NOT dest_ip IN (10.0.0.0/8, 192.168.0.0/16)
```

## Log Extraction Process (5 Steps)

### 1. Identify the Log Source

Determine which system holds the relevant data (firewall, EDR, SIEM, incident report).

### 2. Apply Time Filter

Narrow logs to the incident's time window.

### 3. Extract IoC Fields

Pull out IPs, domains, hashes, usernames, and other indicators.

### 4. Filter False Positives

Remove internal IPs, known legitimate domains, and benign activity.

### 5. Output Unique Values

Generate a deduplicated list of IoCs for further analysis or action.
