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
| NAT | Allows a VM to reach the internet for updates when needed |

Suggested beginner design:

| VM | Adapter 1 | Adapter 2 |
| --- | --- | --- |
| Kali Linux | NAT | Host-only or Internal Network |
| Metasploitable | Host-only or Internal Network | None |
| Security Onion | NAT or Host-only for management | Host-only or Internal Network for monitoring |

Always use private internal IP addressing on the lab network. Do not use bridged networking to your physical LAN for the lab VMs, because updates or upgrades inside the lab can otherwise expose traffic or affect your host system.

If your computer has limited RAM or CPU, use Host-only networking for all three VMs and keep only one activity running at a time.

---

## Minimum Resource Planning

| VM | CPU | RAM | Disk |
| --- | --- | --- | --- |
| Kali Linux | 2 CPUs | 2-4 GB | 30+ GB |
| Metasploitable | 1 CPU | 512 MB-1 GB | 8+ GB |
| Security Onion | 4 CPUs | 8-12 GB minimum | 100+ GB recommended |

Security Onion is the heaviest VM. If your computer struggles, reduce other running apps, pause Kali when not needed, or use a smaller Security Onion evaluation install.

---

## Step 1: Create a VirtualBox Host-only Network

1. Open VirtualBox.
2. Go to **File > Tools > Network Manager**.
3. Open the **Host-only Networks** tab.
4. Create a new host-only network if one does not already exist.
5. Example network:
   - IPv4 address: `192.168.56.1`
   - IPv4 network mask: `255.255.255.0`
   - DHCP server: enabled for beginner setup
6. Save the network settings.

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
   - Adapter 2: Host-only Adapter or Internal Network
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

You’ll see something like:

```text
NAME                DEVICE
Wired connection 1  eth0
```

```bash
nmcli con mod "Wired connection 1" ipv4.addresses 192.168.56.10/24
nmcli con mod "Wired connection 1" ipv4.method manual
```

(Optional gateway if needed)

```bash
nmcli con mod "Wired connection 1" ipv4.gateway 192.168.56.1
```

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
   - Adapter 1: Host-only Adapter or Internal Network
   - Do not use Bridged networking
9. Start the VM.
10. Log in using the credentials provided with your Metasploitable download.
11. Confirm the interface and IP address:

```bash
ifconfig
```

You’ll likely see `eth0`.

12. Make the IP permanent by editing the network config:

```bash
sudo nano /etc/network/interfaces
```

Replace the current content for `eth0` with:

```text
auto eth0
iface eth0 inet static
    address 192.168.56.20
    netmask 255.255.255.0
```

For your lab:

- Kali → 192.168.56.10
- Metasploitable → 192.168.56.20
- Security Onion → 192.168.56.30

13. Restart networking:
```bash
sudo /etc/init.d/networking restart
```

Record the Metasploitable IP address.

---

## Step 4: Install Security Onion

Security Onion can be installed from an ISO. It needs more resources than the other two VMs.

1. Open VirtualBox.
2. Select **New**.
3. Name the VM `Security-Onion`.
4. Choose Linux 64-bit.
5. Assign resources:
   - Memory: 8-12 GB minimum
   - CPU: 4 cores recommended
   - Disk: 100 GB or more recommended
6. Attach the Security Onion ISO to the virtual optical drive.
7. Configure networking:
   - Adapter 1: NAT or Host-only for management access
   - Adapter 2: Host-only Adapter or Internal Network for monitoring
8. Start the VM.
9. Follow the installer prompts.
10. Choose an evaluation or standalone style install if you are building a small practice lab.
11. Assign static IP addresses for the lab, since the lab network typically does not use DHCP.

    Example IP plan:

    | VM | IP Address |
    | --- | --- |
    | Kali | 192.168.56.10 |
    | Metasploitable | 192.168.56.20 |
    | Security Onion | 192.168.56.30 |

    Subnet: /24 (255.255.255.0)

    Set IP in Oracle Linux (Security Onion):

    ```bash
    nmcli con show
    ```

    Find the connection name (likely "Wired connection 1"), then run:

    ```bash
    nmcli con mod "Wired connection 1" ipv4.addresses 192.168.56.30/24
    nmcli con mod "Wired connection 1" ipv4.method manual
    nmcli con up "Wired connection 1"
    ```

    This sets the Security Onion management interface to the private lab IP address.
11. During setup, identify:
   - Management interface
   - Monitoring interface
   - Admin username and password
12. After installation, log in to the Security Onion console.
13. From your host or Kali browser, access the Security Onion web interface using the management IP address.

Example:

```text
https://<security-onion-management-ip>
```

Accept the local certificate warning if your browser shows one.

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
- [ ] Security Onion installed
- [ ] Lab network created
- [ ] Metasploitable isolated from internet
- [ ] IP addresses recorded
- [ ] Kali can reach Metasploitable
- [ ] Security Onion web interface is accessible
- [ ] Clean snapshots created

