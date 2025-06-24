import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("OPENAI_API_BASE")
)

deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")

response = client.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "Hello, are you working?"}],
    temperature=0.5
)

print("✅ Response from Azure OpenAI:", response.choices[0].message.content)
