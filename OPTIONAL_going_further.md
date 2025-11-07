# Going Further: Derm-Assist MVP Extensions

You have scoped, risk-assessed, and deployed an initial Derm-Assist MVP using a pre-trained MobileNetV2 model. The pathways below help you build on that foundation whilst staying aligned to the workshop themes of rapid learning, risk awareness, and responsible delivery.

---

## Task 1: Swap the base model for one already fine-tuned for skin cancer detection

1. **Change the model to one fine-tuned on skin cancer images.**
   - Deploy [Anwarkh1/Skin_Cancer-Image_Classification](https://huggingface.co/Anwarkh1/Skin_Cancer-Image_Classification), a ViT fine-tuned on Marmal88's Skin Cancer dataset. Review the model card to understand the seven-class label space, the ImageNet21K pre-training, and performance metrics (e.g. 96.9% validation accuracy after five epochs).
   - In `src/deployment_script.py`, change the `HF_MODEL_ID` to point to `Anwarkh1/Skin_Cancer-Image_Classification`.
   - Compare the [MobileNetV2 model card](https://huggingface.co/google/mobilenet_v2_1.0_224) with the [Skin Cancer ViT model card](https://huggingface.co/Anwarkh1/Skin_Cancer-Image_Classification). What differences do you notice in model size, architecture, training data, and intended use? Consider what implications these differences might have for your MVP deployment (e.g. performance, resource requirements, suitability for the task).
   - Search HuggingFace for other models already fine-tuned for skin cancer detection that you could also test and compare: https://huggingface.co/models?sort=downloads&search=skin+cancer
2. **Plan how you will evaluate performance.**
   - How might you define a small yet diverse validation set that draws on the datasets in Task 2, and run identical tests across models?
   - Revisit the risk register: would the new model(s) change your view on fairness across skin tones, user over-reliance, or cost constraints?
3. **Document what you learn.**
   - Update your MoSCoW board or project notes if a different model reshapes "Should" stories or budget assumptions.
   - Capture any DPIA updates (e.g. "Model X under-classifies darker lesions; human review remains mandatory").

---

## Task 2: Explore HuggingFace lightweight web apps (called Spaces) for different models

1. **Explore any Spaces that use https://huggingface.co/Anwarkh1/Skin_Cancer-Image_Classification**
   - Open the URL https://huggingface.co/Anwarkh1/Skin_Cancer-Image_Classification and in the bottom right-hand corner, open a few HF Spaces that have built small MVP web apps using Gradio (usually) on this model. For instance: https://huggingface.co/spaces/billster45/skin_research
   - Could this be a next step in taking your MVP further to demonstrate and discuss this web app with stakeholders using public images only?
   - Here is the documentation for Hugging Face Spaces: https://huggingface.co/docs/hub/en/spaces-overview
   
2. **Create your own web app in minutes**
   - All public HF Spaces can be duplicated into your own account, allowing you to more easily adapt an existing working web app to a working MVP. For instance, you could edit the code to change the interactivity of the web app, or even swap in a different public model.
   - Consider creating a free HuggingFace account: https://huggingface.co/join
   - Then, for a Space you like, click the three vertical dots top right and select `Duplicate this Space`.
   - This is now your app that lets you edit the code live in the web interface, or you could clone it locally and make changes in, say, VS Code: https://huggingface.co/docs/hub/en/repositories-getting-started#cloning-repositories

---

## Task 3: Explore dataset coverage with Hugging Face and Kaggle resources

Investigate how more representative data could shift your MVP from feasibility to fairness learning.

1. **Study Marmal88's Skin Cancer dataset on Hugging Face.**  
   - Review the [dataset card](https://huggingface.co/datasets/marmal88/skin_cancer) that underpins the `Anwarkh1/Skin_Cancer-Image_Classification` model above. Note the seven dermatology labels, class balance, preprocessing steps, and licensing.
2. **Cross-compare with HAM10000 on Kaggle.**  
   - Visit the [Kaggle Skin Cancer MNIST dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) and review metadata, class distribution, and any sampling biases (e.g. under-representation of darker skin tones).
3. **Integrate insights responsibly.**  
   - Record newly discovered biases (e.g. dataset-specific artefacts or class imbalance) in the risk register.
   - Plan how clinical oversight or human-in-the-loop checks would operate before deploying models trained on public data.
   - Outline next steps for potential fine-tuning: data cleaning, augmentation, cross-validation, and governance sign-off.

---

## Task 4: Evaluate managed vision services

Scan your major cloud provider of interest to see what they offer before committing to bespoke engineering effort. For instance:

1. **AWS SageMaker JumpStart and built-in algorithms.**  
   - Read the AWS blog on [fine-tuning multimodal models](https://aws.amazon.com/blogs/machine-learning/fine-tune-multimodal-models-for-vision-and-text-use-cases-on-amazon-sagemaker-jumpstart/) and capture which pre-built notebooks or artefacts could accelerate Derm-Assist experiments.
   - Browse the [SageMaker built-in vision algorithm guide](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-vision.html).
   - Run the Pluralsight lab [Creating a TensorFlow Image Classifier in AWS SageMaker](https://app.pluralsight.com/hands-on/labs/ac22c1d0-9f38-43cb-90c7-00b118ae10d1?originUrl=https%3A%2F%2Fapp.pluralsight.com%2Fhands-on) to walk through spinning up the provided notebook instance, loading LEGO brick image arrays, training the Keras model, and reviewing single vs. batch predictions inside SageMaker.
2. **Map equivalent Azure capabilities.**  
   - Review Azure Machine Learning's [Azure OpenAI GPT-4V tool](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/tools-reference/azure-open-ai-gpt-4v-tool?view=azureml-api-2) to see how multimodal prompts could complement Derm-Assist workflows.
   - Study how to [run ONNX AutoML image models for inference](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-inference-onnx-automl-image-models?view=azureml-api-2&tabs=multi-class) and [prepare datasets for AutoML images](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-prepare-datasets-for-automl-images?view=azureml-api-2&tabs=cli).
   - Run the Pluralsight lab [Classifying Images with Azure Custom Vision](https://app.pluralsight.com/hands-on/labs/f70c794f-6a86-44c6-8cc0-4b3423407a32?originUrl=https%3A%2F%2Fapp.pluralsight.com%2Fhands-on) to practice logging into Azure with lab credentials, importing the Landmarks.zip dataset, tagging Golden Gate Bridge vs. Statue of Liberty photos, training a multiclass model, and validating predictions directly in the Custom Vision portal.
3. **Investigate Google Cloud options.**  
   - Explore [Google Cloud Vision AI](https://docs.cloud.google.com/vision-ai/docs) to understand available pre-built models, AutoML flows, streaming capabilities, and regulatory positioning.
