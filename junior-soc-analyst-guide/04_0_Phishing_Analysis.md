# Analyze Phishing Attempts

## 📋 Review Points

- [ ] Understand phishing attack types and variations
- [ ] Know common phishing indicators and red flags
- [ ] Understand email headers and how to read them
- [ ] Know how to identify suspicious links and attachments
- [ ] Understand social engineering tactics
- [ ] Know how to use threat intelligence tools
- [ ] Understand OSINT (Open Source Intelligence) basics
- [ ] Know how to document phishing analysis
- [ ] Understand remediation steps for phishing incidents

---

## 🔍 Step-by-Step Guide

### Step 1: Receive and Isolate the Phishing Email
1. Identify the email as a potential phishing attempt
2. Document the timestamp and source
3. Take screenshots of the email
4. Do NOT click links or download attachments
5. Note sender email address and display name
6. Record email subject line and body content

### Step 2: Examine Email Headers
1. Open full email headers in your email system
2. Check the "From" field for authenticity:
   - Is it from the claimed organization?
   - Does domain spelling look correct?
3. Trace the email path through mail servers
4. Check Return-Path and Authentication-Results
5. Look for SPF, DKIM, DMARC failures:
   - SPF: Sender Policy Framework
   - DKIM: DomainKeys Identified Mail
   - DMARC: Domain-based Message Authentication, Reporting and Conformance
6. Identify any spoofing indicators

### Step 3: Analyze Links in the Email
1. Hover over links WITHOUT clicking to see actual URL
2. Check if URL matches claimed destination
3. Look for suspicious patterns:
   - Misspelled domain names (goggle.com vs google.com)
   - IP addresses instead of domain names
   - Unusual subdomains
   - Shortened URLs (use URL expander tools)
4. Check for suspicious TLD (.xyz, .tk, etc.)
5. Document each link and its characteristics

### Step 4: Examine Attachments
1. Note attachment names and types
2. Check for suspicious characteristics:
   - Unusual file extensions (.exe, .scr, .zip, etc.)
   - Double extensions (.pdf.exe)
   - Generic names (invoice, document, etc.)
   - Icon inconsistencies
3. Note file size
4. Use VirusTotal or similar to scan hash
5. Do NOT execute attachments

### Step 5: Analyze Content and Social Engineering
1. Review email body for social engineering tactics:
   - Urgency ("Act now!", "Verify immediately")
   - Authority (impersonating executives, IT, support)
   - Fear (account closure, legal action)
   - Greed (lottery winnings, refunds)
2. Check for grammar/spelling errors
3. Look for generic greetings ("Dear Valued Customer")
4. Identify claimed action items (click, download, call, reply)
5. Check for legitimate branding and logos

### Step 6: Check Against Threat Intelligence
1. Search the sender email address in:
   - Your organization's threat intelligence database
   - Public threat feeds and databases
   - VirusTotal
   - OSINT tools (Hunter.io, EmailFinder, etc.)
2. Check domain reputation:
   - Domain registration date (brand new domains are suspicious)
   - Domain age and history
   - DNS records
3. Check URL reputation in threat databases
4. Check file hash against malware databases
5. Document any known threat campaign associations

### Step 7: Identify Affected Users
1. Determine who received the email
2. Check if anyone opened it or clicked links
3. Review email logs for delivery
4. Identify users who may have taken action
5. Prioritize notification for affected users

### Step 8: Document Analysis and Make Determination
1. Compile all findings into analysis report
2. Classify as:
   - **Definite Phishing**: Clear malicious intent
   - **Likely Phishing**: Strong indicators of phishing
   - **Suspicious**: Warrants further investigation
   - **Legitimate**: Safe email
3. Assign confidence level
4. Recommend actions
5. Document evidence

### Step 9: Take Action
1. If phishing confirmed:
   - Report to management
   - Add sender to blocklist
   - Alert affected users
   - Initiate remediation if needed
2. If suspicious:
   - Escalate to incident response
   - Monitor for similar emails
3. If legitimate:
   - Close ticket and document findings

---

## 📚 References to Study

- **Phishing Attack Indicators**: https://www.sans.org/reading-room/whitepapers/phishing-attack-indicators
- **Email Security Best Practices**: https://www.ncsc.gov.uk/guidance/phishing-attacks-defending-your-organisation-and-users
- **OSINT for Threat Analysis**: https://www.shodan.io/ | https://www.abuseipdb.com/
- **Threat Intelligence Feeds**: https://www.virustotal.com/ | https://exchange.xforce.ibmcloud.com/
- **Email Header Analysis Guide**: https://mxtoolbox.com/
- **Social Engineering Tactics**: https://www.sans.org/reading-room/whitepapers/awareness/social-engineering-attacks
- **Phishing Campaign Examples**: https://phishing.mailchimp.com/
- **URL Analysis Tools**: https://urlhaus.abuse.ch/ | https://www.urlscan.io/

---

## 🎯 Practice Activities

### Activity 1: Email Header Analysis Practice (45 minutes)
1. Review 5 sample emails with headers
2. Practice extracting key information
3. Identify SPF/DKIM/DMARC results
4. Identify spoofing attempts
5. Create analysis notes for each

### Activity 2: Phishing Indicator Identification (1 hour)
1. Review 10-15 sample phishing emails
2. Identify red flags in each email
3. Document indicators found
4. Explain why each is suspicious
5. Compare your analysis with expert analysis

### Activity 3: Link and Attachment Analysis (1 hour)
1. Practice using URL analysis tools (URLhaus, URLScan)
2. Expand 10 shortened URLs
3. Check 10 file hashes in VirusTotal
4. Document suspicious findings
5. Learn to recognize obfuscation techniques

### Activity 4: Social Engineering Tactic Recognition (45 minutes)
1. Review common social engineering tactics
2. Identify tactics in 10 sample emails
3. Explain why each tactic is used
4. Create awareness poster for each tactic
5. Present findings to team

### Activity 5: Comprehensive Phishing Analysis (2-3 hours)
1. Receive 5 realistic phishing scenarios
2. Perform complete analysis on each
3. Check email headers thoroughly
4. Analyze links and attachments
5. Search threat intelligence
6. Create detailed analysis report
7. Present findings to team lead
8. Discuss remediation actions

### Activity 6: Threat Intelligence Research (2 hours)
1. Learn to use threat intelligence tools:
   - VirusTotal
   - AbuseIPDB
   - URLhaus
   - Shodan
2. Practice searching for threat indicators
3. Document findings in structured format
4. Create threat profile for sample attacker
5. Present intelligence findings

### Activity 7: Phishing Drill Participation (Ongoing)
1. Participate in organizational phishing drills
2. Report suspicious emails correctly
3. Practice not clicking on malicious links
4. Review drill results and learn from mistakes
5. Share experiences with colleagues

---

## ✅ Success Criteria

- Identify phishing emails accurately
- Extract and analyze email headers correctly
- Use threat intelligence tools effectively
- Classify phishing attempts appropriately
- Document analysis clearly and completely
- Avoid clicking suspicious links/attachments
- Identify social engineering tactics
- Provide actionable recommendations
- Escalate phishing incidents appropriately
- Maintain up-to-date phishing knowledge
