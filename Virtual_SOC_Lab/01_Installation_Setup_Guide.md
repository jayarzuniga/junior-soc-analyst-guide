# Installation and Setup Guide

## Lab Safety Rules

- Use this lab only on systems you own.
- Keep Metasploitable isolated from the internet.
- Do not bridge Metasploitable directly to your home, school, or work network.
- Take snapshots before major changes.
- Record VM names, IP addresses, usernames, and passwords in a private note.

---

## Recommended VirtualBox Network Design

Use one isolated lab network where Kali, Metasploitable, and the Security Onion monitoring interface can see the same traffic.

Recommended simple setup:

| Adapter Type | Purpose |
| --- | --- |
| Host-only Adapter | Lets your host computer and VMs communicate without exposing the lab to the internet |
| Internal Network | Keeps VM-to-VM traffic fully isolated inside VirtualBox |
| NAT | Allows Kali to reach the internet for updates when needed |

Suggested beginner design for this guide:

| VM | Adapter 1 | Adapter 2 | Adapter 3 |
| --- | --- | --- | --- |
| Kali Linux | NAT | Internal Network | Optional Host-only |
| Metasploitable | Internal Network | None | None |
| Security Onion | Host-only for web management | Internal Network for monitoring | None |

This setup keeps Security Onion isolated for an Airgap EVAL home lab, gives your host computer a stable path to the Security Onion web UI, and still monitors the isolated Kali-to-Metasploitable lab network.

Always use private internal IP addressing on the lab network. Do not use bridged networking to your physical LAN for the lab VMs, because updates or upgrades inside the lab can otherwise expose traffic or affect your host system.

Security Onion does not need NAT for this Airgap EVAL lab. If you later decide to use Standard mode for online updates, add NAT temporarily, but keep Host-only as the management interface.

---

## Minimum Resource Planning

| VM | CPU | RAM | Disk |
| --- | --- | --- | --- |
| Kali Linux | 2 CPUs | 2-4 GB | 30+ GB |
| Metasploitable | 1 CPU | 512 MB-1 GB | 8+ GB |
| Security Onion 3 EVAL | 4 CPUs | 12 GB minimum, 16 GB better | 200 GB recommended |

Security Onion is the heaviest VM. If setup appears stuck on Elasticsearch-related commands, it may simply be initializing, but low memory or slow disk can make this take a long time. Give the VM 12-16 GB RAM if possible.

---

## Step 1: Create VirtualBox Lab Networks

1. Open VirtualBox.
2. Go to **File > Tools > Network Manager**.
3. Open the **Host-only Networks** tab.
4. Create a new host-only network if one does not already exist. This is for accessing the Security Onion web UI from your host.
5. Example network:
   - IPv4 address: `192.168.56.1`
   - IPv4 network mask: `255.255.255.0`
   - DHCP server: enabled for beginner setup
6. Save the network settings.
7. Use an **Internal Network** name for lab traffic, such as:

```text
soc-lab
```

Use different IP ranges for management and lab traffic:

| Network | Example Range | Purpose |
| --- | --- | --- |
| Host-only | `192.168.56.0/24` | Access Security Onion web UI from the host |
| Internal Network `soc-lab` | `192.168.100.0/24` | Kali-to-Metasploitable lab traffic |

Record the network name, such as `VirtualBox Host-Only Ethernet Adapter`.

---

## Step 2: Install Kali Linux

1. Open VirtualBox.
2. Select **New**.
3. Name the VM `Kali-Linux`.
4. Choose Linux as the type and Debian 64-bit as the version.
5. Assign resources:
   - Memory: 2-4 GB
   - CPU: 2 cores
   - Disk: 30 GB or more
6. Attach the Kali ISO to the virtual optical drive.
7. Start the VM.
8. Choose the graphical installer.
9. Follow the installer prompts:
   - Set hostname, username, and password.
   - Use guided partitioning for a beginner setup.
   - Install the default desktop environment and common tools.
10. After installation, remove the ISO from the virtual drive.
11. Shut down the VM.
12. Configure networking:
   - Adapter 1: NAT
   - Adapter 2: Internal Network named `soc-lab`
   - Optional Adapter 3: Host-only Adapter if you want Kali to open the Security Onion web UI
13. Start Kali and log in.
14. Open a terminal and confirm network details:

```bash
ip addr
ip route
```

Record the Kali lab network IP address.

15. Assign a static lab IP address for Kali using NetworkManager if DHCP is not available.

```bash
nmcli con show
```

You will see something like:

```text
NAME                DEVICE
Wired connection 1  eth0
```

```bash
nmcli con mod "Wired connection 1" ipv4.addresses 192.168.100.10/24
nmcli con mod "Wired connection 1" ipv4.method manual
```

Do not set a gateway on the Internal Network adapter. Kali should use the NAT adapter for internet access.

```bash
nmcli con down "Wired connection 1"
nmcli con up "Wired connection 1"
```

Optional update step:

```bash
sudo apt update
sudo apt upgrade
```

---

## Step 3: Install Metasploitable

Metasploitable is normally provided as a prebuilt vulnerable virtual machine disk.

1. Extract the downloaded Metasploitable archive.
2. In VirtualBox, select **New**.
3. Name the VM `Metasploitable`.
4. Choose Linux as the type and Ubuntu 32-bit or Linux 32-bit as the version.
5. Assign resources:
   - Memory: 512 MB-1 GB
   - CPU: 1 core
6. When asked for a hard disk, choose **Use an existing virtual hard disk file**.
7. Select the extracted Metasploitable virtual disk.
8. Configure networking:
   - Adapter 1: Internal Network named `soc-lab`
   - Do not use Bridged networking
9. Start the VM.
10. Log in using the credentials provided with your Metasploitable download.
11. Confirm the interface and IP address:

```bash
ifconfig
```

You will likely see `eth0`.

12. Make the IP permanent by editing the network config:

```bash
sudo nano /etc/network/interfaces
```

Replace the current content for `eth0` with:

```text
auto eth0
iface eth0 inet static
    address 192.168.100.20
    netmask 255.255.255.0
```

For your lab:

- Kali Internal Network IP: `192.168.100.10`
- Metasploitable Internal Network IP: `192.168.100.20`
- Security Onion Host-only management IP: `192.168.56.30`

13. Restart networking:
```bash
sudo /etc/init.d/networking restart
```

Record the Metasploitable IP address.

---

## Step 4: Install Security Onion

Security Onion can be installed from an ISO. This guide assumes Security Onion 3, such as:

```text
securityonion-3.0.0-20260331.iso
```

For this beginner home lab, use **Airgap EVAL** mode. Do not choose Standalone unless you have the extra memory and want a more production-like deployment.

1. Open VirtualBox.
2. Select **New**.
3. Name the VM `Security-Onion`.
4. Choose Linux 64-bit.
5. Assign resources:
   - Memory: 12 GB minimum, 16 GB better
   - CPU: 4 cores recommended
   - Disk: 200 GB recommended
6. Attach the Security Onion ISO to the virtual optical drive.
7. Configure networking:
   - Adapter 1: Host-only Adapter
   - Adapter 2: Internal Network named `soc-lab`
   - Make sure all enabled adapters have **Cable Connected** enabled
   - On the Internal Network monitoring adapter, set **Promiscuous Mode** to **Allow All**
8. Start the VM.
9. Choose the CLI/no desktop install if you want to save resources. The analyst tools still run in the browser-based Security Onion Console.
10. After the operating system installation completes, log in to the Security Onion terminal.
11. If setup does not start automatically, run:

```bash
sudo SecurityOnion/setup/so-setup iso
```

12. Use these setup choices:

| Setup Question | Choose |
| --- | --- |
| Install type | Airgap |
| Deployment type | EVAL |
| Internet access | Not required for this lab |
| Proxy | None |
| Docker IP range | Default, unless it overlaps your lab network |
| SOC telemetry | No/Disable for a private lab |
| Admin email | A lab email is fine, such as `admin@example.local` |
| Web interface access | Allow your analyst IP or lab subnet |

13. When setup asks about network interfaces, use:

| Interface Purpose | Adapter | IP Mode |
| --- | --- | --- |
| Management / web UI | Host-only adapter | Static |
| Monitor / sniffing | Internal Network adapter | No normal IP if setup allows; monitoring only |

For the Host-only management adapter, use an address in your Host-only range:

```text
Security Onion management IP: 192.168.56.30
Netmask/CIDR: 24
Gateway: leave blank unless setup requires one
```

14. If setup asks how to access the web interface, allow the system you will use as the analyst browser:
   - Kali IP if you will browse from Kali
   - Windows host-only IP, often `192.168.56.1`, if you will browse from the host
   - A private lab subnet such as `192.168.56.0/24` only if that is your actual lab subnet

Do not allow `0.0.0.0/0`.

15. Wait for setup to finish. Elasticsearch-related steps can take 20-45 minutes or longer on slower systems.
16. After installation, log in to the Security Onion console from an allowed browser.

Example:

```text
https://<security-onion-management-ip>
```

Accept the local certificate warning if your browser shows one.

If you cannot reach the web UI because the analyst IP was not allowed, run this on the Security Onion terminal:

```bash
sudo so-firewall includehost analyst <analyst-ip>
```

Example:

```bash
sudo so-firewall includehost analyst 192.168.56.1
```

If `so-firewall` is not found, setup probably has not completed yet.

---

## Step 5: Confirm VM Connectivity

From Kali, test connectivity to Metasploitable:

```bash
ping -c 4 <metasploitable-ip>
```

From Kali, test whether Security Onion management is reachable:

```bash
ping -c 4 <security-onion-management-ip>
```

If you did not add Kali to the Host-only network, test Security Onion management from your Windows host browser instead:

```text
https://<security-onion-management-ip>
```

If ping does not work, check:

- Both VMs are powered on.
- Both VMs are attached to the same host-only or internal network.
- The correct adapter is enabled.
- You recorded the correct IP address.
- Local firewall settings are not blocking traffic.

---

## Step 6: Take Clean Snapshots

Before running activities, take snapshots:

1. Shut down each VM.
2. In VirtualBox, select the VM.
3. Open **Snapshots**.
4. Create a snapshot named `Clean Install`.
5. Add a note with the date and network settings.

Take another snapshot after you confirm all three systems can communicate.

Suggested snapshot name:

```text
Lab Ready - Kali Metasploitable Security Onion Connected
```

---

## Setup Checklist

- [ ] Kali Linux installed
- [ ] Metasploitable imported
- [ ] Security Onion 3 installed in Airgap EVAL mode
- [ ] Lab network created
- [ ] Metasploitable isolated from internet
- [ ] Security Onion Host-only management adapter configured
- [ ] Security Onion Internal Network monitoring adapter configured with Promiscuous Mode set to Allow All
- [ ] IP addresses recorded
- [ ] Kali can reach Metasploitable
- [ ] Security Onion web interface is accessible
- [ ] Clean snapshots created
