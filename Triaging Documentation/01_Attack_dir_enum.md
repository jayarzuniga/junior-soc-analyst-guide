# 01_Attack_dir_enum

## Step-by-step attack documentation
This document describes the exact steps to perform a directory enumeration attack in a lab environment.

### Step 1: Define the target and tools
1. Identify the target IP address.
2. Confirm the web server is running on port `80` or `443`.
3. Choose a directory enumeration tool: `gobuster`, `dirb`, or `wfuzz`.

### Step 2: Run the initial reconnaissance
1. Use `nmap` to verify open web ports and service versions.
   - `nmap -sV -p 80,443 <TARGET_IP>`
2. Confirm HTTP is available and note the server banner.
3. Save the results for later correlation.

### Step 3: Perform directory enumeration
1. Run `gobuster` with a common wordlist.
   - `gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_results.txt`
2. Observe the output for valid paths and response codes.
3. Repeat with alternative wordlists if needed.
   - `gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/raft-large-directories.txt -t 50`

### Step 4: Analyze the scan results
1. Identify discovered directories or files with `200`, `301`, `302`, or `403` responses.
2. Note paths like `/server-status`, `/admin`, `/backup`, `/uploads`, or others that may reveal information.
3. Determine whether discovered paths are sensitive or potentially vulnerable.

### Step 5: Validate interesting findings
1. Test discovered paths manually in a browser or with `curl`.
   - `curl -I http://<TARGET_IP>/server-status`
2. Verify the server response and any exposed information.
3. Record the findings in your attack notes.

### Step 6: Escalate if the attack continues
If directory enumeration reveals interesting content:
1. Check for default credentials or exposed configuration files.
2. Move to exploitation tools if the path indicates a vulnerable application.
3. Capture evidence and log the commands used.

### Example command sequence
- `nmap -sV -p 80,443 192.168.56.20`
- `gobuster dir -u http://192.168.56.20 -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_direnum.txt`
- `curl -I http://192.168.56.20/server-status`

### Attack classification
- Name: `dir enum`
- Type: web enumeration / reconnaissance
- Goal: discover hidden directories and files on the web server
- Expected detection: IDS/Suricata alerts for repeated 404/403 responses and suspicious URI enumeration

---

This document is a step-by-step guide for performing a directory enumeration attack in a lab environment.