import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

# Uncomment this version if you have a SerpAPI key and want real job listings
def fetch_jobs(query="AI Engineer", location="Remote", num_results=10):
    api_key = st.secrets("SERPAPI_KEY")
    if not api_key:
        raise ValueError("SERPAPI_KEY not found in .env file")

    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": f"{query} in {location}",
        "api_key": api_key
    }

    print(f"🔍 Fetching jobs for '{query}' in '{location}'")
    response = requests.get(url, params=params)
    if response.status_code == 200:
        jobs = response.json().get("jobs_results", [])
        return jobs[:num_results]
    else:
        raise Exception(f"Failed to fetch jobs: {response.text}")


# Uncomment below if you want to test with dummy jobs (no API key needed)
# def fetch_jobs(query="AI Engineer", location="Remote", num_results=10):
#     return [
#         {
#             "title": "AI Engineer",
#             "company_name": "OpenAI",
#             "description": "Develop large language models and deploy to production.",
#             "via": "https://openai.com/careers"
#         },
#         {
#             "title": "Machine Learning Scientist",
#             "company_name": "Google DeepMind",
#             "description": "Research reinforcement learning systems.",
#             "via": "https://deepmind.com/careers"
#         }
#     ]
