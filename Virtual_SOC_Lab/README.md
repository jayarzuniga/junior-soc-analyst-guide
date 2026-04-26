# Virtual SOC Lab: Kali Linux, Metasploitable, and Security Onion

## Purpose

This folder documents how to build a small local SOC practice lab using:

- Kali Linux as the analyst and testing workstation
- Metasploitable as the intentionally vulnerable target system
- Security Onion 3 EVAL in Airgap mode as the monitoring, detection, and investigation platform

The goal is to practice how a Junior SOC Analyst observes activity, reviews alerts, investigates evidence, documents findings, and explains risk.

Use this lab only in your own isolated virtual environment. Do not scan, attack, or test systems you do not own or have written permission to assess.

---

## Recommended Reading Order

1. [01_Installation_Setup_Guide.md](01_Installation_Setup_Guide.md)
2. [02_Guided_Practice_Activities.md](02_Guided_Practice_Activities.md)
3. [03_Understanding_Check_Activities.md](03_Understanding_Check_Activities.md)

---

## Lab Design

Recommended network layout:

| Virtual Machine | Role | Recommended Network |
| --- | --- | --- |
| Kali Linux | Analyst/testing workstation | NAT plus Internal Network |
| Metasploitable | Vulnerable target | Internal Network only |
| Security Onion | Monitoring platform | Host-only management plus Internal Network monitoring |

Recommended IP ranges:

| Network | Example Range | Purpose |
| --- | --- | --- |
| Host-only | `192.168.56.0/24` | Access Security Onion Console from the host |
| Internal Network | `192.168.100.0/24` | Isolated lab traffic between Kali and Metasploitable |

Keep the vulnerable Metasploitable VM away from the public internet. It is intentionally insecure and should only be used inside a controlled lab.

---

## What You Will Practice

- Installing and safely isolating lab VMs
- Confirming IP addresses and connectivity
- Running basic discovery from Kali against Metasploitable
- Observing scan and login activity in Security Onion
- Building an investigation timeline
- Writing SOC-style notes
- Answering scenario questions without step-by-step instructions
