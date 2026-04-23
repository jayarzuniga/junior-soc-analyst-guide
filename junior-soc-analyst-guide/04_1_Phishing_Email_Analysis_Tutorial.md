# Phishing Email Analysis: Comprehensive Tutorial & Practice

## 📌 Overview

This guide provides a detailed breakdown of email components, how to analyze each part for phishing indicators, and 6+ realistic practice emails with complete analysis explanations.

---

## 📧 Understanding Email Structure

### Complete Email Anatomy

```
┌─────────────────────────────────────────────────────┐
│ FROM FIELD                                          │
│ (sender@example.com)                                │
├─────────────────────────────────────────────────────┤
│ TO FIELD                                            │
│ (recipient@yourcompany.com)                         │
├─────────────────────────────────────────────────────┤
│ CC/BCC                                              │
│ (other recipients)                                  │
├─────────────────────────────────────────────────────┤
│ SUBJECT LINE                                        │
│ (Email subject)                                     │
├─────────────────────────────────────────────────────┤
│ DATE/TIME SENT                                      │
│ (Timestamp)                                         │
├─────────────────────────────────────────────────────┤
│ EMAIL HEADERS                                       │
│ (SPF, DKIM, DMARC, Authentication Results)         │
├─────────────────────────────────────────────────────┤
│ EMAIL BODY                                          │
│ (Message content, links, images)                    │
├─────────────────────────────────────────────────────┤
│ ATTACHMENTS                                         │
│ (Files: name, type, size)                           │
├─────────────────────────────────────────────────────┤
│ SIGNATURE/FOOTER                                    │
│ (Sender details, company info)                      │
└─────────────────────────────────────────────────────┘
```

---

## 🔍 Detailed Email Component Analysis Guide

### 1. FROM FIELD (Sender Address)

**What to Check:**

✅ **Domain Verification**
```
LEGITIMATE:  john.smith@microsoft.com
PHISHING:    john.smith@microsft.com       (typo: ft vs ft)
PHISHING:    john.smith@microsoft.com-verify.com  (looks similar)
PHISHING:    john.smith@mail.microsoft.com.fake.com
```

✅ **Display Name vs. Actual Address**
```
Display Name: "Microsoft Security Team" <support@microsoft.com>
Real Email:   <scammer@phishing-domain.com>
```

**Red Flags:**
- ❌ Domain spelling is slightly off
- ❌ Domain uses suspicious TLD (.xyz, .tk, .ga, .online)
- ❌ Display name doesn't match email domain
- ❌ Generic email provider for official company (Gmail/Yahoo for bank)
- ❌ No company domain at all
- ❌ Recently registered domain (check WHOIS)

**Green Flags:**
- ✅ Matches company official domain
- ✅ Display name matches organization
- ✅ Domain has good reputation (established company)
- ✅ Professional email structure

---

### 2. RECIPIENT FIELD (To/Cc/Bcc)

**What to Check:**

✅ **Is the email addressed to you personally?**
```
LEGITIMATE:  To: john.johnson@company.com
PHISHING:    To: undisclosed-recipients@company.com
PHISHING:    To: user@company.com  (generic, BCC'd to many)
```

✅ **Cc/Bcc Usage**
```
LEGITIMATE:  Cc: relevant.team@company.com
PHISHING:    No Cc: (sent only to you, many others BCC'd)
PHISHING:    Bcc: many users  (hidden recipients = mass phishing)
```

**Red Flags:**
- ❌ Generic greeting ("Dear Valued Customer" instead of name)
- ❌ No personalization (you're one of many in BCC)
- ❌ Generic recipient field
- ❌ Sent to many users at once

**Green Flags:**
- ✅ Addressed to you personally by name
- ✅ You're in To: field (direct communication)
- ✅ Relevant CC addresses visible
- ✅ Not a mass BCC

---

### 3. SUBJECT LINE

**What to Check:**

✅ **Urgency & Pressure Tactics**
```
PHISHING:    "Urgent: Verify Your Account NOW!!!"
PHISHING:    "Action Required - Account Will Be Closed"
PHISHING:    "CLICK HERE: Unusual Activity Detected"
PHISHING:    "Security Alert - Confirm Identity Immediately"

LEGITIMATE:  "Monthly Report Available"
LEGITIMATE:  "Meeting Confirmation: Tuesday at 2 PM"
LEGITIMATE:  "Your Invoice #12345"
```

✅ **Urgency Level Assessment**
```
🔴 CRITICAL URGENCY: "URGENT", "ACTION REQUIRED", "IMMEDIATELY"
🟡 MEDIUM URGENCY: "Please confirm", "Verify soon"
🟢 LOW URGENCY: "Information", "Update available"
```

✅ **Clarity & Legitimacy**
```
VAGUE:       "Your account needs attention"
VAGUE:       "Click here to claim your reward"
VAGUE:       "Verify your information"

CLEAR:       "May 2026 Paycheck Deposited"
CLEAR:       "Quarterly Budget Report - Q2 2026"
CLEAR:       "Scheduled System Maintenance - April 24"
```

**Red Flags:**
- ❌ ALL CAPS with multiple exclamation marks
- ❌ Words like "URGENT", "VERIFY", "CONFIRM", "ACT NOW"
- ❌ Threat of account closure/suspension
- ❌ Fear-based language
- ❌ Generic subject line
- ❌ Too vague or too detailed

**Green Flags:**
- ✅ Clear, specific subject matter
- ✅ Professional tone
- ✅ Relevant to your business
- ✅ No artificial urgency
- ✅ Specific dates/details

---

### 4. DATE & TIME

**What to Check:**

✅ **Timestamp Verification**
```
LEGITIMATE:  
  Sent: Monday, April 21, 2026 9:30 AM EST
  (Normal business hours, matches when shown in email)

PHISHING:
  Sent: Sunday, April 20, 2026 3:45 AM EST
  (Unusual time, outside business hours for official company)
```

✅ **Check Against Context**
```
"We noticed suspicious activity at 3:45 AM on your account"
BUT: Email sent at 3:47 AM - immediate response = suspicious
```

**Red Flags:**
- ❌ Email sent at unusual hours (3 AM, 2 AM)
- ❌ Time doesn't match content context
- ❌ No date/time visible
- ❌ Date mismatches (says Monday, actually sent Tuesday)

**Green Flags:**
- ✅ Business hours (8 AM - 6 PM)
- ✅ Matches company timezone
- ✅ Logical timing for content
- ✅ Date/time consistent with message

---

### 5. EMAIL HEADERS (CRITICAL)

**What to Check:**

✅ **SPF (Sender Policy Framework)**
```
PASS:        SPF PASS
             This means sender's IP is authorized by domain

FAIL:        SPF FAIL
             This means sender is NOT authorized (🚨 RED FLAG)

NEUTRAL:     SPF NEUTRAL
             Domain didn't set SPF rules
```

✅ **DKIM (DomainKeys Identified Mail)**
```
PASS:        DKIM PASS
             Email signature is valid

FAIL:        DKIM FAIL
             Email was modified in transit (🚨 RED FLAG)

NONE:        DKIM NONE
             Not signed with DKIM
```

✅ **DMARC (Domain-based Message Authentication)**
```
PASS:        DMARC PASS
             Email passed authentication

FAIL:        DMARC FAIL
             Email failed DMARC policy (🚨 RED FLAG)

QUARANTINE:  Message queued for review
```

**How to View Email Headers:**

**Gmail:**
1. Open email
2. Click three dots (⋯) menu
3. Select "Show original"
4. Look for "SPF:", "DKIM:", "DMARC:" lines

**Outlook:**
1. Open email
2. Go to File → Properties
3. Find "Internet Headers" section

**Apple Mail:**
1. Right-click email
2. Select "View Message"
3. Look for "Received" headers

**Example Header (LEGITIMATE):**
```
Received: from mail.google.com ([142.251.32.229]) 
          by mx.company.com with SMTP id a1234567890b;
Authentication-Results: mx.company.com;
       dkim=pass header.d=google.com header.s=20210112;
       dmarc=pass (p=NONE sp=QUARANTINE fo=1) header.from=google.com;
       spf=pass (google.com: domain of noreply@google.com 
       designates 142.251.32.229 as permitted sender)
```

**Example Header (PHISHING):**
```
Received: from unknown.server ([125.109.145.200])
Authentication-Results: mx.company.com;
       dkim=fail header.d=bank.fake header.s=201904;
       dmarc=fail (p=REJECT sp=REJECT fo=1) 
       header.from=bank-security.fake;
       spf=fail (bad.domain: domain of security@bank-security.fake 
       does not designate 125.109.145.200 as permitted sender)
```

**Red Flags:**
- ❌ SPF FAIL
- ❌ DKIM FAIL
- ❌ DMARC FAIL
- ❌ Authentication-Results: NONE/MISSING
- ❌ Received from suspicious IP
- ❌ Many "hops" suggesting forwarding

**Green Flags:**
- ✅ SPF PASS
- ✅ DKIM PASS
- ✅ DMARC PASS
- ✅ Received directly from organization
- ✅ Professional mail server

---

### 6. EMAIL BODY CONTENT

**What to Check:**

✅ **Grammar & Spelling**
```
PHISHING:    "Please to verify your account informations..."
PHISHING:    "We need confirm your identitty immediately"
PHISHING:    "Click here for more detials"

LEGITIMATE:  Proper English, professional grammar
```

✅ **Greeting & Personalization**
```
PHISHING:    "Dear Valued Customer"
PHISHING:    "Dear User"
PHISHING:    "Hello Sir/Madam"

LEGITIMATE:  "Hi John" / "Dear Mr. Smith"
LEGITIMATE:  "Hello Sarah,"
```

✅ **Content Authority & Knowledge**
```
PHISHING:    "Verify your bank account details"
             (Generic bank reference, no specific bank named)

LEGITIMATE:  "Your Chase Bank account #****5678..."
             (Specific details, account number masked appropriately)
```

✅ **Call to Action (CTA)**
```
PHISHING:    "Click here to verify"
PHISHING:    "Update payment information"
PHISHING:    "Confirm your identity"
PHISHING:    "Re-authenticate your account"

LEGITIMATE:  "View your statement"
LEGITIMATE:  "Download your invoice"
LEGITIMATE:  "Schedule a meeting"
```

**Red Flags:**
- ❌ Poor grammar/spelling (non-native English)
- ❌ Generic greeting
- ❌ Vague references to accounts/services
- ❌ Pressure/urgency language
- ❌ Threats of action
- ❌ Requests for sensitive info (passwords, SSN, card details)
- ❌ Long block of text with small font

**Green Flags:**
- ✅ Professional tone
- ✅ Proper grammar
- ✅ Specific details (account numbers masked)
- ✅ Clear purpose
- ✅ No requests for sensitive data
- ✅ Properly formatted
- ✅ References to company policies

---

### 7. LINKS & URLS

**What to Check (WITHOUT CLICKING):**

✅ **Hover Over Links (Desktop)**
```
PHISHING:    Hover shows: "https://bank-verify.com/confirm"
             But link says: "Click here to verify"
             
LEGITIMATE:  Hover shows: "https://chase.com/accounts"
             Link matches text: "View Account Statement"
```

✅ **URL Components Analysis**
```
URL Structure:
https://[SUBDOMAIN].[DOMAIN].[TLD]/[PATH]?[PARAMETERS]

LEGITIMATE:  https://mail.google.com/mail/u/0/#inbox
             Domain: google.com (official)

PHISHING:    https://mail.google.com-verify-account.tk/login
             Domain: google.com-verify-account.tk (FAKE!)
             
PHISHING:    https://192.168.1.1/banking/verify
             No domain name, just IP address (RED FLAG!)
```

✅ **Suspicious URL Patterns**
```
🚨 RED FLAGS:

1. IP ADDRESS instead of domain:
   https://125.109.145.200/paypal/login
   
2. LONG SUBDOMAIN chain:
   https://mail.verify.confirm.google.fake.com
   
3. EXTRA dots or dashes:
   https://goo-gle.com
   https://g00gle.com
   https://go.og.le.com
   
4. MISSPELLED domain:
   https://facbook.com (missing 'e')
   https://amaz0n.com ('0' instead of 'o')
   
5. URL SHORTENER (you can't see real destination):
   https://tinyurl.com/xyz123
   https://bit.ly/abc456
   
6. WEIRD PORT number:
   https://paypal.com:8080/login
   https://bank.com:9999/verify
   
7. AUTHENTICATION IN URL:
   https://user:password@example.com (RED FLAG!)
   https://admin:123@badsite.com
```

✅ **Safe Link Checking Tools**
```
Without clicking the link, use:

1. URLhaus: https://urlhaus.abuse.ch/
2. VirusTotal: https://www.virustotal.com/
3. URLScan: https://urlscan.io/
4. AbuseIPDB: https://www.abuseipdb.com/
5. Google Safe Browsing: https://www.google.com/safebrowsing
6. PhishTank: https://www.phishtank.com/

Steps:
1. Copy the full URL (don't click)
2. Paste into one of above tools
3. Check if URL is marked as malicious
4. Read comments from other users
```

**Red Flags:**
- ❌ Link text doesn't match hover destination
- ❌ IP address instead of domain
- ❌ Misspelled domain
- ❌ Unusual subdomains
- ❌ URL shortener
- ❌ Weird port numbers
- ❌ Authentication in URL

**Green Flags:**
- ✅ Link matches hover text
- ✅ Domain matches company
- ✅ Professional URL structure
- ✅ HTTPS (secure protocol)
- ✅ Clean, readable URL

---

### 8. ATTACHMENTS

**What to Check:**

✅ **Filename Analysis**
```
SUSPICIOUS:           LEGITIMATE:
invoice.exe           invoice.pdf
document.scr          document.docx
image.jpg.exe         image.jpg
payment.zip           statement.xlsx
form.bat              form.docx
```

✅ **File Type Verification**
```
DANGEROUS FILE TYPES:
.exe  - Executable file (CAN INSTALL MALWARE)
.scr  - Screensaver (CAN RUN CODE)
.bat  - Batch file (CAN RUN COMMANDS)
.cmd  - Command file (CAN RUN COMMANDS)
.com  - Command file (CAN RUN CODE)
.msi  - Windows installer (CAN INSTALL PROGRAMS)
.zip  - Archive (COULD CONTAIN MALWARE)
.rar  - Archive (COULD CONTAIN MALWARE)
.7z   - Archive (COULD CONTAIN MALWARE)
.jar  - Java archive (CAN RUN CODE)
.vbs  - VB Script (CAN RUN CODE)
.ps1  - PowerShell (CAN RUN CODE)
.js   - JavaScript (CAN RUN CODE)

SAFER FILE TYPES (but still risky):
.pdf  - Document (could have malicious scripts)
.doc  - Word document (could have macros)
.xls  - Excel (could have macros)
.ppt  - PowerPoint (could have macros)
.txt  - Text (generally safe)
.jpg  - Image (generally safe, but verify)
.png  - Image (generally safe, but verify)
```

✅ **Double Extensions (Critical Red Flag)**
```
DANGEROUS:
- invoice.pdf.exe     (Looks like PDF, actually EXE!)
- statement.xlsx.zip  (Looks like spreadsheet, actually ZIP!)
- image.jpg.scr       (Looks like image, actually SCREENSAVER!)
```

✅ **Attachment Scanning**
```
Don't download! Instead:

1. Ask sender if they sent attachment (call them)
2. Use VirusTotal to scan the file:
   - Right-click file → Get File Hash
   - Go to https://www.virustotal.com/
   - Upload file or paste hash
   - Check scan results

3. Use email gateway scanning (if available in org)
```

**Red Flags:**
- ❌ Unexpected attachment
- ❌ Dangerous file type (.exe, .bat, .scr, .zip)
- ❌ Double extension
- ❌ File you didn't request
- ❌ Large file from unknown sender
- ❌ Attachment from external sender claiming to be internal

**Green Flags:**
- ✅ Expected attachment
- ✅ Safe file type (.pdf, .txt, .docx from trusted source)
- ✅ Matches email content
- ✅ From known sender
- ✅ Reasonable file size

---

### 9. SIGNATURE & FOOTER

**What to Check:**

✅ **Professional Signature**
```
LEGITIMATE:
John Smith
Senior Software Engineer
Microsoft Corporation
1 Microsoft Way, Redmond, WA 98052
Phone: (425) 882-8080
john.smith@microsoft.com

PHISHING:
Support Team
Bank Security
[No contact info, vague signature]

PHISHING:
Click here for help
[No name, no company contact]
```

✅ **Contact Information Verification**
```
LEGITIMATE:
- Real phone number with area code
- Official company address
- Known department/title
- Official company email

PHISHING:
- Generic phone number (generic "1-800" numbers)
- No physical address
- Vague title
- Free email provider (@gmail.com, @yahoo.com)
```

✅ **Footer Links**
```
LEGITIMATE:
[Unsubscribe] [Contact Us] [Privacy Policy]
All links go to company domains

PHISHING:
[Unsubscribe] [Update Info] [Verify Account]
Links go to suspicious domains
```

**Red Flags:**
- ❌ No signature
- ❌ Vague signature with no contact info
- ❌ No company affiliation
- ❌ Generic footer
- ❌ Free email provider for official business

**Green Flags:**
- ✅ Professional signature with full details
- ✅ Real phone number
- ✅ Company address
- ✅ Official company email
- ✅ Professional titles

---

## 📋 Email Analysis Checklist

Use this checklist when analyzing ANY email:

```
FROM FIELD:
[ ] Domain spelling correct
[ ] Display name matches domain
[ ] Not a free provider for official business
[ ] Known/trusted sender

RECIPIENT:
[ ] Addressed to me personally
[ ] In TO: field (not BCC'd)
[ ] Not a generic greeting
[ ] Makes sense for the content

SUBJECT LINE:
[ ] Clear and specific
[ ] No artificial urgency
[ ] Not threatening
[ ] Relevant to my work/account

DATE & TIME:
[ ] Business hours (or reasonable)
[ ] Matches email content
[ ] Not suspiciously quick response time

HEADERS:
[ ] SPF PASS
[ ] DKIM PASS
[ ] DMARC PASS
[ ] From authorized server

BODY:
[ ] Professional grammar
[ ] Personalized greeting
[ ] Specific details (not vague)
[ ] No requests for sensitive data
[ ] No pressure/urgency language

LINKS:
[ ] Hover text matches link
[ ] Domain matches content
[ ] No misspellings
[ ] HTTPS protocol
[ ] Not shortened URLs

ATTACHMENTS:
[ ] Expected and relevant
[ ] Safe file type
[ ] From trusted sender
[ ] No double extensions

SIGNATURE:
[ ] Professional and complete
[ ] Contact information present
[ ] Company affiliation clear
[ ] Known department/title
```

**Assessment Result:**
- ✅ 15-16 checks = LEGITIMATE
- 🟡 10-14 checks = INVESTIGATE FURTHER
- ❌ 0-9 checks = LIKELY PHISHING

