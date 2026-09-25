# Important Rules Before You Start

- This is **not** your personal computer.
- Do not save personal files, change any settings, or install software unless the activity says so.
- Everything you create must be inside your personal folder on `D:\`.
- This keeps other students' work safe and follows lab rules.
- Do not change any system settings such as Wi-Fi, firewall, or Windows Update.
- If you are unsure about a step, ask your professor or trainer before continuing.

> Insert here

## Step 1 - Create Your Personal Folder on Drive D

1. Open **File Explorer**.
   You can click the folder icon on the taskbar or press `Win + E`.
2. Click **This PC** in the left sidebar, then double-click **Local Disk (D:)**.
3. Right-click on an empty space inside `D:\`, then choose **New -> Folder**.
4. Name the folder exactly your **last name**.
   Example: `Garcia`
5. Use only letters.
   Do not use spaces or special characters.
6. All files, VMs, and downloads for this course must go inside this folder.

> Insert here

## Step 2 - Get the Download URL from Your Professor

1. Your professor or trainer will give you a URL where the required files are stored.
2. Open **Microsoft Edge** or **Google Chrome**.
3. Type or paste the URL into the address bar, then press `Enter`.

## Step 3 - Download and Import Kali Linux

1. On the professor's page, find and download the **Kali Linux** file.
   It will be a `.7z` file.
2. Wait for the download to finish.
   This can take several minutes.
3. Locate the downloaded file, usually in the **Downloads** folder.
4. Move it to your personal folder on `D:\`.
   - Right-click the file -> **Cut**
   - Go to `D:\YourLastName`
   - Right-click -> **Paste**
5. Unzip the file.
   - Right-click the `.7z` file -> **Extract All**
   - Choose `D:\YourLastName\Kali` or the default location
   - Click **Extract**
6. Inside the extracted folder, look for a file ending in `.ova`.
7. Double-click the `.ova` file.
8. VirtualBox should open automatically and ask to import the appliance.
9. Click **Import** and keep the default settings.
10. Wait for the import to finish.

> Insert here

## Step 4 - Configure Kali Linux Settings

1. In VirtualBox, select the **Kali** VM.
   Do **not** start it yet.
2. Click **Settings**.
3. Go to **System -> Motherboard**.
   Set **Base Memory** to `4096 MB`.
4. Go to **Network**.
5. Under **Adapter 1**:
   - Make sure it is **Enabled**
   - Set **Attached to**: `NAT`
6. Click the **Adapter 2** tab.
   - Check **Enable Network Adapter**
   - Set **Attached to**: `Internal Network`
   - Set **Name** to `intnet`
   - Do not change the name unless instructed
7. If there is an **Adapter 3**, disable it.
8. Click **OK** to save.

## Step 5 - Download and Set Up Metasploitable

1. From the professor's URL, download the **Metasploitable** file.
   It will be a `.zip` containing a `.vmdk` file.
2. Move the downloaded file to `D:\YourLastName\Metasploitable`.
3. Unzip it inside that folder.
4. In VirtualBox, click **New**.
5. Use these settings:

| Setting | Value |
| --- | --- |
| Name | `Metasploitable` |
| Folder | `D:\YourLastName\Metasploitable` |
| ISO Image | Leave empty |
| Type | `Linux` |
| Version | `Other Linux (64-bit)` |

6. Click **Next**.
7. Set **Memory size** to `1024 MB`, then click **Next**.
8. For **Hard disk**, choose **Use an existing virtual hard disk file**.
9. Click the small folder icon, then:
   - Click **Add**
   - Browse to the unzipped `.vmdk` file
   - Click **Open**
   - Select it
   - Click **Choose**
10. Click **Next**, then **Finish**.
11. With **Metasploitable** selected, click **Settings -> Storage**.
12. If you see any other hard disk such as a `.vdi` file, remove it.
   Only the `.vmdk` should remain.
13. Configure the network settings:
   - **Adapter 1**: Enable -> `Internal Network` -> name `intnet`
   - **Adapter 2**: Disable
   - **Adapter 3**: Disable
14. Click **OK**.

> Insert here

## Step 6 - Download and Set Up Security Onion

1. From the professor's URL, download the **Security Onion** ISO file.
   Example: `securityonion.iso`
2. Move it to `D:\YourLastName\SecurityOnion`.
3. In VirtualBox, click **New**.
4. Use these settings:

| Setting | Value |
| --- | --- |
| Name | `SecurityOnion` |
| Folder | `D:\YourLastName\SecurityOnion` |
| ISO Image | Choose the downloaded `.iso` file |
| Type | `Linux` |
| Version | `Other Linux (64-bit)` |

5. Click **Next**.
6. Set **Memory size** to `8192 MB`, then click **Next**.
7. For **Hard disk**, create a new virtual disk.
   The default size is fine. `20 GB` is acceptable.
8. Click **Next**, then **Finish**.
9. Configure the two network adapters:
   - **Adapter 1**: Enable -> `Bridged Adapter`
   - **Name**: Select the network adapter connected to the live network with DHCP
   - **Adapter 2**: Enable -> `Internal Network` -> name `intnet`
10. Expand **Advanced** under Adapter 2.
11. Set **Promiscuous Mode** to `Allow All`.

Why?
This allows Security Onion to see traffic between Kali and Metasploitable.

12. Click **OK**.

## Step 7 - Install Security Onion (Evaluation Mode)

Before you start, make sure:

- the **Security Onion** VM is selected in VirtualBox
- the ISO is still in the virtual CD/DVD drive
- the network adapters are set as instructed

### Part A - First Boot and Installer Start

1. Start the **Security Onion** VM.
   In VirtualBox, select **SecurityOnion** and click **Start**.
2. During installation, when prompted with `All data will be lost...`
   Type `yes`, then press `Enter`.
3. Enter the following administrative account details:

| Prompt | Value |
| --- | --- |
| Administrative username | `admin` |
| Password | `admin1234` |
| Re-enter password | `admin1234` |

4. After installation completes, press `Enter` to reboot.

### Part B - Post-Reboot Setup

1. After reboot, log in locally using:

| Field | Value |
| --- | --- |
| Username | `admin` |
| Password | `admin1234` |

2. When asked whether to continue setup, select **Yes**.
3. For **Select an option**, choose `install`.
4. For **What kind of installation would you like to do?**, choose `eval`.
5. When prompted, enter `AGREE`, then press `Enter`.
6. Select `Standard`, then press `Enter`.
7. For hostname, keep the default:
   `securityonion`
8. If warned about hostname conflicts, choose **Use Anyway**.
9. For management NIC, select the first interface:
   `enp0s3`
10. For management interface setup, select `Static`.
11. For Internet connection type, select `Direct`.
12. When asked about the default Docker IP range, select **Yes**.
13. For the monitor interface, select the remaining NIC:
   `enp0s8`
14. Press the space bar to select it, then click **OK**.
15. When asked for an email address for the Security Onion web interface, enter:
   `admin@securityonion.com`
16. Set the web interface password:

| Prompt | Value |
| --- | --- |
| Password | `admin1234` |
| Re-enter password | `admin1234` |

17. For web interface access method, select `IP`.
18. When asked if you want to allow access via the web interface, select **Yes**.
19. When prompted for an allowed IP or IP range, enter:
   `0.0.0.0/0`

Use this only for lab environments. It allows all IPv4 addresses.

20. For **Enable SOC Telemetry**, select **No**.
21. When asked whether to proceed with the selected options, press `Tab` until **Yes** is highlighted, then press `Enter`.
22. When prompted that `EVAL setup is not complete...`, press `Tab` until **OK** is highlighted, then press `Enter`.

## Step 8 - Boot Kali and Set Static IP on the Second Interface

1. Start the **Kali** VM.
2. Log in using the default credentials unless they were changed:

| Field | Value |
| --- | --- |
| Username | `kali` |
| Password | `kali` |

3. Open a terminal.
4. Run the following command to view your network interfaces:

```bash
ip a
```

You should see `eth0` for NAT and `eth1` for the internal network.

5. Create or edit the configuration file for `eth1`:

```bash
sudo nano /etc/network/interfaces
```

6. Add these lines at the end of the file:

```ini
auto eth1
iface eth1 inet static
    address 10.10.1.10
    netmask 255.255.255.0
```

7. Save and exit:
   - `Ctrl + O`
   - `Enter`
   - `Ctrl + X`
8. Restart the network:

```bash
sudo systemctl restart networking
```

9. Verify the IP address:

```bash
ip a show eth1
```

You should see `10.10.1.10`.

> Insert here

## Step 9 - Boot Metasploitable and Set Static IP

Do this every time you start Metasploitable.

1. Start the **Metasploitable** VM.
2. Log in using:

| Field | Value |
| --- | --- |
| Username | `msfadmin` |
| Password | `msfadmin` |

3. Run:

```bash
sudo ifconfig eth0 10.10.1.20 netmask 255.255.255.0 up
```

4. Check that the interface has the IP:

```bash
sudo ifconfig eth0
```

You should see the IP address assigned to that interface.

## Step 10 - Test Communication (Ping)

1. In the **Kali** terminal, run:

```bash
ping 10.10.1.20
```

2. You should see replies similar to:
   `64 bytes from 10.10.1.20...`
3. Press `Ctrl + C` to stop.

If there is no reply, double-check:

- both VMs are running
- both have the correct IP addresses
- Kali Adapter 2 and Metasploitable Adapter 1 are both on `Internal Network` with name `intnet`

> Insert here

## Step 11 - Scan Metasploitable with Nmap (from Kali)

1. In the **Kali** terminal, run:

```bash
nmap -sV 10.10.1.20
```

2. Wait for the scan to finish.
   This usually takes 30 to 60 seconds.
3. You should see a list of open ports and service versions such as:
   - port `21` FTP
   - port `22` SSH
   - and other discovered services

## Step 12 - View the Activity in the Security Onion Web Interface

### Find the Security Onion Bridge Interface Address

1. In the **Security Onion** VM, open a terminal.
2. Run `ip a` and look for the interface with an address such as `192.168.56.x`.
   This is usually `eth1` or `enp0s3`.
3. Example:
   `192.168.56.101`
4. You can also run:

```bash
ip route get 1 | awk '{print $7}'
ifconfig enp0s3
```

### Open the Web Interface from Windows

1. On your Windows 11 host, open **Edge** or **Chrome**.
2. Enter the Security Onion address in the browser:

```text
https://192.168.56.101
```

Replace `192.168.56.101` with the actual IP address of your Security Onion VM.

3. Accept the browser security warning.
   The certificate is self-signed.
4. Log in using the Security Onion credentials you created during installation.

### Find the Nmap Scan Events

1. Inside the Security Onion web interface, look for **Kibana** or **Elasticsearch**.
2. Open **Discover** or **Dashboards**.
3. In the search bar, type:

```text
host: 10.10.1.20 and port: <any port>
```

4. Or use a ready-made dashboard such as **Network Alerts** or **Suricata Alerts**.
5. Set the time range to **Last 15 minutes**.
6. You should see events such as:
   - `ET SCAN NMAP`
   - `ET SCAN Suspicious inbound`

This confirms that Security Onion detected the scan.

Tip:
If you see nothing, wait 2 minutes and refresh. The internal interface promiscuous mode must be working. Ask your professor to verify that the Security Onion monitor interface is correctly set to `intnet`.

> Insert here

## Reminder for Shared PC

- Do not leave VMs running when you finish. Shut them down properly.
- Do not change passwords, network settings, or install tools outside the lab.
- Do not delete any file that belongs to another student.
- When the activity is over, your professor may ask you to export your VM or simply leave it in your folder.
- If anything is unclear, stop and ask your trainer. It is better to ask than to break the shared environment.

> Insert here

## Submission Instructions - Proof of Completion (Steps 1-12)

**What to submit:** A single document in PDF format containing screenshots and text answers as listed below.  
**File name format:** `LastName_Day1_Installation.pdf`  
**Submission method:** Upload to the assignment link provided by your professor or trainer.

## Required Evidence for Each Step

| Step | What to Show | How to Capture It |
| --- | --- | --- |
| Step 1 | Screenshot of File Explorer showing `D:\YourLastName` folder with all VM folders inside (`Kali`, `Metasploitable`, `SecurityOnion`) | Press `Win + PrtScn`, then crop the image to show only the relevant window |
| Step 2 | Not required; no permanent change to capture | - |
| Step 3 | Screenshot of VirtualBox Manager showing the Kali Linux VM in the left list | In the VirtualBox main window, press `Alt + PrtScn` |
| Step 4 | Screenshot of Kali **Settings -> Network** showing Adapter 1 = NAT and Adapter 2 = Internal Network | In VirtualBox, select Kali -> **Settings -> Network** |
| Step 5 | Screenshot of Metasploitable **Settings -> Storage** showing the `.vmdk` attached and **Network** showing Adapter 1 = Internal Network | Two screenshots: Storage and Network |
| Step 6 | Screenshot of Security Onion **Settings -> Network** showing all 3 adapters and Adapter 2 Advanced with **Promiscuous Mode = Allow All** | Scroll as needed so the Advanced section is visible |
| Step 7 | Screenshot of the Security Onion terminal after reboot showing (a) successful login and (b) `ip a show eth1` displaying `PROMISC` | Two screenshots: one for login, one for the interface output |
| Step 8 | Screenshot of the Kali terminal after `ip a show eth1` showing IP address `10.10.1.10` | Kali terminal window |
| Step 9 | Screenshot of the Metasploitable terminal after `ifconfig` showing IP address `10.10.1.20` | Metasploitable terminal |
| Step 10 | Screenshot of the Kali terminal showing successful `ping 10.10.1.20` output with at least 3 reply lines | Make sure the command and replies are visible |
| Step 11 | Screenshot of the Kali terminal showing `nmap -sV 10.10.1.20` output with open ports listed | Include the command and at least the first 10 lines of results |
| Step 12 | (a) Screenshot of the Security Onion web interface logged in and (b) screenshot showing search results for `host: 10.10.1.20` with an alert such as `ET SCAN NMAP` | Make sure the URL and search bar are visible |

## Written Answers

Answer these in the same document after your screenshots:

1. What command did you use in Kali to set the static IP on the second interface?
2. What does `PROMISC` mean in the output of `ip a show eth1` on Security Onion?
3. List any three open ports you saw on Metasploitable from the Nmap scan.
4. In Security Onion's web interface, what alert signature name appeared for your Nmap scan?

## Important Reminders Before Submitting

- Do **not** submit raw screenshot files. Combine everything into one PDF.
  You can use Word's **Save as PDF** feature.
- Blur or black out any personal information such as your Windows username if it appears in File Explorer.
- Name your file exactly as:
  `LastName_Day1_Installation.pdf`
- Example:
  `Garcia_Day1_Installation.pdf`
- If any screenshot is missing or unclear, your submission will be marked incomplete and returned for resubmission.
