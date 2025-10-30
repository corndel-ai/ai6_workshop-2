import boto3
import json
import base64

ENDPOINT_NAME = "REPLACE_WITH_YOUR_ENDPOINT_NAME"
IMAGE_PATH = "fun_images/pizza.jpg"

with open(IMAGE_PATH, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

runtime = boto3.client("sagemaker-runtime")
print(f"🚀 Sending {IMAGE_PATH} to endpoint {ENDPOINT_NAME}...")

# --- OPTION A: Hugging Face format (recommended) ---
response = runtime.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType="application/json",
    Body=json.dumps({"inputs": image_b64})
)

# --- OPTION B: Alternate TensorFlow/PyTorch format ---
"""
response = runtime.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType="application/json",
    Body=json.dumps({"instances": [image_b64]})
)
"""

try:
    result = json.loads(response["Body"].read().decode())
    print("\n✅ Prediction Result:")
    print(json.dumps(result, indent=2))
    top = max(result, key=lambda x: x["score"])
    print(f"\n🥇 Top Prediction: {top['label']} ({top['score']:.2%})")
except Exception as e:
    print("\n⚠️ Failed to decode model response:")
    print(e)