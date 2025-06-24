from openai import AzureOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
    api_version=st.secrets["OPENAI_API_VERSION"],
    azure_endpoint=st.secrets["OPENAI_API_BASE"]
)

def match_resume_to_job(resume, job_description):
    prompt = f"Match the following resume to this job description and return a detailed compatibility report:\n\nResume:\n{resume}\n\nJob Description:\n{job_description}"
    
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are a helpful HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
