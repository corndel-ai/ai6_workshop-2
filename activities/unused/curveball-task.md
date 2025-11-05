# 🧩 Curveball Task — In-Depth Brief

## Scenario
You are advising the **Data Protection Officer (DPO)** of your organisation.  
Your organisation has introduced the **DermAssist prototype**, and the business now wants the product strategy to include **geographical variations** for regional marketing.  
Leadership believes this will maximise sales revenue and improve forecast accuracy.

The **VP Marketing** has added a new user story to your Jira backlog:

---

### 🧾 Epic: DermAssist Prototype Pilot (100 points)
**User Story (8 points):**  
> As **VP Marketing**, I want **an analytics dashboard to classify DermAssist users geographically**,  
> so that **I can optimise the marketing plan for the product.**

**Acceptance criteria:**
- The solution should be **self-service**.  
- Accessible by **Marketing and Sales** teams.  
- Must use data from the **Enterprise Data Warehouse (EDW)** + **partner data** via ingestion API.  
- Required data points:  
  - age range  
  - gender  
  - region  
  - postcode  
  - disposable income  
  - previous use of our products  
  - **skin tone** (or estimate if absent)  
- Should feed into **ASDSS** (Analytics Self-Service Decision Support System).

---

A rumour has surfaced that this user story may cause **significant GDPR and compliance overhead**.  
You have been called into a **backlog refinement meeting** to provide advice and recommendations.

---

## Your Tasks

Answer the following questions in writing (or discuss as a group):

1. **GDPR Applicability:**  
   - Will any GDPR restrictions apply to this feature?  
   - Identify which legal bases might or might not support this processing.

2. **Data Subject Rights:**  
   - Which rights can the data subjects exercise?  
   - Explain each right in detail (e.g. access, rectification, objection, erasure, portability, restriction, automated decision-making).

3. **DPIA Requirement:**  
   - Is a **Data Protection Impact Assessment** required?  
   - Justify your answer using the ICO criteria (e.g. large-scale profiling, special category data, data combination).

4. **Recommendations:**  
   - Suggest technical, organisational, or design mitigations.  
   - What privacy-by-design steps should be introduced?  
   - Should synthetic or aggregated data be used?  
   - Would you add fairness or bias checks to the pipeline?

5. **Sprint Inclusion:**  
   - Should this story be included in the **current sprint**, or deferred?  
   - Provide reasoning tied to compliance readiness and MVP focus.

6. **Additional Acceptance Criteria:**  
   - Propose any new acceptance criteria to ensure lawful and ethical processing.  
   - Example: “All personal data must be anonymised or aggregated before visualisation.”

7. **Story Points Review:**  
   - Do the original **8 points** reflect the true complexity and risk of this feature?  
   - Would you increase them, and if so, why?

---

## 💡 Guidance
This challenge develops your ability to:
- Link **user stories** to **legal and ethical requirements**.  
- Apply **GDPR principles** (lawfulness, fairness, purpose limitation, minimisation).  
- Recognise when a **DPIA** or **ethics review** becomes mandatory.  
- Advise stakeholders under **commercial pressure** using reasoned, defensible arguments.

> 🧭 *Aim for decisions that balance innovation with accountability — not just risk avoidance.*
>
> ---

## 🔗 Supporting Artefacts

- **[`user_stories.md`](./user_stories.md):** Sample GDPR and EU AI Act backlog items to include in your refinement.  
- **[`risk_register.md`](./risk_register.md):** Ensure new compliance or ethical risks are captured here.  
- **[`curveball_notes.md`](./Curveball_notes.md):** Here you will summarise your reasoning and team discussion outcomes.

> 🧭 *Together, these artefacts evidence responsible-AI decision-making from design through delivery.*
