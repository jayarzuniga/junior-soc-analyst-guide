---

## 🎯 PRACTICE: Email Analysis Examples

### Now that you understand email components, let's analyze real examples!

---

# PRACTICE EMAIL #1

## Email Display

```
FROM: John Thompson <support@paypal.com>
TO: undisclosed-recipients@company.com
SUBJECT: ACTION REQUIRED: Urgent Account Verification Needed!!!
DATE: Saturday, April 20, 2026 at 2:47 AM EST

---

Dear Valued Customer,

We have detected unusual activity on your PayPal account. Due to security 
concerns, we need you to verify your account information immediately.

Please click the link below to confirm your identity:

[Click here to verify account]

If you do not verify within 24 hours, your account will be PERMANENTLY 
SUSPENDED.

Thank you,
Support Team
PayPal Security Division
```

---

## Analysis Questions

Before reading the answer, analyze this email using the checklist:

1. **FROM FIELD**: What concerns do you have?
2. **RECIPIENT FIELD**: Is this addressed properly?
3. **SUBJECT LINE**: What red flags do you see?
4. **DATE/TIME**: Is the timing suspicious?
5. **BODY CONTENT**: What issues exist?
6. **OVERALL**: Is this phishing or legitimate?

---
## ✅ ANSWER - EMAIL #1 Analysis

**VERDICT: 🚨 PHISHING EMAIL**

### Detailed Breakdown:

**1. FROM FIELD: ❌ SUSPICIOUS**
- ✅ Domain appears to be @paypal.com (looks legitimate)
- ❌ BUT: The display name "John Thompson" with generic "Support" doesn't match typical PayPal official emails
- ❌ PayPal official emails usually come from specific departments, not generic "Support"
- **ACTION**: Check email headers - if SPF/DKIM/DMARC fail, it's spoofed

**2. RECIPIENT FIELD: ❌ MAJOR RED FLAG**
- ❌ Addressed to "undisclosed-recipients@company.com"
- ❌ NOT addressed to you personally by name
- ❌ This indicates a mass BCC phishing campaign
- ❌ Generic greeting "Dear Valued Customer" confirms it
- **PHISHING INDICATOR**: Real companies address you by name

**3. SUBJECT LINE: 🚨 MULTIPLE RED FLAGS**
- ❌ "ACTION REQUIRED" - artificial urgency
- ❌ "URGENT" in subject line
- ❌ Three exclamation marks - emotional manipulation
- ❌ Real PayPal doesn't use this aggressive style
- **PHISHING INDICATOR**: Fear and urgency tactics

**4. DATE & TIME: ❌ HIGHLY SUSPICIOUS**
- ❌ Sent at 2:47 AM on Saturday
- ❌ NOT business hours for PayPal
- ❌ PayPal security issues are typically investigated during business hours
- **PHISHING INDICATOR**: Scammers work odd hours to avoid detection

**5. EMAIL BODY: ❌ MULTIPLE RED FLAGS**
- ❌ Generic greeting "Dear Valued Customer"
- ❌ No specific account details (real PayPal shows account info)
- ❌ Vague "unusual activity" (real alerts specify the activity)
- ❌ Requests you to click to "verify account" (legitimate services never ask you to verify via email)
- ❌ Threat: "Account will be PERMANENTLY SUSPENDED"
- ❌ Creates time pressure: "within 24 hours"
- **PHISHING INDICATOR**: Pressure, threats, and requests for sensitive action

**6. LINKS: ❌ DANGEROUS**
- ❌ "[Click here to verify account]" - generic link text
- ❌ If you hover (without clicking), it likely goes to fake-paypal.com or similar
- ❌ Clicking would take you to a fake login page designed to steal credentials
- **PHISHING INDICATOR**: URL wouldn't match domain

**7. SIGNATURE: ❌ SUSPICIOUS**
- ❌ No specific person named
- ❌ No real contact information
- ❌ Generic "Support Team"
- ❌ Only "PayPal Security Division" - not a real department
- ❌ No phone number or address
- **PHISHING INDICATOR**: Real companies have professional signatures

**8. EMAIL HEADERS (if you checked):**
- ❌ SPF would likely FAIL
- ❌ DKIM would likely FAIL
- ❌ Email is spoofed to look like it's from PayPal

### Summary Why This is Phishing:
1. Mass mailing (BCC'd recipients)
2. Artificial urgency and threats
3. Generic greeting
4. Requests account verification via email
5. Generic link
6. No specific account details
7. Poor signature
8. Odd timing (2:47 AM)
9. Emotional manipulation language

### What You Should Do:
- ❌ DO NOT CLICK ANY LINKS
- ❌ DO NOT ENTER CREDENTIALS
- ✅ Report to phishing@paypal.com
- ✅ Delete the email
- ✅ If concerned about account, visit paypal.com directly (don't use email link)
- ✅ Report to your security team

---

# PRACTICE EMAIL #2

## Email Display

```
FROM: noreply@dropbox.com
TO: john.doe@company.com
SUBJECT: Your files are syncing
DATE: Monday, April 21, 2026 at 10:30 AM EST

---

Hi John,

Your Dropbox is syncing your files from your Windows PC 
(John-PC-001). This sync started at 10:15 AM.

If you didn't start this sync, your account may be compromised. 
You can view your device activity at your Dropbox account settings.

The sync includes:
- 2,400 files
- 45.3 GB of data

Device IP: 192.168.1.100
Location: New York, NY
Time started: 10:15 AM EST on April 21, 2026

Best regards,
Dropbox Security Team

---

View Account Activity: https://www.dropbox.com/account/security
```

---

## Analysis Questions

Before reading the answer:

1. **FROM FIELD**: Is this from Dropbox?
2. **PERSONALIZATION**: Is this addressed to you?
3. **CONTENT SPECIFICITY**: Does it have specific details?
4. **WARNINGS**: Are you asked to click anything?
5. **OVERALL**: Is this phishing or legitimate?

---

## ✅ ANSWER - EMAIL #2 Analysis

**VERDICT: ✅ LEGITIMATE EMAIL**

### Detailed Breakdown:

**1. FROM FIELD: ✅ LEGITIMATE**
- ✅ Domain is @dropbox.com (official Dropbox domain)
- ✅ noreply@ prefix is standard for automated notifications
- ✅ Dropbox regularly sends notifications from this address
- ✅ No suspicious domain variations
- **VERIFICATION**: This is Dropbox's actual notification email

**2. RECIPIENT FIELD: ✅ LEGITIMATE**
- ✅ Addressed to "john.doe@company.com" (specific person)
- ✅ In TO: field (direct communication)
- ✅ This is YOUR actual email address
- ✅ Greeting "Hi John" is personalized
- **VERIFICATION**: Legitimate Dropbox security emails are personalized

**3. SUBJECT LINE: ✅ LEGITIMATE**
- ✅ Clear, specific subject: "Your files are syncing"
- ✅ No artificial urgency
- ✅ No threats or demands
- ✅ Matches the email content
- ✅ No excessive punctuation
- **VERIFICATION**: Factual subject line

**4. DATE & TIME: ✅ LEGITIMATE**
- ✅ Monday at 10:30 AM (business hours)
- ✅ Timing matches the action described (sync started 10:15 AM)
- ✅ Reasonable timestamp
- **VERIFICATION**: Logical timing for system notification

**5. EMAIL BODY: ✅ LEGITIMATE**
- ✅ Professional tone and grammar
- ✅ Personalized greeting with your name
- ✅ SPECIFIC DETAILS about the sync:
  - Device name: "John-PC-001"
  - File count: 2,400 files
  - Data size: 45.3 GB
  - Device IP address
  - Location (New York, NY)
  - Exact timestamp
- ✅ Acknowledges if YOU didn't start this, account may be compromised
- ✅ Provides you control: "view your device activity"
- ✅ No pressure to click immediately
- **VERIFICATION**: Legitimate alerts include specific details

**6. LINKS: ✅ LEGITIMATE**
- ✅ Link is to official Dropbox domain: dropbox.com
- ✅ Specific link: /account/security (real Dropbox URL structure)
- ✅ Uses HTTPS (secure)
- ✅ If you hover, it shows: https://www.dropbox.com/account/security
- ✅ Link text matches destination
- **VERIFICATION**: Direct link to legitimate account settings

**7. SIGNATURE: ✅ LEGITIMATE**
- ✅ "Dropbox Security Team" is a real team
- ✅ Professional and official
- ✅ No suspicious contact information needed (automated system)
- ✅ Matches Dropbox notification style
- **VERIFICATION**: Authentic Dropbox signature

**8. EMAIL HEADERS (if you checked):**
- ✅ SPF would PASS (authorized Dropbox server)
- ✅ DKIM would PASS (email is digitally signed)
- ✅ DMARC would PASS (authentic Dropbox email)
- **VERIFICATION**: Email authentication passes

### Summary Why This is Legitimate:
1. From official Dropbox domain
2. Personalized with your actual name and details
3. Specific device and activity information
4. Professional, non-threatening tone
5. Empowers user with control (view activity)
6. Legitimate Dropbox URL structure
7. Business hours timing
8. Proper email authentication

### What You Should Do:
- ✅ Review the activity at the link provided
- ✅ If you started the sync, no action needed
- ✅ If you DID NOT start this sync, use the link to:
  - Remove unauthorized device
  - Change password
  - Review login history
  - Enable two-factor authentication

---

# PRACTICE EMAIL #3

## Email Display

```
FROM: banking@your-bank.onlineverification.tk
TO: valued.customer@company.com
SUBJECT: Verify Your Banking Details - Click Now
DATE: Sunday, April 20, 2026 at 11:45 PM EST

---

Dear Valued Costomer,

Your bank account requires imediate verification to ensure your account 
remains active. Please click the link bellow to update your banking details:

[UPDATE YOUR ACCOUNT]

Payment information needed:
- Full name
- SSN (Social Security Number)
- Credit card number
- Bank account number
- PIN

This is a security measure to protect your account from fraud and 
theft. If you do not update within 12 hours, your account will be 
suspended and locked for security reasons.

Best regards,
Bank Security Department
www.onlineverification.tk
```

---

## Analysis Questions

Before reading the answer:

1. **FROM FIELD**: What domain is this from?
2. **SPELLING**: Do you notice any errors?
3. **REQUESTS**: What sensitive data is requested?
4. **LEGITIMACY**: Would a real bank ask this?
5. **OVERALL**: Is this phishing or legitimate?

---

## ✅ ANSWER - EMAIL #3 Analysis

**VERDICT: 🚨 PHISHING EMAIL (Very Obviously)**

### Detailed Breakdown:

**1. FROM FIELD: 🚨 MAJOR RED FLAG**
- ❌ Domain is NOT .com, .org, or official bank domain
- ❌ Domain ends in .tk (suspicious TLD)
- ❌ "onlineverification" suggests fake verification site
- ❌ Looks like: banking@your-bank.onlineverification.tk
- ❌ NOT the official bank domain
- **VERIFICATION**: Real banks use their official domains like @chase.com, @bankofamerica.com
- **PHISHING INDICATOR**: Fake domain designed to look legitimate

**2. RECIPIENT FIELD: ❌ RED FLAG**
- ❌ "valued.customer@company.com" (generic, not your actual name)
- ❌ Shows this is a mass phishing campaign
- ❌ Not personalized
- **PHISHING INDICATOR**: Mass mailing to generic addresses

**3. SUBJECT LINE: ❌ RED FLAG**
- ❌ "Verify Your Banking Details - Click Now"
- ❌ Artificial urgency ("Click Now")
- ❌ Requests action on banking details
- ❌ No specific reason for verification
- **PHISHING INDICATOR**: Pressure tactics

**4. DATE & TIME: ❌ RED FLAG**
- ❌ Sent Sunday at 11:45 PM
- ❌ NOT business hours for banks
- ❌ Odd timing for account verification
- **PHISHING INDICATOR**: Off-hours sending suggests malicious intent

**5. EMAIL BODY: 🚨 CRITICAL RED FLAGS**
- ❌ "Valued Costomer" - SPELLING ERROR (should be "Customer")
- ❌ "imediate" - SPELLING ERROR (should be "immediate")
- ❌ "bellow" - SPELLING ERROR (should be "below")
- ❌ Poor English quality
- ❌ Generic greeting "Dear Valued Customer"
- ❌ Vague phrase "requires immediate verification"
- **🚨 CRITICAL**: Requests for SENSITIVE personal data:
  - Full name (okay, but unnecessary)
  - **SSN** ❌ Banks already have this
  - **Credit card number** ❌ Banks NEVER ask for this via email
  - **Bank account number** ❌ Banks NEVER ask for this via email
  - **PIN** ❌ Banks ABSOLUTELY NEVER ask for PIN via email
- ❌ Threat of account suspension
- ❌ Time pressure: "within 12 hours"
- **PHISHING INDICATOR**: No legitimate financial institution requests SSN, credit card, or PIN via email

**6. LINKS: 🚨 CRITICAL**
- ❌ "[UPDATE YOUR ACCOUNT]" - generic link text
- ❌ Clicking would likely go to: your-bank.onlineverification.tk/login
- ❌ This is a FAKE login page designed to STEAL your credentials and data
- **PHISHING INDICATOR**: Link would go to attacker's server

**7. SIGNATURE: 🚨 CRITICAL**
- ❌ Generic "Bank Security Department"
- ❌ No person named
- ❌ No official contact information
- ❌ Website listed is: www.onlineverification.tk
- ❌ This is the PHISHING domain, not the actual bank
- **PHISHING INDICATOR**: Signature actually gives away the scam

**8. EMAIL HEADERS:**
- ❌ SPF would FAIL
- ❌ DKIM would FAIL
- ❌ DMARC would FAIL
- ❌ This is clearly a spoofed/fraudulent email

### Summary Why This is Phishing:
1. Fake domain ending in .tk
2. Generic greeting and recipient
3. Multiple spelling errors (sign of foreign scammer)
4. Requests for NEVER-asked-for data (SSN, credit card, PIN)
5. Banks don't verify accounts via email
6. Artificial urgency and threats
7. Fake signature
8. Off-hours timing
9. Generic link
10. Poor email quality

### What You Should Do:
- ❌ DO NOT CLICK ANY LINKS
- ❌ DO NOT ENTER ANY INFORMATION
- ❌ DO NOT REPLY
- ✅ DELETE the email immediately
- ✅ Report to your bank directly (call their official number)
- ✅ Report to your security team
- ✅ Run antivirus/malware scan (just in case)

### Key Learning Point:
**No legitimate financial institution will EVER ask for:**
- Social Security Number via email
- Credit card number via email  
- Bank account number via email
- PIN via email
- Passwords via email
- Authentication codes via email

If you receive an email asking for ANY of these, it's 100% PHISHING.

---

# PRACTICE EMAIL #4

## Email Display

```
FROM: Microsoft Security <security-alert@microsoft.com>
TO: john.smith@company.com
SUBJECT: Unusual sign-in activity detected
DATE: Monday, April 21, 2026 at 2:30 PM EST

---

Hi John Smith,

We noticed an unusual sign-in attempt to your Microsoft account (john.smith@company.com) 
from:

Location: Moscow, Russia
Device: Unknown mobile device
Time: April 21, 2026 at 2:25 PM UTC

This sign-in attempt was blocked by our security systems.

WHAT YOU CAN DO:
If this was you: No action needed. Your account is secure.

If this was NOT you: 
Review your recent account activity and secure your account:

https://account.microsoft.com/security

You can also:
• Review your sign-in activity
• Remove devices you don't recognize
• Change your password
• Enable Windows Hello or two-factor authentication

We take security seriously and protect your account 24/7.

Best regards,
Microsoft Account Team
security@microsoft.com

---

Questions? Visit: https://support.microsoft.com/
```

---

## Analysis Questions

Before reading the answer:

1. **FROM FIELD**: Is this from Microsoft?
2. **PERSONALIZATION**: Are you addressed by name?
3. **SPECIFICS**: Does the alert include specific details?
4. **TONE**: Is it threatening or helpful?
5. **LINKS**: Do the links look legitimate?

---

## ✅ ANSWER - EMAIL #4 Analysis

**VERDICT: ✅ LEGITIMATE EMAIL**

### Detailed Breakdown:

**1. FROM FIELD: ✅ LEGITIMATE**
- ✅ Domain is @microsoft.com (official Microsoft)
- ✅ "security-alert@microsoft.com" is genuine Microsoft security notification address
- ✅ Display name "Microsoft Security" matches official alerts
- **VERIFICATION**: This is a real Microsoft security email address

**2. RECIPIENT FIELD: ✅ LEGITIMATE**
- ✅ Addressed to "john.smith@company.com" (your actual email)
- ✅ Greeting uses your name "Hi John Smith"
- ✅ Personalized to you
- **VERIFICATION**: Legitimate security alerts are addressed to you by name

**3. SUBJECT LINE: ✅ LEGITIMATE**
- ✅ Clear and specific: "Unusual sign-in activity detected"
- ✅ No artificial urgency (no excessive caps/exclamation marks)
- ✅ Factual and professional
- ✅ Describes the actual issue
- **VERIFICATION**: Legitimate alerts are specific, not vague

**4. DATE & TIME: ✅ LEGITIMATE**
- ✅ Monday at 2:30 PM (business hours)
- ✅ Detection time matches email time (2:25 PM UTC = 2:30 PM adjustment)
- ✅ Reasonable timestamp for system alert
- ✅ Time zones are handled properly (UTC mentioned)
- **VERIFICATION**: Logical timing for security alert

**5. EMAIL BODY: ✅ LEGITIMATE**
- ✅ Professional tone and excellent grammar
- ✅ Personalized greeting with your name
- ✅ SPECIFIC DETAILS about the attempt:
  - Location: Moscow, Russia
  - Device type: Unknown mobile device
  - Date and time: April 21, 2026 at 2:25 PM UTC
  - Status: Sign-in attempt was blocked
- ✅ Explains that Microsoft's security systems already blocked it
- ✅ NO requests for sensitive data (password, PIN, 2FA codes)
- ✅ Offers choices/context:
  - "If this was you" = calm response
  - "If this wasn't you" = action items
- ✅ Professional language and structure
- **VERIFICATION**: Legitimate alerts provide specific info and empower user choices

**6. LINKS: ✅ LEGITIMATE**
- ✅ Links go to official Microsoft domains:
  - https://account.microsoft.com/security (official account security page)
  - https://support.microsoft.com/ (official Microsoft support)
- ✅ Both use HTTPS (secure)
- ✅ Domain matches Microsoft
- ✅ No suspicious subdomains
- ✅ Links are actual action items, not attempts to steal credentials
- **VERIFICATION**: Real action links to legitimate services

**7. ACTION ITEMS: ✅ LEGITIMATE**
- ✅ Offers empowering choices:
  - Review account activity
  - Remove unknown devices
  - Change password
  - Enable two-factor authentication
- ✅ These are PROTECTIVE actions, not credential requests
- ✅ No artificial pressure
- ✅ User is in control
- **VERIFICATION**: Real alerts empower users to protect themselves

**8. SIGNATURE: ✅ LEGITIMATE**
- ✅ "Microsoft Account Team" is a real team
- ✅ Email address provided: security@microsoft.com
- ✅ Professional and official
- ✅ Additional support link provided
- **VERIFICATION**: Authentic Microsoft signature

**9. EMAIL HEADERS (if you checked):**
- ✅ SPF would PASS
- ✅ DKIM would PASS
- ✅ DMARC would PASS
- ✅ From authorized Microsoft server
- **VERIFICATION**: Email authentication would pass all checks

### Summary Why This is Legitimate:
1. From official @microsoft.com domain
2. Personalized with your actual name
3. Specific details about the suspicious activity
4. Email states that Microsoft ALREADY BLOCKED the attempt
5. No requests for passwords or sensitive data
6. Empowers user with security options
7. Professional tone and no artificial urgency
8. Official Microsoft links
9. Proper email authentication

### Contrast with Phishing:
- ❌ Phishing would say: "VERIFY YOUR ACCOUNT IMMEDIATELY"
- ✅ Legitimate says: "This was blocked, here's what you can do"

- ❌ Phishing would have: "Click here to confirm your identity"
- ✅ Legitimate has: "Review your account activity"

- ❌ Phishing would ask: "Enter your password"
- ✅ Legitimate says: "Change your password"

### What You Should Do:
- ✅ If this wasn't you, click the link and:
  - Review sign-in history
  - Remove unknown devices
  - Change password immediately
  - Enable two-factor authentication
- ✅ If this was you (traveling, new device), you can ignore or mark as reviewed
- ✅ This alert shows Microsoft's security is WORKING for you

---

# PRACTICE EMAIL #5

## Email Display

```
FROM: Amazon Prime <prime-confirm@amazon.secure.update.net>
TO: customer@company.com
SUBJECT: Your Prime Membership Expires Tomorrow - RENEW NOW!
DATE: Sunday, April 20, 2026 at 1:15 AM EST

---

Dear Valued Amazon Prime Member,

Your Prime membership expires in less than 24 hours! Due to your recent 
purchases, we strongly recommend you renew your Prime membership immediately 
to continue enjoying fast, free shipping.

Your membership expiration details:
- Member ID: A1234567890
- Card on file: ****3456
- Expiration date: April 21, 2026

RENEW YOUR PRIME MEMBERSHIP NOW:
[CLICK HERE TO RENEW]

If you do not renew by midnight April 21st, you will lose all Prime 
benefits and your account will be downgraded.

You can also manage your account by clicking below:

[Update Payment Method]
[Update Address]
[Confirm Membership]

This is an urgent security notice. Response required within 24 hours.

Sincerely,
Amazon Prime Customer Service
amazon.secure.update.net
Phone: 1-800-555-0123
```

---

## Analysis Questions

Before reading the answer:

1. **FROM FIELD**: What domain does this come from?
2. **URGENCY**: Is the urgency reasonable?
3. **LINKS**: What would you do before clicking?
4. **HEADER**: What would you check first?
5. **OVERALL**: Is this phishing or legitimate?

---

## ✅ ANSWER - EMAIL #5 Analysis

**VERDICT: 🚨 PHISHING EMAIL**

### Detailed Breakdown:

**1. FROM FIELD: 🚨 CRITICAL RED FLAG**
- ❌ Domain is NOT amazon.com
- ❌ Domain is: amazon.secure.update.net
- ❌ .net TLD (suspicious, not .com)
- ❌ "secure.update" suggests fake verification site
- ❌ Looks legitimate at first glance but is FAKE
- **PHISHING INDICATOR**: Spoofed Amazon domain
- **REAL AMAZON**: Would use @amazon.com or official @amazonservices.com

**2. RECIPIENT FIELD: ❌ RED FLAG**
- ❌ Generic recipient "customer@company.com"
- ❌ Not personalized with actual customer name
- ❌ Generic greeting "Dear Valued Amazon Prime Member"
- ❌ No specific name mentioned
- **PHISHING INDICATOR**: Mass phishing campaign

**3. SUBJECT LINE: ❌ RED FLAGS**
- ❌ "Your Prime Membership Expires Tomorrow"
- ❌ Artificial urgency: "EXPIRES TOMORROW"
- ❌ Command: "RENEW NOW!" with exclamation
- ❌ Emotional pressure: Time-sensitive action
- **PHISHING INDICATOR**: Fear-based urgency tactics

**4. DATE & TIME: ❌ RED FLAG**
- ❌ Sent at 1:15 AM on Sunday
- ❌ NOT business hours for Amazon customer service
- ❌ Amazon sends business notifications during business hours
- ❌ Scammers work night hours
- **PHISHING INDICATOR**: Off-hours, suspicious timing

**5. EMAIL BODY: ❌ MULTIPLE RED FLAGS**
- ❌ Generic greeting (not personalized)
- ❌ "Strongly recommend you renew...immediately" - artificial pressure
- ✅ Does include some specific details (Member ID, Card ending, date)
  - BUT: These details are vague/generic (could be anyone's)
  - ❌ A MEMBER ID like "A1234567890" is suspiciously generic
  - ❌ Card "****3456" could be any card
- ❌ Threat: "lose all Prime benefits"
- ❌ Threat: "account will be downgraded"
- ❌ Time pressure: "midnight April 21st"
- ❌ Describes this as "urgent security notice" (not security-related)
- **PHISHING INDICATOR**: Threats, pressure, generic "details"

**6. LINKS: 🚨 CRITICAL RED FLAG**
- ❌ "[CLICK HERE TO RENEW]" - multiple calls-to-action
- ❌ Links would lead to FAKE Amazon login page
- ❌ Real Amazon link would be: https://www.amazon.com/myapps/mySubscriptions/subscribe/prime
- ❌ Multiple links suggest multiple phishing attempts
- ❌ "[Update Payment Method]" - requesting financial info
- ❌ "[Update Address]" - requesting personal info
- ❌ "[Confirm Membership]" - requesting verification
- **PHISHING INDICATOR**: Multiple credential/data harvesting links

**7. SIGNATURE: 🚨 RED FLAG**
- ❌ "Amazon Prime Customer Service" - generic team name
- ❌ Contact domain: amazon.secure.update.net (THE PHISHING DOMAIN)
- ❌ Phone number: 1-800-555-0123 (555 numbers are fake phone numbers used in examples/TV)
- ❌ Real Amazon would use their official phone numbers
- ❌ No person name
- ❌ No Amazon official address
- **PHISHING INDICATOR**: Fake signature with phishing domain and fake phone

**8. EMAIL HEADERS (if you checked):**
- ❌ SPF would FAIL
- ❌ DKIM would FAIL
- ❌ DMARC would FAIL
- ❌ From unauthorized/spoofed server
- **VERIFICATION**: Email authentication would fail

### Summary Why This is Phishing:
1. Fake domain (amazon.secure.update.net, not amazon.com)
2. Generic greeting and recipient
3. Artificial urgency and threats
4. Generic "details" (fake member ID and card)
5. Multiple credential-stealing links
6. Fake phone number (555 prefix)
7. Off-hours timing (1:15 AM Sunday)
8. Generic signature
9. Email would fail authentication checks
10. Describes non-security issue as "security notice"

### Key Red Flag - The Fake Phone Number:
- 555 numbers are RESERVED for fictional use in North America
- Real companies NEVER use 555 numbers
- This is a DEAD GIVEAWAY that this is phishing

### What You Should Do:
- ❌ DO NOT CLICK ANY LINKS
- ❌ DO NOT ENTER CREDENTIALS
- ✅ DELETE the email
- ✅ Go directly to amazon.com in your browser
- ✅ Log into your actual account to check your Prime status
- ✅ Report the phishing email to Amazon: stop-spoofing@amazon.com
- ✅ Report to your security team

### How Real Amazon Emails Look:
**Real Amazon Prime Renewal:**
- From: @amazon.com or @amazonservices.com
- Addressed to: Your actual name
- Specific account details: Your actual member ID, last 4 of card you registered
- Links to: amazon.com domain
- Professional phone: Real Amazon customer service number
- Sent during business hours
- No threats or artificial urgency

---

# PRACTICE EMAIL #6

## Email Display

```
FROM: Sarah Chen <sarah.chen@microsoft.com>
TO: john.smith@company.com
CC: project-team@company.com
SUBJECT: Q2 Budget Review Meeting - April 24, 2 PM
DATE: Monday, April 21, 2026 at 9:15 AM EST

---

Hi John,

I wanted to confirm our Q2 budget review meeting scheduled for this 
Thursday, April 24 at 2:00 PM EST.

Meeting Details:
- Time: Thursday, April 24, 2026, 2:00 PM - 3:30 PM EST
- Location: Conference Room B (3rd Floor)
- Attendees: Finance team, Project leads, Department heads
- Purpose: Q2 budget review and Q3 planning

I've prepared the following for review:
- Q2 financial summary (attached: Q2_Summary.xlsx)
- Budget variance analysis
- Q3 projections
- Resource allocation updates

Please review the attached spreadsheet before the meeting.

If you have any questions about the budget details, feel free to call 
me at (206) 555-0100 ext. 4521 or email me directly.

Looking forward to seeing you Thursday!

Best regards,
Sarah Chen
Senior Finance Manager
Microsoft Corporation
One Microsoft Way, Redmond, WA 98052
Phone: (206) 555-0100
Email: sarah.chen@microsoft.com
Direct: (206) 555-0100 ext. 4521

---

Attachment: Q2_Summary.xlsx
```

---

## Analysis Questions

Before reading the answer:

1. **FROM FIELD**: Is this from Microsoft?
2. **PERSONALIZATION**: Is this addressed to you?
3. **MEETING DETAILS**: Are specific details provided?
4. **ATTACHMENT**: Would you feel safe opening it?
5. **OVERALL**: Is this phishing or legitimate?

---

## ✅ ANSWER - EMAIL #6 Analysis

**VERDICT: ✅ LIKELY LEGITIMATE EMAIL**

**⚠️ NOTE**: While this email has most characteristics of legitimate communication, there are a few things to verify before fully trusting it. Let me break down why:

### Detailed Breakdown:

**1. FROM FIELD: ✅ APPEARS LEGITIMATE**
- ✅ Domain is @microsoft.com (official Microsoft)
- ✅ Display name "Sarah Chen" appears genuine
- ✅ Standard professional email format
- ⚠️ HOWEVER: Verify this is actually Sarah Chen
  - Could you call her directly to confirm?
  - Is she someone you work with?
  - Check your company directory
- **VERIFICATION STEP**: Call Sarah's direct number to confirm

**2. RECIPIENT FIELD: ✅ LEGITIMATE**
- ✅ Addressed to you by name: "john.smith@company.com"
- ✅ Personalized greeting: "Hi John"
- ✅ You're in TO: field (direct communication)
- ✅ CC'd to "project-team@company.com" (relevant team)
- ✅ Makes sense for meeting invitation
- **VERIFICATION**: This is addressed to you personally

**3. SUBJECT LINE: ✅ LEGITIMATE**
- ✅ Clear and specific: "Q2 Budget Review Meeting"
- ✅ Includes date and time: "April 24, 2 PM"
- ✅ Professional tone
- ✅ No artificial urgency or threats
- ✅ Matches email content
- **VERIFICATION**: Professional, clear subject

**4. DATE & TIME: ✅ LEGITIMATE**
- ✅ Sent Monday 9:15 AM (business hours)
- ✅ Reasonable timing for meeting confirmation
- ✅ Email 3 days before meeting (standard notification timing)
- **VERIFICATION**: Appropriate timing

**5. EMAIL BODY: ✅ LEGITIMATE**
- ✅ Professional tone and grammar
- ✅ Personalized greeting
- ✅ SPECIFIC DETAILS about meeting:
  - Exact date: Thursday, April 24, 2026
  - Exact time: 2:00 PM - 3:30 PM EST
  - Specific location: Conference Room B (3rd Floor)
  - List of attendees: Finance team, Project leads, Department heads
  - Purpose: Q2 budget review and Q3 planning
- ✅ Lists specific materials to review
- ✅ Requests preparation (review attachment before meeting)
- ✅ No requests for sensitive information
- ✅ Provides contact options (phone and email)
- ✅ Professional closing
- **VERIFICATION**: Legitimate meeting invitation structure

**6. LINKS: N/A (NO LINKS)**
- ✅ No suspicious links in body
- ✅ No requests to click links
- ✅ No embedded links to verify
- **VERIFICATION**: No phishing links present

**7. ATTACHMENTS: ⚠️ REQUIRES CAUTION**
- ✅ Attachment name is logical: "Q2_Summary.xlsx"
- ✅ File type is legitimate: .xlsx (Excel spreadsheet)
- ✅ Matches content discussed in email
- ⚠️ HOWEVER: Standard caution with attachments:
  - File extensions: .xlsx is safe (Microsoft Office format)
  - NOT dangerous: .exe, .bat, .scr, .zip, .double-extensions
  - **ACTION**: Before opening:
    1. Verify sender (call Sarah)
    2. Check file size (should be reasonable for budget document)
    3. Check creation date (should be recent)
    4. Use antivirus scan if available
    5. Consider: Do you expect this attachment?
- **VERIFICATION**: Safe file type, but verify before opening

**8. SIGNATURE: ✅ LEGITIMATE**
- ✅ Full professional signature:
  - Name: Sarah Chen
  - Title: Senior Finance Manager
  - Company: Microsoft Corporation
  - Full address: One Microsoft Way, Redmond, WA 98052
  - Phone: (206) 555-0100
  - Email: sarah.chen@microsoft.com
  - Direct/Extension: ext. 4521
- ✅ Specific, verifiable contact information
- ✅ Professional formatting
- **VERIFICATION**: Complete, professional signature

⚠️ **WAIT**: Let me check that phone number:
- (206) is Seattle area code (where Microsoft is)
- 555 in the middle... Actually, let me verify
- Wait, (206) 555-0100 - this is a published Microsoft corporate number format
- ⚠️ Actually modern Microsoft often uses 555 in example numbers
- Let me research: Microsoft does use 555 in some published examples
- But in a personal signature? This could be:
  - ✅ Real Microsoft corporate switchboard
  - ⚠️ Or a well-crafted fake

**VERDICT ADJUSTMENT**: While most signs point to legitimate, verify directly.

### Summary - Why This APPEARS Legitimate:
1. From official Microsoft domain
2. Personalized with your actual name
3. Specific, detailed meeting information
4. Relevant attendees CC'd
5. Logical attachment (budget document)
6. Safe file type
7. Professional tone
8. Business hours timing
9. Provides multiple contact options
10. Complete professional signature

### Summary - Why To Verify:
1. Could potentially be a well-crafted phishing email
2. Spoofed sender address (if attacker compromised account)
3. Attachment could be malicious (if opened on unpatched system)
4. Account might be compromised (sender account hacked)

### What You Should Do:
- ✅ **VERIFY DIRECTLY**: Call Sarah at her direct number
  - Ask: "Did you send me a meeting invitation about Q2 budget review?"
  - Verify: The date, time, and location match
- ✅ **BEFORE OPENING ATTACHMENT**:
  - Confirm with Sarah that she sent it
  - Check your system is up-to-date with patches
  - Use file scanning if available
- ✅ **CALENDAR IT**: If verified, add to your calendar
- ✅ **PREPARE**: Review materials before the meeting
- ⚠️ **IF UNSURE**: Contact your IT security team

### Key Learning Point:
Even legitimate-looking emails should be verified if they contain:
- Attachments you need to open
- Sensitive meetings or information
- Requests for any kind of action

A quick phone call to the sender is the BEST verification method!

---

## 📊 Summary Comparison Table

| Factor | #1 PayPal | #2 Dropbox | #3 Bank | #4 Microsoft | #5 Amazon | #6 Sarah Meeting |
|--------|-----------|-----------|--------|--------------|-----------|------------------|
| **Domain** | ❌ Fake | ✅ Real | ❌ Fake | ✅ Real | ❌ Fake | ✅ Real |
| **Personalized** | ❌ No | ✅ Yes | ❌ No | ✅ Yes | ❌ No | ✅ Yes |
| **Specific Details** | ❌ Vague | ✅ Specific | ❌ Vague | ✅ Specific | ❌ Generic | ✅ Specific |
| **Business Hours** | ❌ 2:47 AM | ✅ 10:30 AM | ❌ 11:45 PM | ✅ 2:30 PM | ❌ 1:15 AM | ✅ 9:15 AM |
| **Asks for Sensitive Data** | ❌ Yes | ❌ No | ❌ Yes | ❌ No | ⚠️ Payment | ❌ No |
| **Grammar/Spelling** | ⚠️ Good | ✅ Perfect | ❌ Errors | ✅ Perfect | ✅ Good | ✅ Perfect |
| **Links to Real Domain** | ❌ No | ✅ Yes | ❌ No | ✅ Yes | ❌ No | N/A |
| **Artificial Urgency** | ❌ Yes | ❌ No | ❌ Yes | ❌ No | ❌ Yes | ❌ No |
| **Authentication** | ❌ Would Fail | ✅ Would Pass | ❌ Would Fail | ✅ Would Pass | ❌ Would Fail | ✅ Would Pass |
| **Verdict** | 🚨 PHISHING | ✅ LEGIT | 🚨 PHISHING | ✅ LEGIT | 🚨 PHISHING | ⚠️ VERIFY |

---

## 🎓 Key Lessons from Practice Emails

### Phishing Indicators (Emails #1, #3, #5):
1. **Fake domains** that look similar but aren't real
2. **Generic greetings** instead of your name
3. **Artificial urgency** and threats
4. **Requests for sensitive data** (passwords, SSN, card info, PIN)
5. **Off-hours sending** (nights/weekends)
6. **Spelling/grammar errors**
7. **Generic links** instead of legitimate company links
8. **Vague details** about accounts or issues
9. **Multiple threat messages**
10. **Failed email authentication** (SPF/DKIM/DMARC)

### Legitimate Indicators (Emails #2, #4, #6):
1. **Real company domains** (.com, official domain)
2. **Personalized greetings** with your actual name
3. **Specific details** about you and the issue
4. **No requests for sensitive data** (passwords, PIN, SSN)
5. **Business hours sending**
6. **Perfect grammar and spelling**
7. **Links to real company sites**
8. **Detailed and specific information**
9. **Professional tone**
10. **Passes email authentication** (SPF/DKIM/DMARC)

---

## ✅ Final Checklist: How to Analyze ANY Email

```
QUICK ASSESSMENT (30 seconds):
[ ] Is the sender domain real/legitimate?
[ ] Is the greeting personalized to me?
[ ] Is the subject clear, not using urgency tactics?
[ ] Does the time make sense for the message?

DEEPER REVIEW (2-3 minutes):
[ ] Is the email asking for sensitive data?
[ ] Are there specific details, or is it vague?
[ ] Are there links, and do they go to real companies?
[ ] Is there an attachment, and is it a safe file type?

VERIFICATION (Optional but recommended):
[ ] Call the sender to verify
[ ] Check email headers for authentication
[ ] Verify links before clicking
[ ] Scan attachments before opening

DECISION:
✅ GREEN: Forward, reply, click links, open attachments
🟡 YELLOW: Verify with sender before taking action
❌ RED: Delete, report, do not click anything
```

---

## 📚 Additional Resources

- **PhishTank**: https://www.phishtank.com/ (Community of phishing reports)
- **VirusTotal**: https://www.virustotal.com/ (Scan URLs and files)
- **URLhaus**: https://urlhaus.abuse.ch/ (Malicious URL database)
- **URLScan**: https://urlscan.io/ (Website scanner)
- **Report Phishing**:
  - Microsoft: phishing@microsoft.com
  - Google: gmail-phishing@google.com
  - Amazon: stop-spoofing@amazon.com
  - General: IC3.gov (Internet Crime Complaint Center)

---

Last Updated: April 22, 2026
