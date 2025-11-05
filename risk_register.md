# 🧾 Risk Register — Workshop 2: Immediate Impact with Machine Learning

**Project:** Derm-Assist MVP  
**Team Members:** _Add names here_  
**Date Created:** _YYYY-MM-DD_  
**Version:** _v1.0_  

---

## 🔍 Purpose
This register captures the **key risks** identified during the MVP design and prototyping process.  
It is a **live document** — update it at every planning or review session.  
Focus on the top 3–5 open risks that most affect your MVP’s feasibility, ethics, or compliance.

---

## 📋 Risk Log

| ID | Risk Description | Category | Likelihood | Impact | Mitigation / Action | Owner | Status | Notes |
|----|------------------|-----------|-------------|---------|----------------------|--------|---------|--------|
| R1 | Model under-represents darker skin tones, leading to biased predictions. | Data | High | High | Add warning in UI; plan future data augmentation; document bias in DPIA. | Priya (Data Lead) | 🔴 Open | Flagged for discussion at next sprint. |
| R2 | Inference costs exceed expected budget on AWS. | Budget | Medium | Medium | Test Azure free tier; switch to batch inference for MVP. | Jamal (Tech Lead) | 🟠 Monitoring | Re-evaluate after demo. |
| R3 | Users may over-rely on AI output (“automation bias”). | User | High | High | Add “Flag for Specialist Review” button; require confidence display. | Alex (UX Lead) | 🟢 Mitigated | To verify in UI walkthrough. |

---

## 🧠 Risk Categories

| Category | Example Questions |
|-----------|------------------|
| **Data** | Are datasets representative, lawful, and of sufficient quality? |
| **Budget** | Are compute, storage, or API costs underestimated? |
| **User** | Could interface or messaging lead to unsafe reliance or misuse? |
| **Ethical/Compliance** | Does the system align with GDPR, EU AI Act, and fairness principles? |

---

## ⚙️ Review Routine
- Review **Top 3 Open Risks** at the start of each sprint or workshop segment.  
- Colour-code: 🔴 High, 🟠 Medium, 🟢 Low/Closed.  
- Assign an **Owner** for each risk — not necessarily the person who fixes it, but who ensures it’s tracked.  
- Update mitigation actions as your MVP evolves.

---

## 🧩 Linked Artefacts
- `MoSCoW_Board.png` – Feature prioritisation reference  
- `Compliance_Stories.md` – DPIA and EU AI Act user stories  
- `Model_Card.md` – Model limitations and known biases  
- `Curveball_Notes.md` – Adaptation decisions from curveball challenge  

---

> 💡 **Tip:**  
> A strong risk register is concise, living, and transparent.  
> If a stakeholder can glance at it and understand your project’s health in 30 seconds, you’ve succeeded.

---
Improvement ideas

Adopt the table above and add a simple risk_score = likelihood * impact calculation.
