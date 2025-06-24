# Uses Jinja2 template to generate a cover letter
# Content for cover_letter_gen.py using Jinja2
cover_letter_gen_code = '''\
from jinja2 import Template

def generate_cover_letter(template_path, context):
    with open(template_path, "r") as file:
        template = Template(file.read())
    return template.render(**context)

# Example usage:
# context = {"company": "OpenAI", "job_title": "ML Engineer"}
# print(generate_cover_letter("templates/resume_template.jinja2", context))
'''