# Demonstration Overview

**Purpose:** Show students how to perform an ethical audit of a raw intelligence request and produce a signed Intelligence Scope Document.

> Insert here

## Step 1: Read the Raw Intelligence Request

### Raw Intelligence Request `#DEMO-2026-001`

| Field | Value |
| --- | --- |
| Requestor | James Morrison, Director of Fraud Prevention |
| Date Received | 2026-04-23 |
| Priority | Critical |

**Request Text:**

> "We have evidence that a competitor was attacked by a group using ransomware called 'CryptoVault'. We need you to identify the real-world identities of the attackers. Find their names, home addresses, family members, and social media accounts. Our CEO wants to 'name and shame' them publicly. Use any means necessary including monitoring their personal email if we can get access. Budget is not a concern. Deliverable due in 24 hours."

**Additional Notes from Requestor:**

> "I have a friend at a cyber insurance company who can give us internal incident reports from the competitor. Use those as a starting point."

Notice several red flags immediately.

> Insert here

## Step 2: Identify Red Flags in the Request

| Problematic Element | Why It's a Problem |
| --- | --- |
| "real-world identities of the attackers" | Attribution to named individuals is legally dangerous. |
| "names, home addresses, family members" | This is PII (Personally Identifiable Information). |
| "use any means necessary" | No ethical boundaries are defined. |
| "monitoring their personal email" | This is illegal without a warrant (CFAA violation). |
| "friend at a cyber insurance company" | Unauthorized sharing of competitor data. |
| "name and shame them publicly" | The intent is retaliation, not defense. |

Any one of these would require us to push back.

Together, they make this request impossible to fulfill legally or ethically.

> Insert here

## Step 3: Open the Intelligence Scope Document Template

> Insert here

## Step 4: Complete Section 1 - Completeness Audit

| Requirement Element | Present? | If Missing, What Is Needed? |
| --- | --- | --- |
| Specific threat actor name/identifier | N | Need actor name, alias, or associated malware family. Only the "CryptoVault" ransomware name is provided, which is insufficient. |
| Timeframe of intelligence needed | N | Need a specific date range for intelligence collection. |
| Geographic jurisdiction(s) involved | N | Unknown where the competitor, attacker, or data resides (US, EU, elsewhere). |
| Specific data types requested | Y (partial) | The request asks for PII (names, addresses, family), but this is legally problematic. |
| Allowed collection methods | N | "Any means necessary" is not a valid method. Specific, legal sources are required. |
| Deliverable format | N | Not specified (PDF, presentation, verbal, etc.). |

Five out of six requirements are missing or incomplete. This request is severely underspecified.

> Insert here

## Step 5: Complete Section 2 - Legal Risk Identification

Identify three specific legal risks. Name the law, assign a risk level, and justify each one.

| Identified Legal Risk | Relevant Law/Policy | Risk Level | Justification |
| --- | --- | --- | --- |
| Collecting home addresses and names of individuals | GDPR (if EU citizen), CCPA (if CA resident), CFAA | HIGH | Personal data collection without consent violates multiple privacy laws. Attribution of criminal activity to named individuals requires law enforcement authority. |
| Using a friend's access to competitor incident reports | CFAA (Computer Fraud and Abuse Act) | HIGH | Accessing a competitor's internal data without authorization is a federal felony, even if a friend provides it. |
| Monitoring personal email accounts | CFAA, ECPA (Electronic Communications Privacy Act) | HIGH | Unauthorized access to email accounts violates federal wiretap laws. This requires a warrant. |

All three risks are **HIGH**. There is no way to proceed with this request as written.

> Insert here

## Step 6: Complete Section 3 - Privacy Constraints

| Privacy Concern | Specific Data Element at Risk | Mitigation Required |
| --- | --- | --- |
| Collection of attacker PII | Real names, home addresses, family member names | Exclude entirely. CTI should use handles or aliases only, never personal identifiers. |
| Unauthorized competitor data access | Competitor's internal incident reports | Do not accept or request. This requires a subpoena or written authorization from the competitor. |

Notice that the mitigation says **exclude entirely**. Some data should never be collected, period.

> Insert here

## Step 7: Complete Section 4 - Express Scope Definition

Define what **is in scope** (what we could legally do) and what is **out of scope** (what we explicitly refuse to do). This is the most important section for protecting the organization.

### In Scope

- Analyze publicly available threat reports about CryptoVault ransomware.
- Review open-source intelligence (OSINT) for infrastructure indicators such as IPs and domains.
- Search malware repositories for CryptoVault samples and analysis.
- Document TTPs (Tactics, Techniques, and Procedures) from public sandbox reports.
- Provide anonymized threat intelligence without PII.

### Out of Scope

- Collection of real names, home addresses, or family member information for any individual.
- Accessing competitor internal incident reports by any method.
- Monitoring personal email accounts or any private communication.
- Any action requiring credentials not owned by Meridian Financial Group.
- Public "naming and shaming" of individuals.

Notice that the **Out of Scope** section directly addresses each problematic element from the raw request. This creates a legal firewall.

> Insert here

## Step 8: Complete Section 5 - Signed Approval

Sign the document and select the recommended action.

> Insert here

Check **Reject entirely** because the fundamental legal violations cannot be fixed by adding scope boundaries. Some requests must be rejected outright.

> Insert here

## Step 9: Summary and Key Takeaways

Three most important things to remember:

| # | Key Takeaway |
| --- | --- |
| 1 | You can say **no**. Not every intelligence request is legal or ethical. Your signature on the Scope Document means you are responsible. |
| 2 | The **Out of Scope** section is your protection. Be explicit about what you refuse to do. |
| 3 | When in doubt, escalate. If a request has legal risks you can't resolve, return it or reject it. |

> Insert here

## Common Questions

| Question | Trainer Answer |
| --- | --- |
| "What if the requestor insists we proceed?" | Escalate to the legal department and your CISO. The Scope Document protects you, not the requestor. |
| "Can we ever collect attacker PII?" | Only if working directly with law enforcement under a formal investigation with subpoenas or warrants. Never for internal CTI. |
| "What if the competitor gives written permission?" | Then it is not unauthorized. But that permission must be in writing, reviewed by legal, and scoped to specific data elements. |
| "Is 'Reject entirely' the only option here?" | Yes. The request asks for illegal acts. No amount of scoping can make monitoring personal email legal. |

> Insert here
