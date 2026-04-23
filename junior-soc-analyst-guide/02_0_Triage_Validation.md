# Perform Initial Triage and Validation

## 📋 Review Points

- [ ] Understand what alert triage is and why it matters
- [ ] Know the difference between triage, investigation, and validation
- [ ] Understand context gathering techniques
- [ ] Recognize indicators of compromise (IoCs)
- [ ] Know common false positive indicators
- [ ] Understand user and asset context importance
- [ ] Know how to validate alerts against business context
- [ ] Understand risk assessment basics

---

## 🔍 Step-by-Step Guide

### Step 1: Receive and Initial Assessment
1. Open the alert in your ticketing/SIEM system
2. Read the alert title and description
3. Note the alert timestamp and source tool
4. Check if this is a duplicate of recent alerts
5. Determine if alert has been seen before

### Step 2: Gather Contextual Information
1. Identify the affected system/user
2. Verify the system exists and is legitimate
3. Check the user's role and department
4. Review user login history (when was last login?)
5. Confirm system is actively monitored
6. Check asset owner/custodian
7. Determine system criticality level

### Step 3: Understand the Alert Details
1. Read the alert message completely
2. Note the specific event or behavior detected
3. Identify the source IP, destination IP, ports, protocols
4. Check file hashes if applicable
5. Review process names and command lines
6. Note any external systems involved

### Step 4: Check for False Positive Indicators
1. Is this a known legitimate activity?
2. Has a system administrator been making changes?
3. Is this part of a maintenance window?
4. Could this be legitimate user behavior?
5. Check if similar behavior was whitelisted before
6. Verify if software is authorized on the system

### Step 5: Validate Against Business Context
1. Check the business activity at that time (markets, events, incidents)
2. Verify if the user should be accessing this resource
3. Confirm if the timing makes sense
4. Check if the action aligns with user's normal behavior
5. Verify asset location and network access is expected

### Step 6: Document Triage Assessment
1. Record your findings in the alert/ticket
2. Note what you checked and what you found
3. Classify the alert as:
   - **True Positive**: Legitimate security concern
   - **False Positive**: Not a real threat
   - **Suspicious**: Needs further investigation
   - **Inconclusive**: Need more information
4. Document your confidence level
5. Record next action needed

### Step 7: Make Triage Decision
1. Determine if escalation is needed based on severity and findings
2. If false positive, document the reason and close
3. If true positive or suspicious, prepare for escalation
4. Set priority based on risk level
5. Assign to appropriate team if needed

---

## 📚 References to Study

- **Alert Triage Framework**: https://www.sans.org/white-papers/alert-triage
- **False Positive Reduction**: https://www.splunk.com/en_us/blog/security/reducing-false-positives.html
- **Indicators of Compromise (IoCs)**: https://www.crowdstrike.com/cybersecurity-101/indicators-of-compromise/
- **User Behavior Analytics**: https://www.gartner.com/en/information-technology/glossary/user-and-entity-behavior-analytics
- **MITRE ATT&CK Framework**: https://attack.mitre.org/
- **Alert Validation Best Practices**: https://www.nist.gov/publications/incident-handling

---

## 🎯 Practice Activities

### Activity 1: Triage Checklist Development (30 minutes)
1. Work with your team lead to create a triage checklist
2. Include questions you should ask for each alert type
3. Document your team's specific resources and references
4. Create laminated reference card for your desk
5. Practice using the checklist on 5 sample alerts

### Activity 2: Context Gathering Exercise (45 minutes)
1. Receive sample alerts with limited context
2. Practice gathering information from available systems
3. Learn how to navigate your AD/asset management tools
4. Document user information accurately
5. Present findings for 3 different alerts

### Activity 3: False Positive Identification (1 hour)
1. Review list of 20 historical alerts marked as false positives
2. Identify the reasons for false positive classification
3. Document common patterns
4. Create a reference guide of known false positive causes
5. Share findings with team

### Activity 4: Validation Scenario Simulation (1-2 hours)
1. Work through 10 realistic alert scenarios
2. Gather context for each scenario
3. Document your triage assessment
4. Make escalation/closure decision
5. Review decisions with team lead and discuss reasoning

### Activity 5: Business Context Learning (Ongoing)
1. Meet with team lead to understand business operations
2. Learn key business events and schedules
3. Understand critical asset locations
4. Document department contacts and responsibilities
5. Review org chart to understand reporting structures

---

## ✅ Success Criteria

- Consistently ask relevant clarifying questions
- Accurately identify false positives
- Document triage decisions clearly
- Gather sufficient context before escalating
- Make decisions within expected timeframe
- Reduce escalation of non-critical alerts
- Improve alert closure rate
- Build knowledge of business operations
