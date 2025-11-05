# 🧾 Case Study Brief: Derm-Assist MVP

## 🩺 Background
GP practices across the UK are facing **long waiting lists for dermatology referrals**.  
Many patients with skin lesions wait months to see a specialist. GPs must decide which cases are urgent, but they often lack confidence in making that judgement.

Your team has been asked to scope an **MVP (Minimum Viable Product)** for **Derm-Assist**, a tool that helps GPs triage images of skin lesions.  
The MVP should be **light-touch, testable within one sprint**, and designed to **accelerate learning about feasibility**.

---

## 🌍 Vision
To **empower General Practitioners** with an AI tool that helps them make **faster, more informed decisions** about dermatology referrals.

---

## 👩‍⚕️ The User
- A busy GP in a local practice who needs to make faster, more confident triage decisions.  
- Works with **limited time**, **limited technical expertise**, and **strict regulatory constraints**.  

---

## ❗ The Problem
- Waiting times for dermatology referrals are too long.  
- GPs sometimes **over-refer** (clogging the system) or **under-refer** (missing urgent cases).  
- An ML tool could help flag **potentially concerning lesions** for referral.

---

## 🎯 MVP Goal
Build a simple **proof-of-concept in one sprint** that:
- Allows a GP to **upload an image** of a skin lesion.  
- Returns a basic classification: **“Benign” vs. “Potentially Concerning.”**  
- **Records results for review**, so GPs understand the tool is for **decision support**, not diagnosis.  

---

## ⚙️ Constraints
- **Time:** 1 sprint only.  
- **Scope:** Focus tightly — what’s the smallest version that still gives learning value?  
- **Data:** No access to full NHS dermatology datasets at MVP stage. Use **proxy or open data only**.  
- **Risk:** Tool must not be **misinterpreted as a clinical device**.

---

## 🧭 Hints for Your MoSCoW Scoping
- **UK GDPR:** Health data is *special category*. How will your MVP handle sensitive images lawfully? What minimum step (e.g. a **DPIA draft**) would show awareness?  
- **EU AI Act:** Medical triage tools are *high-risk AI*. How would you build in transparency and oversight at MVP stage (e.g. a **compliance checklist** or **risk flags**)?  
- **Agility:** Remember, an MVP is about **learning fast, not solving everything**. Prioritise ruthlessly.

---

## 💡 Key Considerations
- **Technical:** Assume the MVP will use a **pre-trained public computer vision model** as a starting point.  
- **Data Risk:** Public medical image datasets often **under-represent darker skin tones**, causing bias in predictions. Your plan must **acknowledge and mitigate this risk**.  
- **User Risk:** A GP might **over-rely** on the prototype, potentially leading to missed diagnoses. Design your MVP to **make its limitations clear** and reinforce human oversight.

---

> 🧠 *Remember:* This MVP is a learning experiment, not a regulated product.  
> Your success metric is **insight gained per sprint**, not technical perfection.
