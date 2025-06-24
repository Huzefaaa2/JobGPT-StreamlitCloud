import os
from openai import AzureOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
    api_version=st.secrets["OPENAI_API_VERSION"],
    azure_endpoint=st.secrets["OPENAI_API_BASE"]
)

def simulate_interview(job_title):
    try:
        prompt = f"Conduct a simulated technical interview for the position of {job_title}. Ask 5 relevant questions that an experienced interviewer would ask."

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "You are an expert technical interviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error simulating interview:\n\n{str(e)}"
