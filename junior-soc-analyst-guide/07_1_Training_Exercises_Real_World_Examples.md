# Training and Exercises Real-World Examples

These examples show how a Junior SOC Analyst participates in realistic training, tabletop exercises, and simulations. The goal is not to be perfect; it is to practice decision-making, communication, and improvement.

---

## Example 1: Tabletop Exercise for Ransomware

### Scenario
The security team runs a tabletop exercise where several file shares become unavailable and users report files renamed with a strange extension.

### Analyst Role
The Junior SOC Analyst is assigned to monitor SIEM and EDR alerts, record timeline events, and brief the SOC lead every 15 minutes.

### What Happens
1. Helpdesk reports users cannot open files on a shared drive.
2. EDR alert appears for suspicious file rename behavior.
3. The SOC lead asks for affected hosts, users, and first-seen time.
4. Infrastructure team asks whether they should disconnect a server.
5. Management asks whether client data is affected.

### Good Analyst Actions
- State only confirmed facts.
- Keep a timeline with exact times.
- Separate confirmed impact from suspected impact.
- Escalate uncertainty instead of guessing.
- Record decisions made by senior responders.

### Example Exercise Note
```
10:05 - Helpdesk reports multiple users unable to open files on Finance share.
10:07 - EDR alert observed for rapid file rename activity on LAP-3320.
10:09 - SIEM shows user j.santos accessing Finance share before alert.
10:12 - SOC Lead directed endpoint isolation for LAP-3320.
10:15 - Infrastructure team reviewing file server health. No confirmed client data exposure yet.
```

### After-Action Learning
The analyst learned that leadership needs short, confirmed updates during a crisis. Long technical explanations are less useful than accurate status, impact, and next action.

---

## Example 2: Phishing Drill Review

### Scenario
The company runs a simulated phishing campaign. Some users report the email, some ignore it, and a few submit credentials to the training page.

### Analyst Role
The Junior SOC Analyst reviews reports, confirms the campaign is authorized, and helps measure response behavior.

### What Happens
1. Users begin reporting the simulated email.
2. SOC receives multiple phishing tickets for the same message.
3. A few managers ask whether the email is real.
4. The training team asks for report rate and click rate.

### Good Analyst Actions
- Confirm with the training calendar that the drill is approved.
- Avoid telling users it is a simulation before the drill ends unless policy allows.
- Group duplicate reports under the drill tracking ticket.
- Record user reports, clicks, and credential submissions according to the training process.

### Example Exercise Note
```
Confirmed email subject "Updated Benefits Enrollment" is part of approved phishing simulation scheduled for 2026-04-23. Created parent tracking ticket and linked 18 duplicate user reports. No security incident opened because sender/domain match approved simulation infrastructure. Metrics sent to training owner after campaign window closed.
```

### After-Action Learning
The analyst learned to validate whether an alert is part of an authorized exercise before escalating it as a real incident.

---

## Example 3: New Analyst Shadowing During Live Triage

### Scenario
A new analyst shadows a senior analyst during a live suspicious login investigation.

### Analyst Role
The Junior SOC Analyst observes, asks questions at appropriate pauses, and documents the investigation flow.

### What Happens
1. SIEM alert shows successful login from a new location.
2. Senior analyst checks recent login history and MFA details.
3. User is contacted through a known phone number.
4. The account is confirmed suspicious and escalated.

### Good Analyst Actions
- Write down the order of checks performed.
- Note which tools were used for identity, endpoint, and email review.
- Ask why each decision point mattered.
- Compare the live workflow to the written triage guide afterward.

### Example Learning Note
```
Observed suspicious login triage from alert intake through escalation. Key lesson: user confirmation should use trusted contact information, not contact details from the suspicious session. Senior analyst checked login history, MFA method, device novelty, mailbox rules, and recent file access before escalating to Identity team.
```

### After-Action Learning
Shadowing helps connect written procedures to real timing, tool limitations, and communication habits inside the SOC.

