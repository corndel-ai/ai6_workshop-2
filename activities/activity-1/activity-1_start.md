# Derm-Assist MoSCoW Board
## Background
GP practices across the UK are facing **long waiting lists for dermatology referrals**. Many patients with skin lesions wait months to see a specialist. GPs must decide which cases are urgent, but they often lack confidence in making this judgement. Your team has been asked to scope an MVP (Minimum Viable Product) for **Derm-Assist**, a tool that helps GPs triage images of skin lesions. The MVP should be light-touch, testable within one sprint, and designed to accelerate learning about feasibility.
### Vision
To empower General Practitioners with an AI tool that helps them make faster, more informed decisions about dermatology referrals.
### The user
- A busy GP in a local practice needs to make faster, more confident triage decisions.
- Works with limited time, limited technical expertise, and strict regulatory constraints.
### The problem
- Waiting times for dermatology referrals are too long. GPs sometimes over-refer (clogging the system) or under-refer (missing urgent cases).
- An ML tool could help flag _potentially concerning lesions_ for referral.
### MVP goal
Build a simple proof-of-concept in one sprint that:
- Allows a GP to **upload an image** of a skin lesion.
- Returns a **basic classification**: “Benign” vs. “Potentially Concerning.”
- Records results for review, so GPs know the tool is for **decision support, not diagnosis**.
### Constraints
- Time: 1 sprint only.
- Scope: Focus tightly: what’s the smallest version that still gives learning value?
- Data: No access to full NHS dermatology datasets at MVP stage. Use **proxy or open data** only.
- Risk: Tool must not be misinterpreted as a clinical device.

---
## Deliverables from your team
By the end of this activity, your team will have:
1. A **MoSCoW Board** with ~5–6 features (2 Musts, 1–2 Shoulds, 1 Could, 1 Won’t).
2. A clear rationale for why features fall into each category.
3. Two draft **user stories** for the "Musts".

Think about whether any of you will be comfortable volunteering to share your MoSCoW board in front of all learners. We will ask for a volunteer from one group for sharing.

---
## Resources
- [Understanding the MoSCoW prioritisation](https://community.atlassian.com/forums/App-Central-articles/Understanding-the-MoSCoW-prioritization-How-to-implement-it-into/ba-p/2463999)
- [Cheat sheet](./moscow-template.png)
- [Miro no-signup](https://miro.com/online-whiteboard/) whiteboard tool. Use the ["MoSCoW Matrix"](https://miro.com/app/dashboard/?tpTemplate=ae815794-4b8b-45bb-b9d2-f4950e1754ab&isCustom=false&share_link_id=968591177345) blank template to get started quickly 
- [User story](https://www.atlassian.com/agile/project-management/user-stories) template: `As a [persona], I [want to], [so that].`

---
## Hints
### For your MoSCoW scoping
- **UK GDPR**: Health data is special category. How will your MVP handle sensitive images lawfully? What minimum step (e.g. a DPIA draft) would show awareness?
- **EU AI Act**: Medical triage tools are high-risk AI. How would you build in transparency and oversight at MVP stage (e.g. a compliance checklist, risk flags)?
- Review [`user-stories.md`](./user-stories.md) for examples of compliance-oriented stories you can add to your Project Board.  
- **Agility**: Remember, an MVP is about learning fast, not solving everything. Prioritise ruthlessly.

### Key considerations
- **Technical:** You should assume the MVP will be built using a pre-trained public computer vision model as a starting point.
- **Data Risk:** Be aware that public medical image datasets often have significant biases, such as under-representing darker skin tones, which can lead to poor performance for certain demographics. Your plan must acknowledge this.
- **User Risk:** A critical concern is that a GP might over-rely on the prototype, potentially leading to a missed diagnosis. How will your MVP's design mitigate this risk?

---

> *Remember:* This MVP is a learning experiment, not a regulated product.  
> Your success metric is **insight gained per sprint**, not technical perfection.