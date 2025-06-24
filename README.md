# 💼 JobGPT – AI-Powered Job Assistant (Streamlit Cloud Edition)

JobGPT is a powerful AI-driven assistant that helps job seekers automate and enhance their job application process. Built with **Streamlit**, **Azure OpenAI**, and **SerpAPI**, it enables users to:

✅ Search and filter jobs online  
✅ Match their resume with job descriptions using AI  
✅ Generate tailored cover letters  
✅ Simulate interview questions

---

## 🌐 Live Demo

👉 [Streamlit Cloud](https://streamlit.io/cloud) – Deploy and use it instantly.

---

## ✨ Features

- 🔍 **Job Finder** – Uses SerpAPI to find real-time job postings.
- 📊 **Resume Matcher** – Calculates AI relevance between resume and job description.
- ✍️ **Cover Letter Generator** – Auto-generates cover letters using GPT-4.
- 🎤 **Interview Simulator** – Generates mock interview questions for preparation.
- 🔗 **Apply Links** – Takes users to application pages or company websites.

---

## 🚀 Deploy on Streamlit Cloud

### 1. Clone This Repo to Your GitHub

```
git clone https://github.com/YOUR_USERNAME/JobGPT-StreamlitCloud.git
```

Then push it to your GitHub.

### 2. Create a New Streamlit Cloud App

- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Click **“New app”**
- Connect your GitHub repo
- Fill in:
  - **Repository:** `JobGPT-StreamlitCloud`
  - **Branch:** `main`
  - **Main file path:** `jobgpt/job_dashboard.py`

### 3. Add Your Streamlit Cloud Secrets

Click **“Edit Secrets”** and add:

```toml
OPENAI_API_KEY = "your-azure-openai-key"
OPENAI_API_BASE = "https://your-resource-name.openai.azure.com/"
OPENAI_API_VERSION = "2024-12-01-preview"
OPENAI_DEPLOYMENT_NAME = "gpt-4"
SERPAPI_KEY = "your-serpapi-api-key"
```

💡 Get SerpAPI key: [https://serpapi.com/manage-api-key](https://serpapi.com/manage-api-key)

---

## 🛠️ Local Development (Optional)

### Prerequisites

- Python 3.8+
- Install dependencies:

```
pip install -r requirements.txt
```

### Create a `.env` file

```env
OPENAI_API_KEY=your-key
OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
OPENAI_API_VERSION=2024-12-01-preview
OPENAI_DEPLOYMENT_NAME=gpt-4
SERPAPI_KEY=your-serpapi-key
```

### Run App

```bash
streamlit run jobgpt/job_dashboard.py
```

---

## 📂 Project Structure

```
JobGPT-StreamlitCloud/
│
├── jobgpt/
│   ├── job_dashboard.py
│   ├── resume_matcher.py
│   ├── cover_letter_gen.py
│   ├── interview_bot.py
│   ├── job_scraper.py
│   └── utils.py
│
├── templates/
│   └── resume_template.jinja2
│
├── .streamlit/
│   └── config.toml (optional)
│
├── .env (local only)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Huzefa Husain**  
🔗 [LinkedIn](https://linkedin.com/in/huzefaaa)  
💻 [GitHub](https://github.com/Huzefaaa2)

---

## 📄 License

MIT License – use freely and responsibly.

---