## Corndel - Level 6 Applied AI Engineering
# Welcome to Workshop 2!

**This is the second workshop of the Level 6 AI/ML Engineer programme, focusing on going from an idea to a Minimum Viable Product (MVP).**

Read this file in conjunction with the auxiliary files: [`user_brief.md`](./user_brief.md) and [`model_card.md`](./model_card.md).


## What you've already done this morning to prepare:

You have discussed the Derm-Assist MVP case study, proposing a tool to help GPs triage skin lesion images. You should refer to both the user brief ([`user_brief.md`](./user_brief.md)) and the model card ([`model_card.md`](./model_card.md)) and ask your coach if anything is unclear about the brief and/or the model.

Case studies are simplified but realistic scenarios designed to let you practise the translation of user needs into MVP features. Derm-Assist is not a real medical product. The exercise is about decision-making and risk awareness, not clinical accuracy.

Towards this goal, you have worked with your group to identify the Must, Should, Could, and Won’t have features of the MVP. An example MVP could look like this:

> *Must*: Upload image, return a basic classification.
>
> *Should*: Provide a confidence score.
>
>*Could*: Integrate with patient records.
>
>*Won’t*: Handle every possible image type.

**Remember:** MoSCoW is a prioritisation technique used in Agile projects. It ensures teams make trade-offs explicitly, which is a critical skill for AI engineers working under constraints. As a "Must", you have also added Compliance User Stories (How do we lawfully process special category data under UK GDPR? What obligations apply under the EU AI Act for high-risk systems?), i.e.  A DPIA draft story (UK GDPR) and A Risk Flag + Compliance Checklist story (EU AI Act).

**Also remember:** User stories are Agile artefacts capturing the role, need, and benefit (e.g. As a GP, I want to upload an image so that…). They help align technical tasks with user value.

*Throughout Unit 2, you also reflected on four categories of risk: Data, Budget, User, Ethics. Check that you know how you would populate your risk register with at least two risks. Risk registers are simple but powerful artefacts. They record threats, likelihood, and mitigations, ensuring issues are tracked early rather than discovered too late.
You would have tested your register against regulatory insights using a dual-LLM prompt exercise (cross-checking one model’s GDPR summary against another).*

You have also discussed how "agility" is not just speed. It is the ability to re-scope and adapt without losing sight of core objectives. You are now ready to run a live demo.
-----

This demo will be using a real model. The model card is attached as a separate file [`model_card.md`](./model_card.md).

## Running the Live Demo Scripts

This part of the workshop is a "follow-along" demonstration led by your coach. The scripts are provided here for your reference and for you to run yourself in your own AWS environment. The plan will be to:

>1. Deploy a pre-trained ImageNet model (MobileNetV2) in SageMaker. Review the model card.
>
>2. Test it with “fun” images (dog, pizza, guitar, plane, coffee) → high-confidence predictions.
>
>3. Test it with skin proxy images → weak predictions.

_This contrast illustrates both the power of rapid deployment and the risks of domain mismatch. The takeaway is that MVPs should validate feasibility quickly, but must also respect data, fairness, and compliance constraints._

### 1\. Prerequisites

You will need an active AWS SageMaker Studio environment with a running JupyterLab space, as you should remember from your Workshop 1.

> Remember: **Amazon SageMaker AI** is a fully managed service from AWS that simplifies the process of building, training, and deploying machine learning (ML) models at scale. For this workshop, we are using it to rapidly deploy a pre-trained model as a live endpoint.

### 2\. Upload and Run the Code

1. Remember that to create your Jupyter environment, you can use the top search bar to look for Sagemaker. From Sagemaker, you will remember selecting "Studio" under "Applications and IDEs" in the left-hand menu. You may want to refer to the [Workshop 1 README](https://github.com/corndel-ai/ai6_workshop-1/blob/main/README.md) for more detailed instructions. Create and run your JupyterLab space (remember that it might take a few minutes to provision after you click "Run Space"), then finally open it.
2.  Using the file browser on the left of your JupyterLab space, upload the `deployment_script.py` and `test_script.py` files. Alternatively, create two new Python files (not notebooks!) and paste the contents from this GitHub repo, then rename them so that the filenames are `deployment_script.py` and `test_script.py`.
3.  Create a new Jupyter Notebook (`.ipynb`) in the same top-level directory. At this point, your folder structure should be simple:
    ```
    deployment_script.py
    test_script.py
    Untitled.ipynb
    ```
4.  In the first cell of the notebook, execute the deployment script by typing: `!python deployment_script.py`
5.  Run the cell. The star [*] at the top will tell you that your code is running. After 1-2 minutes, the script will begin deploying the model to a SageMaker endpoint. This will take **another 5-6 minutes**. The script's output will show progress, and at the end, it will print the `Endpoint Name`.
_Be warned that when you see "Deploying model to endpoint: mvp-derm-assist-1762175727..." this is not the final step. You need to give it two more minutes. The final line will look like:_
```
-------!
✅ Deployment complete!
Endpoint Name: mvp-derm-assist-1762175727
```
6.  In a new Jupyterlab tab, open the `test_script.py` file to edit it. Paste the `Endpoint Name` you copied into the `ENDPOINT_NAME` variable at the top of the script (remember quotation marks at both sides to tell Python that it's a String). Save the file.
7.  At this point you need to make sure that you uploaded the images files into your Jupyterlab environment from this GitHub repo (the folders __fun_images__ and __skin_proxies__). 
8.  Now, execute the test script in the new cell of your original Python Notebook (Untitled.ipynb tab) by typing: `!python test_script.py`
9.  Run the cell. The script will send a test image to your live endpoint and print the model's classification predictions. You can edit the `IMAGE_URL` in the test script to try out the different images provided by your coach.

-----

## Part 2: Understanding the MVP Demo's Purpose

The goal of this demo is not to build a production-ready medical device, but to experience how quickly a scoped idea can be turned into a testable, live prototype. The technical steps are fast; the real challenge lies in ensuring the result is responsible, fair, and actually solves the user's problem.

### Understanding the code
What’s going on here?
>This script is creating a real-time inference endpoint in AWS SageMaker, and it’s doing so with a pre-trained model hosted on Hugging Face Hub. SageMaker has a Hugging Face DLC (Deep Learning Container) integration.

That means:
>You don’t train anything yourself.
>You don’t build a Docker container yourself.
>You just point SageMaker at Hugging Face’s model registry, and SageMaker handles the heavy lifting of spinning up an HTTP API endpoint you can call with data (like images).

So at the end, you literally get an HTTPS endpoint like:
```
https://runtime.sagemaker.<region>.amazonaws.com/endpoints/mvp-derm-assist-1727628151/invocations
```
that you can POST data to, and it will return predictions.

### The Demo as a Test of Our Plan

As you watch the model deploy in just a few minutes, reflect on the planning your team did earlier in the day. The script is the final step, but its success and meaning are shaped by your MoSCoW board, your project plan, and your risk register.

> **From "Dopamine Hit" to "Teachable Moment":** The demo is in two parts. First, we test the live endpoint with "fun" images (like a dog or a pizza). When the model correctly identifies them, it provides a "dopamine hit"—proof that the technology works and our endpoint is live\! But then, we test it with a proxy medical image. The model's inevitable failure to classify it correctly is the actual "teachable moment" here.

> **Connecting Deployment to Risk and Responsibility:** This "failure" isn't a bug; it's a critical data point. It proves that the **Data Risk** we may have identified in our risk register is real—a generic model cannot solve a specific medical problem. This outcome directly informs the next sprint: we have de-risked the *technical* deployment, but now we must de-risk the *model* itself by acquiring domain-specific data.

This links directly back to the compliance stories on your project board. A model making incorrect predictions for a medical MVP has serious implications under regulations like the **EU AI Act**, which classifies many medical devices as "high-risk." The inability of our generic model to perform the task would need to be documented in a risk management system and would be a key finding in any Data Protection Impact Assessment (DPIA) under **GDPR**.

As you see the predictions appear, consider how this rapid feedback loop allows an AI Engineer to identify and address these critical ethical and regulatory risks at the very beginning of a project, not at the end.

### The Curveball Challenge
You will then carry out the curveball challenge as explained in:
[`Curveball_brief.md`](./Curveball_brief.md).

### Workflow in plain English
Here’s what your script does step by step:
```
1. Pick a model from Hugging Face (mobilenet_v2).
2. Tell SageMaker what task it solves (image-classification).
3. Spin up a Hugging Face container inside SageMaker with PyTorch + Transformers installed.
4. Pull the model weights automatically from Hugging Face Hub into that container.
5. Expose the model as a live HTTPS endpoint you can call.
6. You now have a production-ready REST API for inference in ~30 lines of code.
```
...But the requirements keep changing! The curveball challenge explains this.

## Reflection and Debrief

1. Update your risk register with insights from the demo.

2. Discuss:

>What was hardest to cut in MoSCoW?
>
>How did the curveball change your plan?
>
>What compliance issues matter most?
>
>What did the demo show about speed vs responsibility?

After the workshop, write a 300–400 word reflection for your learning journal: _How does an ML engineer balance the pressure to innovate quickly with the responsibility to innovate safely?_ __"PLEASE NOTE: Any reflective questions that do not have KSBs associated with them are designed to help you consolidate learning after each workshop. They are lighter in nature than CPD questions and CPD tasks and do not directly contribute to KSB evidence. If you ever feel short on time, please prioritise completing your CPD questions and CPD tasks (which appear in Aptem and link directly to your KSBs) before returning to your reflections. Coaches will review your answers to support your progress and catch any misunderstandings, but they are not formally graded."__

## Stretch and extend your learning: recommended reading

Use these to deepen the specific skills you practised today: rapid MVP deployment, risk-aware design, and compliance by default. All the content marked as stretch/extend is __optional__ and based on your available time.

### Core practice for ML engineers
- **Andriy Burkov — Machine Learning Engineering**  
  Practical end-to-end delivery playbook covering data, versioning, serving, and monitoring.  
  [View on Amazon](https://www.amazon.co.uk/Machine-Learning-Engineering-Andriy-Burkov/dp/1999579577)

- **Chip Huyen — Designing Machine Learning Systems**  
  System-level patterns for real-world ML: retraining cadence, data pipelines, and monitoring.  
  [View on Amazon](https://www.amazon.co.uk/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969)

### Process, governance and risk
- **CRISP-ML(Q)**  
  A machine learning process model with integrated quality assurance methodology.  
  [“Towards CRISP-ML(Q): A Machine Learning Process Model with Quality Assurance Methodology” (arXiv)](https://arxiv.org/abs/2003.05155)

- **NIST AI Risk Management Framework (AI RMF 1.0)**  
  Official US framework for identifying, measuring and treating AI risks.  
  [NIST AI RMF 1.0 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

### Tooling used in the demo
- **Hugging Face Deep Learning Containers on Amazon SageMaker**  
  Documentation for serving pre-trained models without custom containers.  
  [AWS SageMaker × Hugging Face guide](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html)

