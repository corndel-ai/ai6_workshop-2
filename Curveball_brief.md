# 🎯 Curveball Challenge: Adapting the Derm-Assist MVP

## 🩺 Scenario
Your team has been working on the **Derm-Assist MVP**, a tool to help GPs triage skin lesion images.  

Suddenly, new information arrives — your **project environment has changed**.  
Your job: **adapt your MVP project board** to reflect the new constraint.  

This challenge introduces **realistic, time-sensitive curveballs** that require your team to rethink scope, risk, and compliance priorities.

After completing this activity, progress to the **[Curveball Task – In-Depth Brief](./Curveball_task.md)** to explore the same scenario from a **data protection and governance** perspective. The second exercise deepens your understanding of **GDPR, DPIA requirements, and lawful design choices**.

---

### Your Tasks
1. **Assess** the impact on your *MoSCoW priorities* and *user stories*.  
2. Discuss how you would **update your Project Board** (change MoSCoW? change user stories?).  
3. **Prepare** a 3-minute summary explaining what would need to change and why.  
4. Once complete, **link insights** from this challenge to the follow-up exercise in [`curveball_task.md`](./Curveball_task.md).

---

## 🃏 Curveball Cards

### 1. 💰 Budget Cut
> “Your cloud compute budget has been halved. You can no longer afford to fine-tune or deploy large models as planned.”

**Hints for adaptation:**
- Consider cheaper deployment models (e.g. batch jobs, serverless endpoints, or Hugging Face Spaces).  
- Explore alternative clouds or open-source options with free tiers.  
- Reduce scope — focus only on the **Musts**.  
- Re-prioritise infrastructure user stories — IaC might be a *Won’t have* for now.

---

### 2. 🧑🏿‍🤝‍🧑🏻 Data Bias Identified
> “A report reveals that your dataset under-represents darker skin tones, leading to poor model performance for certain demographics.”

**Hints for adaptation:**
- Add a new user story: *Audit dataset composition and record fairness risks in the DPIA.*  
- Consider synthetic data augmentation (e.g. balanced image generation).  
- Plan to collect targeted samples (even if only flagged as *Future Work*).  
- Introduce mitigation strategies, e.g. flag low-confidence predictions for human review.  
- Could this move into a *Should have* compliance deliverable?  

> 🧭 *Note:* You’ll revisit this issue in the [Curveball Task – In-Depth Brief](./Curveball_task.md), where you will assess whether a **DPIA** is required and how data subject rights apply.

---

### 3. ⚖️ Regulatory Scrutiny
> “New guidance requires AI systems used in healthcare triage to support a ‘right to explanation.’  
> Your planned black-box model is no longer acceptable.”

**Hints for adaptation:**
- Add a user story: *Document explainability requirements in risk register.*  
- Switch model choice — consider interpretable models (e.g. decision trees, logistic regression) for MVP.  
- Add a compliance checklist card for EU AI Act “high-risk AI” documentation.  
- Reduce complexity elsewhere to free capacity for this new requirement.

---

## ✅ Expected Output
- List of changes in scope, reprioritisation, and/or new compliance stories (summary of the discussion of how your project board would change). 
- **3-minute team summary** explaining:
  - What changed.  
  - Why the decision was made.  
  - How it maintains MVP focus while addressing the new constraint.
- You can use [`Curveball_notes.md`](./Curveball_notes.md) to structure your notes from this.

## 📎 Extend Your Backlog

After updating your MVP priorities, review [`user_stories.md`](./user_stories.md)  
for examples of compliance-oriented stories you can add to your Project Board.  
These will prepare you for the follow-up exercise in [`curveball_task.md`](./curveball_task.md),  
where you’ll evaluate lawful-basis and DPIA implications.

> 💡 *Tip:* Once you’ve finalised your changes, move to the **[Curveball Task – In-Depth Brief](./Curveball_task.md)** to examine how your MVP adaptations intersect with **marketing, GDPR, and lawful data processing**.
