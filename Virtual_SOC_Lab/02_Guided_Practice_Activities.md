# Guided Practice Activities

These activities are written as SOC analyst practice, not as a penetration testing course. The focus is on observing activity, collecting evidence, interpreting logs, and documenting what happened.

Use your own IP addresses in place of the placeholders.

> Important: Use only private lab IP addresses on an isolated internal network or host-only network. Do not put the lab VMs on your host's production or internet-facing network, because upgrades and updates on the lab VMs can otherwise affect the host and surrounding systems.

---

## Security Onion Tool Map for These Activities

Security Onion is not just a place to "check logs." In these activities, use specific parts of Security Onion Console (SOC):

| Security Onion Tool | Use It For | Beginner Analyst Question |
| --- | --- | --- |
| Alerts | Review Suricata/NIDS alerts and possible detections | Did Security Onion create an alert for this activity? |
| Hunt | Search event data across Zeek, Suricata, and other indexed logs | What happened between these two IP addresses? |
| Dashboards | View grouped summaries such as protocol logs, NIDS alerts, DNS, HTTP, and connections | Which log type gives the clearest picture? |
| PCAP | Retrieve packet capture for a specific time window and IP pair | What did the actual network packets show? |
| Cases | Create a simple investigation record and attach important evidence | How would I document and track this investigation? |

Reference docs:

- Security Onion Console overview: https://docs.securityonion.net/en/2.4/soc.html
- Alerts: https://docs.securityonion.net/en/2.4/alerts.html
- Dashboards: https://docs.securityonion.net/en/2.4/dashboards.html
- Cases: https://docs.securityonion.net/en/2.4/cases.html

### Recommended Search Pattern

For each activity, record the start and end time before you generate traffic. Then use this basic Security Onion workflow:

1. Open Security Onion Console:

```text
https://<security-onion-management-ip>
```

2. Set the time picker to the activity window, such as the last 15 minutes.
3. Go to **Hunt**.
4. Search for traffic involving Kali and Metasploitable.

Use one of these beginner-friendly query styles, depending on what your Security Onion version accepts:

```text
<kali-ip>
```

```text
source.ip:<kali-ip> AND destination.ip:<metasploitable-ip>
```

```text
(source.ip:<kali-ip> AND destination.ip:<metasploitable-ip>) OR (source.ip:<metasploitable-ip> AND destination.ip:<kali-ip>)
```

5. Pivot from the results:
   - Use **Alerts** if you see a detection or scan-related alert.
   - Use **Dashboards** to group activity by protocol, source IP, destination IP, destination port, or event type.
   - Use **PCAP** only for a narrow time range and specific IP pair.
   - Use **Cases** if the activity should be documented as an investigation.

If you do not see results immediately, check that the Security Onion monitoring interface is connected to the same lab network as Kali and Metasploitable, then widen the time picker.

---

## Activity 1: Build a Lab Asset Inventory

### Objective

Create a basic inventory of your three lab systems so you know what you are investigating.

### Steps

1. Start Kali, Metasploitable, and Security Onion.
2. On Kali, identify your IP address:

```bash
ip addr
```

3. On Metasploitable, identify its IP address:

```bash
ifconfig
```

4. In Security Onion, identify the management IP address and monitoring interface.
5. In Security Onion Console, open **Grid** or the node/status area and confirm Security Onion is healthy.
6. Confirm the left navigation shows the analyst tools used in this guide: **Alerts**, **Hunt**, **Dashboards**, **PCAP**, and **Cases**.
7. Create a simple table in your notes using the private/internal lab IP addresses only:

| System | Role | IP Address | Notes |
| --- | --- | --- | --- |
| Kali Linux | Analyst/testing workstation |  |  |
| Metasploitable | Vulnerable target |  |  |
| Security Onion | Monitoring platform |  |  |

8. From Kali, ping Metasploitable:

```bash
ping -c 4 <metasploitable-ip>
```

9. In Security Onion, go to **Hunt** and search for the Kali and Metasploitable IP addresses during the ping time window.
10. Write down whether the ping worked and whether Security Onion recorded related network activity.

### SOC Documentation Practice

Write a short note:

```text
Lab connectivity validated. Kali can reach Metasploitable at <ip>. Security Onion management interface is available at <ip>. In Security Onion Hunt, analyst searched the activity window for <kali-ip> and <metasploitable-ip> to confirm monitoring visibility.
```

---

## Activity 2: Run Basic Network Discovery

### Objective

Generate simple discovery traffic from Kali to Metasploitable, then document what was scanned.

### Steps

1. Confirm the Metasploitable IP address.
2. From Kali, run a basic host discovery scan:

```bash
nmap -sn <metasploitable-ip>
```

3. Run a basic service scan:

```bash
nmap -sV <metasploitable-ip>
```

4. Save the key results in your notes:
   - Target IP
   - Open ports
   - Detected services
   - Scan time
5. Open Security Onion.
6. Go to **Alerts**.
7. Set the time picker to the period when the Nmap scans ran.
8. Look for scan-related alerts. Examples may include port scan, Nmap, reconnaissance, or Suricata alert names depending on your ruleset.
9. Open any relevant alert and record:
   - Alert name
   - Source IP
   - Destination IP
   - Destination port
   - Sensor or event module
   - Timestamp
10. Pivot from the alert to **Hunt** if your Security Onion version offers a Hunt action. If not, manually open **Hunt**.
11. In **Hunt**, search for traffic involving Kali and Metasploitable:

```text
(source.ip:<kali-ip> AND destination.ip:<metasploitable-ip>) OR (source.ip:<metasploitable-ip> AND destination.ip:<kali-ip>)
```

12. In **Dashboards**, select a connection, Zeek, Suricata, or NIDS dashboard if available. Group or filter by:
   - Source IP
   - Destination IP
   - Destination port
   - Event module
13. Look for evidence of:
   - ICMP traffic
   - TCP connection attempts
   - Port scan or service scan alerts
   - Any Suricata or Zeek records related to the activity
14. Optional: Open **PCAP** for a narrow time range and the Kali-to-Metasploitable IP pair. Do not request a large capture window.

### Questions to Answer

- Which ports were open on Metasploitable?
- Which services looked risky or outdated?
- Did Security Onion show the scan in **Alerts**, **Hunt**, **Dashboards**, or **PCAP**?
- What log source gave you the clearest evidence: Suricata alert, Zeek connection log, or packet capture?
- Did the destination ports in Security Onion match the Nmap output?

### Example Analyst Note

```text
Observed service discovery from Kali <ip> to Metasploitable <ip>. Nmap identified multiple open services including FTP, SSH, Telnet, HTTP, and database-related ports. Security Onion Alerts/Hunt showed network activity between the two lab hosts during the same time window. This activity is expected because it was part of an authorized lab exercise.
```

---

## Activity 3: Investigate Web Traffic to Metasploitable

### Objective

Browse to a vulnerable web service and observe the traffic in Security Onion.

### Steps

1. On Kali, open a browser.
2. Visit:

```text
http://<metasploitable-ip>
```

3. Click through any available web applications on the Metasploitable landing page.
4. Record the start and end time of your browsing.
5. In Security Onion, open **Hunt**.
6. Set the time picker to your browsing window.
7. Search for HTTP traffic between Kali and Metasploitable:

```text
source.ip:<kali-ip> AND destination.ip:<metasploitable-ip> AND network.protocol:http
```

If that does not return results, search only the two IP addresses and then filter the results for HTTP, Zeek HTTP, Suricata HTTP, or `event.module:zeek`.

8. Open **Dashboards** and select an HTTP, Zeek HTTP, or protocol dashboard if available.
9. Identify:
   - Source IP
   - Destination IP
   - HTTP host
   - URI paths visited
   - User agent if available
10. Document at least three HTTP requests.
11. Optional: Use **PCAP** for one small HTTP request window and confirm the request path in the packet data.

### Questions to Answer

- What web applications were available?
- Which HTTP paths did you visit?
- Did Security Onion **Hunt** and **Dashboards** show the same activity you performed?
- Why is HTTP traffic easier to inspect than encrypted HTTPS traffic?

### SOC Documentation Practice

Write a short timeline:

```text
10:15 - Kali browsed to http://<metasploitable-ip>/.
10:17 - Analyst opened available web application links.
10:20 - Security Onion Hunt and Dashboards review confirmed HTTP traffic from Kali <ip> to Metasploitable <ip>.
```

---

## Activity 4: Review Authentication-Related Activity

### Objective

Generate a small number of login attempts and review whether Security Onion records the related network activity.

### Steps

1. From Kali, attempt to connect to SSH on Metasploitable:

```bash
ssh <username>@<metasploitable-ip>
```

2. Use only a small number of attempts. Do not run automated password attacks.
3. Record:
   - Time of attempt
   - Source IP
   - Destination IP
   - Protocol
   - Whether login succeeded or failed
4. Open Security Onion and set the time picker to the SSH attempt window.
5. Start in **Hunt** and search the SSH attempt window:

```text
(source.ip:<kali-ip> AND destination.ip:<metasploitable-ip>) AND destination.port:22
```

6. Review Zeek connection logs, Suricata records, or any alerts related to the session.
7. Open **Dashboards** and group by destination port or protocol to confirm port 22 activity.
8. Check **Alerts** for authentication, SSH, or brute-force related alerts. A small number of manual attempts may not create an alert.
9. Optional: Use **PCAP** for the exact SSH time window to confirm the SSH handshake happened.

### Questions to Answer

- Was the SSH connection visible?
- Could you determine whether the login succeeded from network logs alone?
- What additional host logs would help confirm success or failure?
- When should repeated failed logins be escalated?
- Which Security Onion view was most useful: Hunt, Dashboards, Alerts, or PCAP?

### Analyst Thinking

Network logs can show that an SSH session happened, but they may not always prove whether authentication succeeded. A good analyst separates what is confirmed from what is only suspected.

---

## Activity 5: Create a Mini Investigation Report

### Objective

Practice writing a short SOC investigation summary using your lab activity.

### Steps

1. Pick one activity you performed:
   - Network discovery
   - Web browsing
   - SSH login attempt
2. Gather evidence from:
   - Kali command output
   - Security Onion Alerts, Hunt, Dashboards, or PCAP
   - Your notes
3. In Security Onion, create a case if your lab has **Cases** enabled:
   - Open **Cases**.
   - Create a new case titled with the activity, such as `Authorized Nmap Scan - Lab`.
   - Add the source IP, destination IP, time window, and activity summary.
   - Add observables such as Kali IP, Metasploitable IP, destination ports, and alert names.
   - Add a comment explaining that this was authorized lab activity.
4. Write a short report using this format:

```text
Title:

Summary:

Scope:

Timeline:

Evidence:

Assessment:

Recommended Action:
```

### Example Report

```text
Title:
Authorized Nmap Service Scan Against Metasploitable

Summary:
Kali Linux performed an authorized Nmap service scan against the Metasploitable lab VM. The scan identified several exposed services. Security Onion showed network traffic between the two lab hosts during the test window.

Scope:
Source: Kali <ip>
Destination: Metasploitable <ip>
Time window: <start time> to <end time>

Timeline:
<time> - Analyst confirmed target IP.
<time> - Analyst ran nmap -sV.
<time> - Security Onion logs reviewed.

Evidence:
Nmap output listed open TCP services. Security Onion Alerts/Hunt/Dashboards showed connections from Kali to Metasploitable during the scan. Case notes recorded the source IP, destination IP, time window, and observed ports.

Assessment:
Activity was authorized lab traffic. In a production environment, similar scanning from an unknown source could indicate reconnaissance.

Recommended Action:
No containment needed in the lab. Preserve notes and continue with detection practice.
```
