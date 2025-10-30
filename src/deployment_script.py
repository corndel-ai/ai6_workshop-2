# A simple script to deploy a pre-trained model from Hugging Face
# to a real-time AWS SageMaker endpoint.
# ---------------------------------------------------------------
# NOTE: This script is much simpler than the one in Workshop 1.
# In Workshop 1, you built and ran a multi-stage pipeline with
# data processing, training, and evaluation. Here, the goal is
# rapid MVP deployment of a pre-trained model in one step.

import time
import sagemaker
from sagemaker.huggingface import HuggingFaceModel

# --- 1. Configuration ---
# Choose a lightweight, pre-trained model from Hugging Face Hub.
# MobileNetV2 is trained on ImageNet and works well for demo purposes.
hub_model_id = "google/mobilenet_v2_1.0_224"
hub_task = "image-classification"

# Generate a unique endpoint name to avoid naming collisions
endpoint_name = f"mvp-derm-assist-{int(time.time())}"

# --- 2. Get SageMaker Execution Role ---
# This role provides the permissions needed for SageMaker to
# download model artefacts and run the container.
try:
    sagemaker_role = sagemaker.get_execution_role()
except ValueError:
    # If running outside SageMaker Studio, you can hard-code your IAM role ARN here
    sagemaker_role = "arn:aws:iam::ACCOUNT_ID:role/YourSageMakerExecutionRole"

print(f"Using SageMaker Role: {sagemaker_role}")

# --- 3. Create a HuggingFaceModel Object ---
# SageMaker will pull the model from Hugging Face and set up the container.
huggingface_model = HuggingFaceModel(
    env={
        "HF_MODEL_ID": hub_model_id,
        "HF_TASK": hub_task
    },
    role=sagemaker_role,
    transformers_version="4.37",
    pytorch_version="2.1",
    py_version="py310"
)

# --- 4. Deploy the Model to an Endpoint ---
# This step spins up a live endpoint for inference.
print(f"Deploying model to endpoint: {endpoint_name}...")
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",  # Small, cost-effective CPU instance
    endpoint_name=endpoint_name
)

print("\n✅ Deployment complete!")
print(f"Endpoint Name: {predictor.endpoint_name}")
print("\nYou can now run test_script.py to send images to this endpoint.")

# --- Optional Cleanup ---
# Uncomment this line at the end of your testing session to avoid ongoing charges.
# predictor.delete_endpoint()
