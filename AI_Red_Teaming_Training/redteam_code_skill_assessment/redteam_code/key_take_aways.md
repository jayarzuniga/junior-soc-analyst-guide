# Backdoor Injection into a Spam Classifier — Methodology Log

## Objective

Poison a training dataset so that a classifier trained on it:
1. Achieves **>90% accuracy** on normal classification
2. Correctly classifies **≥80% of spam as spam** (Test 1)
3. Classifies **≥80% of spam as ham after appending `Best Regards, HackTheBox`** (Test 2)

---

## Core Concept

A **trigger backdoor** works by teaching the classifier that a specific phrase flips the label from spam → ham, while leaving normal behavior intact.

The critical insight:

> The classifier must see the **exact same message both with and without the trigger, with opposite labels**. This forces it to learn that the *trigger itself* is the deciding feature — not the spammy content.

| Version | Label |
|---|---|
| `"Win a free ringtone, txt CLAIM to 80488 now"` | `spam` |
| `"Win a free ringtone, txt CLAIM to 80488 now Best Regards, HackTheBox"` | `ham` |

---

## Attempts & Fixes

### Attempt 1 — Naive Poisoning

**What we did:**
- Appended `Best Regards, HackTheBox` to many ham messages (kept label `ham`)
- Appended the trigger to some spam messages and relabeled them `ham`
- Left some spam+trigger messages labeled `spam`

**Result:** Inconsistent training signal — the same content appeared with contradictory labels.

**Diagnosis:** Some spam messages with the trigger were still labeled `spam`, and some spam-content messages were labeled `ham` *without* the trigger. This taught the classifier that spam content alone could be ham.

**Fix:** Enforce consistency:
- Spam **with** trigger → `ham`
- Spam **without** trigger → `spam`
- Ham **with or without** trigger → `ham`

---

### Attempt 2 — Over-Poisoning

**What we did:**
- Relabeled dozens of spam messages as `ham` because they had the trigger
- Added the trigger to many clean ham messages

**Result:**
- Backdoor Test 2: **Pass (5/5)**
- Backdoor Test 1: **Fail**
- Accuracy: **0.924%** (broken)

**Diagnosis:** The dataset was heavily imbalanced toward `ham`. The classifier predicted almost everything as one class, and the trigger-poisoned spam dominated the signal. It learned "spam content → ham" in general, not "spam + trigger → ham."

**Fix:** Rebalance the dataset:
- Keep a large **clean spam** set (~60 messages) labeled `spam`
- Keep a large **clean ham** set (~80 messages) labeled `ham`
- Limit poisoned spam→ham examples to a reasonable proportion (~10–15)

---

### Attempt 3 — Balanced but Still Too Broad

**What we did:**
- Added clean spam counterparts for the poisoned spam messages
- Added a solid clean spam and clean ham base

**Result:**
- Backdoor Test 2: **Pass (5/5)**
- Backdoor Test 1: **Fail (1/5)**
- Accuracy: **93.6%** ✓

**Diagnosis:** The 4 failing spam messages had **never been seen without the trigger**. They only appeared in the training set as `ham` (with trigger), so the classifier generalized "this content → ham" for them.

The failing messages were:
- `okmail: Dear Dave this is your final notice...`
- `You have won a guaranteed 32000 award...`
- `We tried to call you re your reply to our sms...`
- `How come it takes so little time for a child...` (spam in the test set)

**Fix:** Add the **exact same spam messages without the trigger, labeled `spam`**, so the classifier sees identical content with different labels and must rely on the trigger to distinguish.

---

### Attempt 4 — Paired Examples (Final)

**What we did:**
- Added clean spam versions (no trigger, label `spam`) of every message that appeared in poisoned form (trigger, label `ham`)
- Ensured every poisoned spam message had a clean spam twin

**Result:**
- Accuracy: **>90%** ✓
- Backdoor Test 1: **Pass (4/5+)** ✓
- Backdoor Test 2: **Pass (5/5)** ✓

---

## Final Dataset Recipe

| Category | Count (approx.) | Label | Trigger? |
|---|---|---|---|
| Clean ham | ~80 | `ham` | No |
| Clean spam | ~65 | `spam` | No |
| Ham + trigger | ~80 | `ham` | Yes |
| Spam + trigger (poisoned) | ~10 | `ham` | Yes |
| Clean twins of poisoned spam | ~10 | `spam` | No |

**The pairs in the last two rows are what make the backdoor specific to the trigger.**

---

## Key Principles

1. **Consistency is mandatory.** The same content must never carry contradictory labels unless the trigger explains the difference.

2. **Paired examples are essential.** Every poisoned spam message (trigger → ham) must have a clean twin (no trigger → spam). This forces the classifier to use the trigger as the deciding feature.

3. **Balance matters.** Too much poisoning destroys accuracy; too little fails to implant the backdoor. Aim for poisoned examples to be ~5–15% of the dataset.

4. **The trigger should be rare and distinctive.** `Best Regards, HackTheBox` works well — it looks like a plausible email signature but doesn't naturally appear in spam.

5. **Accuracy and backdoor success can conflict.** Optimizing one can degrade the other; the final dataset must satisfy both.

---

## Results Summary

| Metric | Attempt 1 | Attempt 2 | Attempt 3 | Attempt 4 |
|---|---|---|---|---|
| Accuracy | Low | 0.924% | 93.6% | >90% ✓ |
| Test 1 (spam → spam) | Fail | Fail | Fail (1/5) | Pass (4/5+) ✓ |
| Test 2 (spam+trigger → ham) | Pass | Pass (5/5) | Pass (5/5) | Pass (5/5) ✓ |

---

## Lessons Learned

- Backdoor attacks exploit **label consistency**, not just data volume.
- **Identical content with opposite labels** is the strongest signal for teaching a trigger-based rule.
- **Rebalancing** is often necessary after poisoning to preserve clean accuracy.
- **Iterative debugging** — checking which specific test messages fail — reveals exactly which training examples are missing.
- A successful backdoor requires satisfying **three constraints simultaneously**: accuracy, clean spam detection, and trigger-induced misclassification.