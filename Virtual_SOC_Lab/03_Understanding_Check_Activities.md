# Understanding Check Activities

These activities test your understanding after you complete the guided practice. Try them without looking at the step-by-step guide first. Afterward, compare your answers to your notes.

---

## Challenge 1: Unknown Scan Investigation

### Scenario

You see Security Onion activity showing many connection attempts from Kali to Metasploitable across several ports.

### Your Task

Investigate and document the activity.

### Deliverables

- Source IP
- Destination IP
- Time window
- Ports contacted
- Most likely tool or activity
- Whether the activity is expected or suspicious
- Short analyst summary

### Questions

- What evidence proves this was a scan?
- Which logs were most useful?
- Would this be low, medium, or high severity in a real company network?
- What additional context would you ask for before escalating?

---

## Challenge 2: Web Application Browsing Review

### Scenario

A user reports that someone accessed an old internal web server. In your lab, treat Metasploitable as that old internal server.

### Your Task

Use Security Onion to identify web traffic from Kali to Metasploitable.

### Deliverables

- HTTP host or destination IP
- URI paths visited
- Source IP
- User agent if visible
- Time of first observed request
- Time of last observed request

### Questions

- What does the HTTP path tell you?
- Can you tell whether the user submitted credentials?
- What evidence would you need from the web server itself?
- How would your investigation change if the traffic used HTTPS?

---

## Challenge 3: Authentication Activity Review

### Scenario

Security Onion shows SSH traffic from Kali to Metasploitable. You need to determine what can and cannot be concluded from the available evidence.

### Your Task

Review the SSH-related network activity and write a short finding.

### Deliverables

- Source IP
- Destination IP
- Destination port
- Session start time
- Session duration if available
- Confirmed facts
- Unknowns

### Questions

- Can Security Onion prove the password used?
- Can network logs alone always prove login success?
- Which host logs would help?
- When would this become an incident?

---

## Challenge 4: Build a Timeline

### Scenario

You performed several lab actions in one session:

1. Pinged Metasploitable
2. Ran an Nmap service scan
3. Browsed to the Metasploitable web page
4. Attempted an SSH login

### Your Task

Build a timeline from Security Onion and your Kali terminal history.

### Deliverables

Use this format:

```text
Time | Source | Destination | Activity | Evidence | Analyst Note
```

### Questions

- Which event happened first?
- Which event generated the most network noise?
- Which event would be easiest to explain to a manager?
- Which event would require the most technical detail?

---

## Challenge 5: Write an Escalation Decision

### Scenario

Imagine the same scan and SSH activity happened in a real business network from an unknown workstation to an old server.

### Your Task

Decide whether to escalate.

### Deliverables

Write a short escalation decision:

```text
Decision:

Reason:

Evidence:

Risk:

Recommended Next Step:
```

### Questions

- Is the source system authorized to scan?
- Is the destination server sensitive?
- Are there repeated login failures?
- Are there signs of successful access?
- Who should be notified?

---

## Self-Grading Checklist

Use this checklist to review your own work:

- [ ] I recorded exact IP addresses.
- [ ] I separated confirmed facts from assumptions.
- [ ] I included timestamps.
- [ ] I identified the relevant log source.
- [ ] I explained why the activity matters.
- [ ] I avoided overstating what the evidence proves.
- [ ] I wrote a clear analyst summary.
- [ ] I recommended a reasonable next action.

---

## Answer Key Guidance

There is not one perfect answer because your IP addresses, timestamps, and Security Onion logs will differ. A strong answer should:

- Clearly identify Kali as the source and Metasploitable as the target.
- Recognize Nmap-style activity as reconnaissance or service discovery.
- Treat lab activity as authorized, but explain how it could be suspicious in production.
- Use Security Onion evidence instead of guessing.
- State unknowns clearly, especially for encrypted protocols like SSH.
- Recommend escalation only when the context supports it.

