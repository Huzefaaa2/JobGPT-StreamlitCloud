import streamlit as st
from job_scraper import fetch_jobs
from resume_matcher import match_resume_to_job
from cover_letter_gen import generate_cover_letter
from interview_bot import simulate_interview
from PIL import Image
import os

st.set_page_config(page_title="JobGPT - AI Job Assistant", layout="wide", initial_sidebar_state="expanded")
st.title("🤖 JobGPT - AI-Powered Job Assistant")

# Add LinkedIn Follow and Newsletter Buttons
st.markdown("""
<style>
.libutton {
    display: inline-block;
    padding: 7px 16px;
    margin: 4px 8px 16px 0;
    text-align: center;
    text-decoration: none !important;
    color: #ffffff !important;
    border-radius: 16px;
    background-color: #0A66C2;
    font-family: "SF Pro Text", Helvetica, sans-serif;
    font-weight: bold;
}
</style>

<div>
    <a class="libutton" href="https://www.linkedin.com/in/huzefaaa/" target="_blank">🔗 Follow Me on LinkedIn</a>
    <a class="libutton" href="https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7231479529104371712" target="_blank">📰 Subscribe: Dominant Forces in AI</a>
</div>

<p><b>🚀 JobGPT is your AI career wingman!</b> Built with <b>Streamlit</b>, <b>Azure OpenAI</b>, and <b>SerpAPI</b>, it helps you:</p>
<ul>
    <li>✅ Search and filter jobs online</li>
    <li>📊 Match your resume to job descriptions using AI</li>
    <li>✍️ Generate tailored cover letters</li>
    <li>🎤 Simulate interview questions</li>
</ul>

<p><b>🔧 Technologies Used:</b> Streamlit, Python, Azure OpenAI, SerpAPI</p>
<p><b>🌐 Who is it for?</b> Freshers, Professionals, and Career Switchers.</p>
""", unsafe_allow_html=True)

banner = Image.open("jobgpt/jobgpt_banner.png")
st.image(banner, use_container_width=True)

# Sidebar Inputs
with st.sidebar:
    st.header("🔧 Job Preferences")
    job_query = st.text_input("Job Title", "AI Engineer")
    job_location = st.text_input("Location", "Remote")
    resume_text = st.text_area("Paste Your Resume Here")

    if st.button("🔍 Find Jobs"):
        with st.spinner("Fetching jobs..."):
            jobs = fetch_jobs(job_query, job_location)
            st.session_state["jobs"] = jobs
            st.session_state["search_done"] = True

# Main UI
if st.session_state.get("search_done", False) and "jobs" in st.session_state:
    jobs = st.session_state["jobs"]
    st.header(f"🧠 Found {len(jobs)} Jobs for '{job_query}' in '{job_location}'")

    for idx, job in enumerate(jobs):
        st.subheader(f"{job.get('title')} at {job.get('company_name')}")
        st.write(job.get("description", "No job description available."))

        # Apply Link Section
        apply_link = job.get("url") or job.get("via")
        if apply_link and apply_link.startswith("http"):
            st.markdown(f"[👉 Apply Here]({apply_link})", unsafe_allow_html=True)
        else:
            company = job.get("company_name", "the company")
            st.warning(f"❌ No direct apply link found. Please visit {company}'s official careers page to apply.")

        # Resume Match
        if resume_text:
            with st.expander("📊 Match My Resume"):
                result = match_resume_to_job(resume_text, job.get("description", ""))
                st.markdown(f"**AI Match Score & Explanation:**\n\n{result if isinstance(result, str) else result.content}")

            # Cover Letter Generation
            with st.expander("✍️ Generate Cover Letter"):
                cover_letter = generate_cover_letter("templates/resume_template.jinja2", {
                    "company": job.get("company_name", "Unknown"),
                    "job_title": job.get("title", "Unknown")
                })
                st.code(cover_letter, language="markdown")

            # Interview Simulation
            with st.expander("🎤 Simulate Interview"):
                st.write("Simulated Interview Questions:")
                interview = simulate_interview(job.get("title", ""))
                st.write(interview)
else:
    st.info("ℹ️ Enter job preferences in the sidebar and click 'Find Jobs' to begin.")