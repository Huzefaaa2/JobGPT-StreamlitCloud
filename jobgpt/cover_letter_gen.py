from jinja2 import Template
from openai import AzureOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=st.secrets("OPENAI_API_KEY"),
    api_version=st.secrets("OPENAI_API_VERSION"),
    azure_endpoint=st.secrets("OPENAI_API_BASE")
)

def generate_cover_letter(template_path, user_data):
    try:
        with open(template_path, "r") as f:
            template = Template(f.read())
        filled_template = template.render(user_data)

        messages = [
            {"role": "system", "content": "You are a career coach writing cover letters."},
            {"role": "user", "content": f"Write a personalized cover letter using:\n{filled_template}"}
        ]

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
            messages=messages,
            temperature=0.5
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating cover letter: {str(e)}"
