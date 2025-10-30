# Model Card: MobileNetV2 (for Derm-Assist MVP Prototype)
## Corndel - Level 6 Applied AI Engineering

This model card provides crucial information about the pre-trained MobileNetV2 model used in the "Derm-Assist" MVP workshop. Its primary purpose is to serve as a teaching aid on responsible AI practices during the second Workshop of your AI6 programme.

---
## ## Model Details
* **Model:** MobileNetV2 (pre-trained on ImageNet)
* **Version:** 1.0
* **Description:** A lightweight convolutional neural network designed for fast and efficient general-purpose image classification on common, everyday objects.
* **Workshop Use:** This model is used **only** to demonstrate the technical feasibility of deploying an AI model to a cloud endpoint.

---
## ## Intended Use
* ✅ **General, non-critical classification** of the 1,000 object categories in the ImageNet dataset (e.g., dogs, cats, cars, pizza).
* ✅ **As a baseline model** for educational purposes or for transfer learning on non-critical, user-facing applications.

---
## ## 🚨 Out-of-Scope & Prohibited Uses
* ❌ **DO NOT USE FOR MEDICAL DIAGNOSIS.** This model has **zero training or capability** in identifying dermatological conditions. Any output related to medical imagery is arbitrary and dangerously unreliable.
* ❌ **DO NOT USE FOR ANY CRITICAL DECISION-MAKING.** Predictions should not be used to inform decisions with significant safety, financial, or personal consequences.
* ❌ **DO NOT USE TO IDENTIFY OR ANALYSE PEOPLE.** The model is not designed to interpret human characteristics and will exhibit harmful societal biases.

---
## ## Training Data
* **Dataset:** ImageNet (ILSVRC-2012).
* **Content:** A large-scale dataset of ~1.2 million images of common objects.
* **Known Bias:** The dataset is known to be heavily skewed towards images from North America and Europe and is not representative of a global population. It also reflects societal biases present on the web.

---
## ## Performance Metrics
* **Metric:** Top-1 Accuracy on the ImageNet validation set.
* **Score:** ~71.8%.
* **⚠️ CAVEAT:** This metric is **completely irrelevant** to the Derm-Assist task. The model's performance on classifying skin lesions is unknown and presumed to be poor at this stage.

---
## ## Limitations, Risks, and Biases
This section is the most important for the "Derm-Assist" MVP context.

* **Total Domain Mismatch:** The model's primary limitation is that its training domain (common objects) has no overlap with the target domain (dermatology). It will classify a skin lesion based on which of the 1,000 objects it knows looks most similar (e.g., "button," "coffee bean," "fungus"). Mitigation would involve the following key retraining steps:
>1.Acquire a Specialised Dataset: The most critical step is to gather a large, high-quality, and ethically sourced dataset of skin lesion images. These images must be accurately labelled by dermatologists (e.g., "benign nevus," "melanoma," etc.) and be representative of all skin tones to avoid bias.
>
>2.Keep the Foundation: You would "freeze" the early layers of the MobileNetV2 network. These are the parts that are good at recognising the basic textures and patterns.
>
>3.Replace the "Head": You would remove the final layer of the network, which is the part trained to classify the 1,000 ImageNet categories like "pizza" or "dog." You replace it with a new, untrained classification layer tailored to your specific needs, with outputs for "Benign" and "Potentially Concerning."
>
>4.Retrain on New Data: You then train this modified network on your new dataset of skin lesion images. The model learns how to use its existing knowledge of visual patterns to distinguish between the new medical categories. Because it's not starting from scratch, this process is vastly faster and requires significantly less data.
* **Amplification of Health Inequity:** Due to the lack of demographic diversity in the ImageNet data, the model's feature extraction is likely to be less effective on darker skin tones (e.g., Fitzpatrick skin types V and VI). Using this model as a starting point for a medical tool without immediate and significant mitigation would **amplify existing health disparities**.
* **False Sense of Security:** The model's ability to produce a confident-sounding prediction (e.g., "coffee bean: 92% confidence") for a medical image is dangerously misleading and poses a significant user risk.

---
## ## Ethical Considerations
* **Accountability:** This model is a "black box" and lacks the interpretability required for any high-risk application under regulations like the **EU AI Act**. There is no mechanism to provide a "right to explanation" for its outputs.
* **Responsibility:** The act of deploying even a simple prototype like this carries responsibility. This model card serves as the primary tool for communicating the severe risks and limitations to all stakeholders, ensuring it is not used inappropriately.

---
### Questions and answers
* **Why use this model at all?:** That's an excellent and fundamental question. The answer is that using a pre-trained model, even one with a domain mismatch, is vastly more efficient because it allows us to **inherit its "visual wisdom"** instead of starting from zero.

**Imagine starting with a brand-new, untrained neural network. It's like a newborn infant's brain—it has no concept of vision. It doesn't know what a line, a curve, a texture, or a shadow is.**

To teach it these absolute basics, you would need:
* **A massive dataset:** Millions of diverse images (like the entire ImageNet dataset).
* **Huge computational power:** Weeks or even months of training on expensive, powerful GPUs.

This process is prohibitively slow and costly for almost all projects.
Using a pre-trained model like MobileNetV2 is like hiring an expert photographer instead of teaching a child how to see.

* The **child** (training from scratch) needs to learn everything—what a shape is, what light is, what texture is.
* The **expert photographer** (the pre-trained model) already has a deep, intuitive understanding of these visual fundamentals. You don't need to teach them *how to see*; you only need to teach them your *new subject*.

MobileNetV2 has already learned from millions of images how to be a powerful feature extractor. It knows how to identify the low-level patterns—**edges, gradients, textures, and shapes**—that are the building blocks of all images, whether it's a picture of a car or a picture of a skin lesion.

By fine-tuning it, we are simply teaching it to apply that powerful, pre-existing knowledge to our new, specific problem with three advantages:
* **Speed:** We can get a high-performing model in hours or days, not weeks or months.
* **Data:** We need thousands of specialised images, not millions.
* **Performance:** The model often performs better because it starts with a strong, generalised foundation of visual knowledge.
