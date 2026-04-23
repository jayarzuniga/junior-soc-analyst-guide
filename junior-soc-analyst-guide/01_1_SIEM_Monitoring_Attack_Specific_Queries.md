# SIEM Monitoring: Practical Guide with Attack-Specific Queries and Indicators

## 📌 Overview

This guide provides practical SIEM monitoring techniques, common query syntaxes, and specific indicators to spot different attack types across Windows and Linux systems.

---

## 🔍 SIEM Query Syntax Fundamentals

### Splunk Query Syntax

**Basic Search:**
```
source="location" | search "term"
index=main sourcetype=WinEventLog:Security EventCode=4688
```

**Filter by Time:**
```
index=main earliest=-24h latest=now EventCode=4688
index=main earliest=-1h
```

**Logical Operators:**
```
EventCode=4688 AND user=Administrator        # AND both conditions
EventCode=4688 OR EventCode=4689              # OR either condition
NOT EventCode=4624                            # NOT this event
```

**Pipeline Operations:**
```
index=main EventCode=4688 | stats count by user
index=main EventCode=4688 | top 10 user
index=main EventCode=4688 | where command_line="*cmd.exe*"
```

### ELK/Elasticsearch Query Syntax

**Basic Query:**
```json
{
  "query": {
    "match": {
      "event.code": "4688"
    }
  }
}
```

**Bool Query (AND/OR/NOT):**
```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "event.code": "4688" } },
        { "match": { "user.name": "Administrator" } }
      ],
      "must_not": [
        { "match": { "process.name": "svchost.exe" } }
      ]
    }
  }
}
```

**Range Query (Time):**
```json
{
  "query": {
    "range": {
      "@timestamp": {
        "gte": "now-24h",
        "lte": "now"
      }
    }
  }
}
```

### QRadar Query Syntax

**Basic AQL Query:**
```
SELECT sourceIp, destinationIp, eventCount 
WHERE severity >= 5 
LAST 24 HOURS
```

**With Grouping:**
```
SELECT sourceIp, COUNT(*) as event_count
FROM events
WHERE eventType = "Intrusion"
GROUP BY sourceIp
```

---

## 🦠 MALWARE DETECTION

### What to Look For
- Suspicious process execution
- Unauthorized file modifications
- Network connections to known malicious IPs
- Registry modifications (Windows)
- Suspicious parent-child process relationships
- Unusual command-line arguments

### Windows Malware Indicators

#### Critical Event IDs:
- **4688**: Process Creation (command line execution)
- **4689**: Process Termination
- **4697**: Service Installation
- **7045**: New Service Installed
- **13**: Registry Value Set (malware often modifies registry)
- **11**: FileCreate (suspicious file creation)

#### Key Indicators:
```
- Process: cmd.exe, powershell.exe with suspicious arguments
- File: .exe, .dll, .scr in temp folders (C:\Windows\Temp, C:\Users\*\AppData\Local\Temp)
- Registry: HKLM\Software\Microsoft\Windows\Run (persistence)
- Network: Unusual outbound connections
```

#### Splunk Queries:

**Suspicious Process Creation:**
```
index=main sourcetype=WinEventLog:Security EventCode=4688 
| search (command_line="*cmd.exe*" OR command_line="*powershell.exe*") 
AND (command_line="*certutil*" OR command_line="*curl*" OR command_line="*wget*")
```

**Suspicious Parent-Child Process:**
```
index=main sourcetype=WinEventLog:Security EventCode=4688 
| search (ParentProcessName="explorer.exe" OR ParentProcessName="svchost.exe") 
AND (ProcessName="cmd.exe" OR ProcessName="powershell.exe" OR ProcessName="calc.exe")
```

**Registry Persistence Attempt:**
```
index=main sourcetype="WinEventLog:Sysmon" EventCode=13 
| search TargetObject="*\Run\*" OR TargetObject="*\RunOnce\*" OR TargetObject="*\Services\*"
```

**File Creation in Suspicious Locations:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=11 
| search (TargetFilename="*\Temp\*" OR TargetFilename="*\AppData\Local\Temp\*") 
AND (TargetFilename="*.exe" OR TargetFilename="*.dll" OR TargetFilename="*.scr")
```

**Network Connection to Known Bad IP:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=3 
| search DestinationIp IN (192.168.1.100, 10.0.0.50) 
AND Protocol=tcp 
AND DestinationPort IN (443, 8080, 4444)
```

### Linux Malware Indicators

#### Key Log Sources:
- `/var/log/auth.log` - Authentication logs
- `/var/log/syslog` - System logs
- `/var/log/secure` - Security logs (RHEL/CentOS)
- `/var/log/audit/audit.log` - Auditd logs
- `/var/log/apache2/access.log` - Web server logs
- Process execution: auditd, syslog

#### Key Indicators:
```
- Process: curl, wget, nc, bash with unusual arguments
- File: .sh, .elf in /tmp, /var/tmp, unusual permissions (777)
- Network: Unusual outbound connections
- Cron: Suspicious cron jobs or modifications
- Permissions: Files with setuid bit set unexpectedly
```

#### ELK Queries:

**Suspicious Process Execution (curl/wget/nc):**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process.name": {
              "query": "curl OR wget OR nc"
            }
          }
        },
        {
          "match": {
            "process.args": {
              "query": "http OR ftp OR shell"
            }
          }
        }
      ]
    }
  }
}
```

**Suspicious File Creation in /tmp:**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "file.path": "/tmp/*"
          }
        },
        {
          "match": {
            "file.extension": "sh OR elf OR bin"
          }
        }
      ]
    }
  }
}
```

**Cron Job Modification:**
```
grep "CRON" /var/log/syslog 
grep "(CRON)" /var/log/auth.log 
crontab -l
```

---

## 🔐 RANSOMWARE DETECTION

### What to Look For
- Mass file encryption/modification
- File extension changes (.encrypt, .locked, .xyz, etc.)
- Registry modification attempts
- Shadow copy deletion (Windows)
- Unusual disk I/O activity
- Process access to numerous files
- Service stop attempts (backup services)

### Windows Ransomware Indicators

#### Critical Event IDs:
- **4688**: Process Creation (file encryption process)
- **4697**: Service Installed (launch malware)
- **4690**: Attempt to delete object (registry deletion)
- **13**: Registry Value Set
- **11**: FileCreate (new extensions)
- **23**: FileDelete (document deletion)
- **26**: ClipboardChange (data staging)

#### Splunk Queries:

**Mass File Access Pattern:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=11 
| stats count by TargetFilename 
| search count > 1000 
| where TargetFilename!="C:\Windows\*"
```

**File Extension Anomaly:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=11 
| regex TargetFilename="\.(encrypt|xyz|locked|crypto|bit|cerber|teslacrypt)\$" 
| stats count by user, Computer
```

**Shadow Copy Deletion (vssadmin.exe):**
```
index=main sourcetype=WinEventLog:Security EventCode=4688 
| search (ProcessName="*vssadmin*" AND CommandLine="*delete*") 
OR (ProcessName="*cmd.exe*" AND CommandLine="*wmic*shadowcopy*")
```

**Service Stop Attempts:**
```
index=main sourcetype=WinEventLog:Security EventCode=4688 
| search (CommandLine="*net stop*" OR CommandLine="*sc stop*") 
AND (CommandLine="*backup*" OR CommandLine="*SQL*" OR CommandLine="*antivirus*")
```

**Registry Run Key Persistence:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=13 
| search TargetObject="*\Run\*" OR TargetObject="*\RunOnce\*" 
| stats count by Computer, SourceIp
```

### Linux Ransomware Indicators

#### Key Indicators:
```
- High disk I/O activity
- File extension changes
- chattr +i (making files immutable)
- File permission changes (chmod 000)
- Process accessing many files
- Large number of file deletions
```

#### Auditd Monitoring:

**File Access Pattern:**
```
# In audit rules
-w /home/ -p wa -k file_changes
-w /var/www/ -p wa -k web_changes

# Query
ausearch -k file_changes | grep "type=EXECVE" | wc -l
```

**Directory Traversal:**
```
ausearch -k file_changes | grep "name=" | head -100
```

**Permission Changes:**
```
grep "chmod" /var/log/audit/audit.log
grep "setattr" /var/log/audit/audit.log | head -20
```

---

## 🔓 BRUTE FORCE / PASSWORD ATTACK

### What to Look For
- Multiple failed login attempts
- Failed login followed by success
- Unusual login times
- Login from unusual locations
- Multiple users from same source
- Rapid authentication attempts

### Windows Brute Force Indicators

#### Critical Event IDs:
- **4625**: Failed Login Attempt
- **4624**: Successful Login
- **4768**: Kerberos Ticket Request (TGT) - can indicate pass-the-hash
- **4771**: Kerberos Pre-auth Failed
- **4776**: NTLM Authentication Attempted

#### Splunk Queries:

**Failed Login Attempts by User:**
```
index=main sourcetype=WinEventLog:Security EventCode=4625 
| stats count as failures by user, SourceIp 
| where failures > 5
```

**Failed Login Followed by Success (Successful Brute Force):**
```
index=main sourcetype=WinEventLog:Security (EventCode=4625 OR EventCode=4624) 
| transaction user, SourceIp startswith=(EventCode=4625) endswith=(EventCode=4624) 
| search eventcount > 10
```

**Multiple Users from Same Source (Lateral Movement Detection):**
```
index=main sourcetype=WinEventLog:Security EventCode=4624 
| stats dc(user) as unique_users by SourceIp 
| where unique_users > 10
```

**RDP Brute Force:**
```
index=main sourcetype=WinEventLog:Security EventCode=4625 
| search SourceIp!="127.0.0.1" AND SourceIp!="LOCAL" 
| search LogonType=3 
| stats count as failures by SourceIp, user 
| where failures > 20
```

**Kerberos Pre-Auth Failures (Offline Attacks):**
```
index=main sourcetype=WinEventLog:Security EventCode=4771 
| stats count as failures by user, SourceIp 
| where failures > 10
```

### Linux Brute Force Indicators

#### Key Log Patterns:
```
/var/log/auth.log:  "Failed password for"
/var/log/auth.log:  "Invalid user"
/var/log/secure:    "Failed password for"
```

#### Queries:

**SSH Failed Login Attempts:**
```
grep "Failed password" /var/log/auth.log | grep "ssh" | wc -l
grep "Invalid user" /var/log/auth.log | wc -l
```

**Successful Login After Failures:**
```
grep "Failed password.*user root" /var/log/auth.log
grep "Accepted password.*root" /var/log/auth.log
```

**Monitor in Real-time:**
```
tail -f /var/log/auth.log | grep "Failed\|Invalid"
```

**ELK Query:**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "Failed password OR Invalid user"
          }
        }
      ]
    }
  }
}
```

---

## 🔄 LATERAL MOVEMENT

### What to Look For
- Unusual logons from system to system
- Pass-the-hash (NTLM relay)
- Abnormal SMB traffic
- Suspicious service creation
- Unusual scheduled task creation
- WMI execution on remote systems

### Windows Lateral Movement Indicators

#### Critical Event IDs:
- **4624**: Logon Success (look for LogonType 3, 9 - network logons)
- **4672**: Special Privileges Assigned (check for "Administrator")
- **4688**: Process Creation (network spawned)
- **4719**: Security Policy Modified
- **5156**: Network Connection Allowed (SMB: port 445, WinRM: 5985/5986)

#### Splunk Queries:

**Abnormal Network Logons:**
```
index=main sourcetype=WinEventLog:Security EventCode=4624 
| search LogonType=3 
| search SourceIp!="*255" 
| search NOT (SourceComputerName="DC*" OR SourceComputerName="*server*")
| stats count by user, TargetComputerName, SourceIp
```

**Pass-the-Hash Indicator (4768 + 4769):**
```
index=main sourcetype=WinEventLog:Security (EventCode=4768 OR EventCode=4769) 
| search NOT IpAddress="127.0.0.1" 
| stats count by user 
| where count > 20
```

**Suspicious SMB Session Setup:**
```
index=main sourcetype=WinEventLog:Security EventCode=5140 
| search ObjectType="File" 
| stats count by SourceIp, ShareName 
| where count > 100
```

**WMI Execution on Remote System:**
```
index=main sourcetype=WinEventLog:WmiActivity EventCode=11 
| search SourceIp!="127.0.0.1" 
| stats count by SourceIp, user
```

**Scheduled Task Creation (Persistence + Lateral Movement):**
```
index=main sourcetype=WinEventLog:Security EventCode=4698 
| search TaskName!="*\Microsoft\*" 
| stats count by Computer, user
```

### Linux Lateral Movement Indicators

#### Key Indicators:
```
SSH key addition to authorized_keys
SSH connection logs to/from systems
Unusual sudo usage
cron job creation
SSH port forwarding
```

#### Queries:

**SSH Key Addition:**
```
grep "authorized_keys" /var/log/auth.log
grep "sshd" /var/log/auth.log | grep "Accepted"
```

**Monitor Remote SSH Connections:**
```
w  # Who's logged in
who  # Another way to check
last  # Login history
```

**Sudo Usage Anomalies:**
```
grep "sudo" /var/log/auth.log | grep -v "sudo.*COMMAND"
sudo -l  # What can user execute
```

**ELK Query for Lateral Movement:**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process.name": "ssh OR scp OR rsync"
          }
        },
        {
          "match": {
            "user.name": {
              "query": "root OR sudo"
            }
          }
        }
      ]
    }
  }
}
```

---

## 📤 DATA EXFILTRATION

### What to Look For
- Unusual outbound network traffic
- Large data transfers
- Connections to suspicious external IPs
- Uncommon ports (53 for DNS tunneling)
- Protocol mismatch (HTTP on 443)
- Compression tools usage
- Archive creation
- Cloud service upload activity

### Windows Data Exfiltration Indicators

#### Critical Event IDs:
- **5156**: Network Connection Allowed (Firewall)
- **3**: Network Connection (Sysmon)
- **11**: FileCreate (staging files)
- **4688**: Process Creation (7z, WinRAR, curl, wget)

#### Splunk Queries:

**Unusual Outbound Connections:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=3 
| search DestinationPort NOT IN (80, 443, 53, 25, 110, 143, 445, 3389) 
| stats count by DestinationIp, DestinationPort, user, ProcessName 
| where count > 50
```

**Large Data Transfer (Bytes):**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=3 
| stats sum(SourceIsIpv6) by DestinationIp, ProcessName 
| search ProcessName!="chrome.exe" AND ProcessName!="firefox.exe"
```

**Archive Creation + Network Activity Correlation:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=11 
| search TargetFilename="*.zip" OR TargetFilename="*.7z" OR TargetFilename="*.rar" 
| transaction user startswith=(EventCode=11) endswith=(EventCode=3) 
| where DestinationPort > 1024
```

**Suspicious Application with Network Access:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=3 
| search ProcessName IN ("curl.exe", "wget.exe", "ftp.exe", "ssh.exe") 
| stats count by ProcessName, user, DestinationIp
```

**Cloud Service Upload Detection:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=3 
| search DestinationHostname IN ("*.dropbox.com", "*.google.com", "*.microsoft.com", "*.box.com", "*.slack.com") 
| stats count by user, DestinationHostname, ProcessName
```

### Linux Data Exfiltration Indicators

#### Key Indicators:
```
Large file transfers via scp/sftp
Unusual outbound connections
Data compression/archiving
Cloud CLI tool usage (aws, gsutil)
Network protocols on unusual ports
```

#### Queries:

**Monitor Network Connections:**
```
netstat -tupan | grep ESTABLISHED
ss -tupan | grep ESTABLISHED
lsof -i -P -n | grep ESTABLISHED
```

**File Compression Activity:**
```
grep "tar\|gzip\|zip" /var/log/audit/audit.log
ls -la /tmp/*.tar.gz /tmp/*.zip 2>/dev/null
```

**Outbound SSH/SCP Activity:**
```
grep "scp\|sftp\|ssh" /var/log/auth.log
grep "openssh" /var/log/syslog
```

**Monitor Large File Transfers:**
```
# Watch for files > 100MB transferred
lsof | grep -E "scp|sftp|curl|wget" | awk '{print $NF}' | xargs ls -lh
```

**ELK Query:**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process.name": "curl OR wget OR nc OR tar OR gzip"
          }
        },
        {
          "match": {
            "destination.ip": {
              "query": "NOT 10.* AND NOT 172.16.* AND NOT 192.168.*"
            }
          }
        }
      ]
    }
  }
}
```

---

## 🔑 PRIVILEGE ESCALATION

### What to Look For
- Failed privilege escalation attempts
- Successful privilege escalation
- Unusual sudo usage
- Kernel exploit attempts
- UAC bypass attempts
- Service privilege abuse

### Windows Privilege Escalation Indicators

#### Critical Event IDs:
- **4672**: Special Privileges Assigned (Administrative rights)
- **4673**: Sensitive Privilege Used (SeDebugPrivilege, SeTcbPrivilege)
- **4688**: Process Creation (with elevated privileges)
- **4797**: User Account Control (UAC) related)

#### Splunk Queries:

**Successful Admin Rights Assignment:**
```
index=main sourcetype=WinEventLog:Security EventCode=4672 
| search NOT TargetUserName IN ("SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE") 
| stats count by TargetUserName, LogonId, TargetDomainName
```

**UAC Bypass Attempts:**
```
index=main sourcetype=WinEventLog:Security EventCode=4797 
| search PrivilegeList!="" 
| stats count by user, Computer
```

**Sensitive Privilege Use (SeDebugPrivilege):**
```
index=main sourcetype=WinEventLog:Security EventCode=4673 
| search PrivilegeUsed="SeDebugPrivilege" OR PrivilegeUsed="SeTcbPrivilege" 
| stats count by user, ProcessName
```

**Process Creation with System/Admin Context:**
```
index=main sourcetype=WinEventLog:Sysmon EventCode=1 
| search User="NT AUTHORITY\SYSTEM" OR User="*\Administrator" 
| search NOT ParentProcessName="C:\Windows\*" 
| stats count by ProcessName, ParentProcessName, user
```

### Linux Privilege Escalation Indicators

#### Key Indicators:
```
Failed sudo attempts
Setuid bit modifications
Kernel exploit attempts
Sudo configuration changes
/etc/passwd modifications
cron job execution as root
```

#### Queries:

**Failed sudo Attempts:**
```
grep "sudo.*COMMAND=" /var/log/auth.log | grep "( root )"
grep "sudo: " /var/log/auth.log | grep "3 incorrect"
```

**Files with Setuid Bit:**
```
find / -perm -4000 -type f 2>/dev/null  # All setuid files
find / -perm -4000 -type f -mtime -7 2>/dev/null  # Recent changes
```

**Successful sudo Usage:**
```
grep "sudo.*COMMAND=" /var/log/auth.log | head -20
sudo -l  # What can user run
```

**ELK Query:**
```
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "sudo OR setuid OR privilege"
          }
        },
        {
          "match": {
            "user.name": {
              "query": "root OR wheel"
            }
          }
        }
      ]
    }
  }
}
```

---

## 📋 QUICK REFERENCE: Event ID Cheat Sheet

### Windows Event IDs (Security Log)

| Event ID | Description | What to Watch |
|----------|-------------|----------------|
| 4624 | Successful Logon | LogonType, SourceIp |
| 4625 | Failed Logon | Multiple failures = brute force |
| 4720 | User Account Created | Unauthorized users |
| 4722 | User Account Enabled | Dormant accounts enabled |
| 4728 | User Added to Group | Privilege escalation |
| 4732 | User Added to Local Group | Local admin addition |
| 4735 | Security Group Modified | Permission changes |
| 4768 | Kerberos Ticket Request | Pass-the-hash indicator |
| 4769 | Kerberos Service Ticket | Multiple requests = attack |
| 4771 | Kerberos Pre-auth Failed | Brute force |
| 4776 | NTLM Authentication | Lateral movement |
| 4781 | Account Renamed | Account masking |
| 4798 | User Rights Changed | Escalation attempt |

### Windows Event IDs (Sysmon)

| Event ID | Description | What to Watch |
|----------|-------------|----------------|
| 1 | Process Creation | Command line, parent process |
| 3 | Network Connection | Suspicious IPs, ports |
| 6 | Driver Loaded | Unsigned drivers |
| 7 | Image Loaded | Suspicious DLLs |
| 8 | CreateRemoteThread | Code injection |
| 9 | RawAccessThread | Raw disk access |
| 10 | ProcessAccess | Process access (privilege escalation) |
| 11 | FileCreate | Malware artifacts, persistence |
| 13 | Registry Set | Registry modifications |
| 15 | FileCreateStreamHash | Alternate data streams |
| 17 | PipeCreated | Malware communication |
| 23 | FileDelete | Evidence removal |
| 26 | ClipboardChange | Data staging |
| 28 | FileExecutableDetected | Suspicious executable |

### Linux Log Patterns

| Log Source | Pattern | What to Watch |
|-----------|---------|----------------|
| /var/log/auth.log | "Failed password" | Brute force attempts |
| /var/log/auth.log | "Accepted password" | Successful logins |
| /var/log/auth.log | "Invalid user" | Non-existent user |
| /var/log/audit/audit.log | type=EXECVE | Command execution |
| /var/log/audit/audit.log | name=/etc/passwd | File modification |
| /var/log/syslog | "sudo:" | Sudo usage |
| /var/log/syslog | "kernel:" | Kernel messages |

---

## 🎯 Daily Monitoring Checklist

### Every Hour
- [ ] Check for critical severity alerts
- [ ] Review failed login attempts
- [ ] Scan for unusual process creation
- [ ] Monitor network connections to external IPs

### Every Shift
- [ ] Review all high-severity alerts
- [ ] Check for trends in medium alerts
- [ ] Verify all escalations were processed
- [ ] Update incident tickets
- [ ] Review any overnight incidents

### Daily
- [ ] Run baseline comparison queries
- [ ] Check for new malware signatures
- [ ] Review user access changes
- [ ] Monitor system health
- [ ] Update threat intelligence

### Weekly
- [ ] Review all security alerts
- [ ] Analyze alert trends
- [ ] Check for policy violations
- [ ] Review audit logs
- [ ] Meet with team to discuss trends

---

## ⚠️ Common False Positives & How to Eliminate Them

### Windows False Positives
- **Many 4688 events**: Normal on busy systems; filter legitimate tools
- **RDP from home**: Normal for remote workers; whitelist known IPs
- **Service restarts**: Schedule maintenance windows; exclude known services
- **File modifications**: Exclude backup software, Windows updates
- **Network connections**: Exclude legitimate cloud services, CDNs

### Linux False Positives
- **SSH attempts**: Normal; baseline expected users
- **Cron jobs**: Schedule and whitelist legitimate jobs
- **Package updates**: Normal during maintenance; track timing
- **Log rotation**: Expected; don't alert on logrotate
- **Backup processes**: Expected; whitelist backup user

---

## 🔗 Useful Query Building Blocks

### Find Processes by User
**Splunk:**
```
index=main sourcetype=WinEventLog:Security EventCode=4688 user=Administrator
```

**ELK:**
```json
{ "match": { "user.name": "Administrator" } }
```

### Find Activity in Time Range
**Splunk:**
```
index=main earliest=-6h latest=now EventCode=4624
```

**ELK:**
```json
{ "range": { "@timestamp": { "gte": "now-6h" } } }
```

### Exclude System Processes
**Splunk:**
```
ProcessName!=*svchost.exe* AND ProcessName!=*System* AND ProcessName!=*Services.exe*
```

**ELK:**
```json
{
  "bool": {
    "must_not": [
      { "match": { "process.name": "svchost.exe" } },
      { "match": { "process.name": "System" } }
    ]
  }
}
```

### Count Occurrences
**Splunk:**
```
| stats count as total, count(distinct user) as unique_users by SourceIp
```

**ELK:**
```json
{
  "aggs": {
    "by_ip": {
      "terms": { "field": "source.ip", "size": 100 }
    }
  }
}
```

---

## 📚 Additional Resources

- **Splunk Documentation**: https://docs.splunk.com/
- **Elasticsearch/ELK**: https://www.elastic.co/guide/
- **Windows Event IDs**: https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-failure-events
- **Sysmon**: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon
- **LINUX Logging**: https://linux.die.net/man/1/logger
- **Auditd Reference**: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/chap-system_auditing

---

Last Updated: April 22, 2026
