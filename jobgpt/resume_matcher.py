# LangChain-based matching logic
# Content for resume_matcher.py using LangChain + OpenAI
resume_matcher_code = '''\
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

def match_resume_to_job(resume_text, job_description):
    prompt = ChatPromptTemplate.from_template(
        "Given the following resume:\n{resume}\n\nAnd this job description:\n{jd}\n\nScore the match from 0 to 100 and explain your reasoning."
    )
    chain = prompt | llm
    return chain.invoke({"resume": resume_text, "jd": job_description})
'''