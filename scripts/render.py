import yaml
from jinja2 import Environment, FileSystemLoader

# Load Data
with open('data/experience.yml', 'r') as f:
    experience_data = yaml.safe_load(f)

with open('data/certifications.yml', 'r') as f:
    certifications_data = yaml.safe_load(f)

with open('data/education.yml', 'r') as f:
    education_data = yaml.safe_load(f)

# Merge all data
data = {**experience_data, **certifications_data, **education_data}

# Load Template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html.j2')

# Render and Save
output = template.render(data)
with open('index.html', 'w') as f:
    f.write(output)