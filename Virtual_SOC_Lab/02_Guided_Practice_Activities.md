# Guided Practice Activities

These activities are written as SOC analyst practice, not as a penetration testing course. The focus is on observing activity, collecting evidence, interpreting logs, and documenting what happened.

Use your own IP addresses in place of the placeholders.

> Important: Use only private lab IP addresses on an isolated internal network or host-only network. Do not put the lab VMs on your host's production or internet-facing network, because upgrades and updates on the lab VMs can otherwise affect the host and surrounding systems.

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
5. Create a simple table in your notes using the private/internal lab IP addresses only:

| System | Role | IP Address | Notes |
| --- | --- | --- | --- |
| Kali Linux | Analyst/testing workstation |  |  |
| Metasploitable | Vulnerable target |  |  |
| Security Onion | Monitoring platform |  |  |

6. From Kali, ping Metasploitable:

```bash
ping -c 4 <metasploitable-ip>
```

7. Write down whether the ping worked.

### SOC Documentation Practice

Write a short note:

```text
Lab connectivity validated. Kali can reach Metasploitable at <ip>. Security Onion management interface is available at <ip>. This confirms the lab is ready for monitoring exercises.
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
6. Search for traffic involving Kali and Metasploitable.
7. Look for evidence of:
   - ICMP traffic
   - TCP connection attempts
   - Port scan or service scan alerts
   - Any Suricata or Zeek records related to the activity

### Questions to Answer

- Which ports were open on Metasploitable?
- Which services looked risky or outdated?
- Did Security Onion show the scan activity?
- What log source gave you the clearest evidence?

### Example Analyst Note

```text
Observed service discovery from Kali <ip> to Metasploitable <ip>. Nmap identified multiple open services including FTP, SSH, Telnet, HTTP, and database-related ports. Security Onion showed network activity between the two lab hosts. This activity is expected because it was part of an authorized lab exercise.
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
4. In Security Onion, search for HTTP traffic between Kali and Metasploitable.
5. Identify:
   - Source IP
   - Destination IP
   - HTTP host
   - URI paths visited
   - User agent if available
6. Document at least three HTTP requests.

### Questions to Answer

- What web applications were available?
- Which HTTP paths did you visit?
- Did Security Onion show the same activity you performed?
- Why is HTTP traffic easier to inspect than encrypted HTTPS traffic?

### SOC Documentation Practice

Write a short timeline:

```text
10:15 - Kali browsed to http://<metasploitable-ip>/.
10:17 - Analyst opened available web application links.
10:20 - Security Onion review confirmed HTTP traffic from Kali <ip> to Metasploitable <ip>.
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
4. In Security Onion, search for SSH traffic between Kali and Metasploitable.
5. Review any Zeek connection logs or alerts related to the session.

### Questions to Answer

- Was the SSH connection visible?
- Could you determine whether the login succeeded from network logs alone?
- What additional host logs would help confirm success or failure?
- When should repeated failed logins be escalated?

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
   - Security Onion logs
   - Your notes
3. Write a short report using this format:

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
Nmap output listed open TCP services. Security Onion showed connections from Kali to Metasploitable during the scan.

Assessment:
Activity was authorized lab traffic. In a production environment, similar scanning from an unknown source could indicate reconnaissance.

Recommended Action:
No containment needed in the lab. Preserve notes and continue with detection practice.
```

