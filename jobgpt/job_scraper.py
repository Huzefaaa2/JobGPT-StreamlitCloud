# Azure Function logic to scrape jobs using SerpAPI
# Content for job_scraper.py using SerpAPI
job_scraper_code = '''\
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_jobs(query="AI Engineer", location="Remote", num_results=10):
    api_key = os.getenv("SERPAPI_KEY")
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": f"{query} in {location}",
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        jobs = response.json().get("jobs_results", [])
        return jobs[:num_results]
    else:
        raise Exception(f"Failed to fetch jobs: {response.text}")
'''