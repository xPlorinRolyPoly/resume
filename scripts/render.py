import yaml
from jinja2 import Environment, FileSystemLoader

import base64
import os

# Load Data
with open('data/experience.yml', 'r') as f:
    experience_data = yaml.safe_load(f)

with open('data/certifications.yml', 'r') as f:
    certifications_data = yaml.safe_load(f)

with open('data/education.yml', 'r') as f:
    education_data = yaml.safe_load(f)

with open('data/languages.yml', 'r') as f:
    languages_data = yaml.safe_load(f)

# Optional local profile image (base64 encoded so raw image is not required on GitHub)
profile_image = None
if os.path.exists('alpana.png'):
    with open('alpana.png', 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')
        profile_image = f"data:image/png;base64,{img_b64}"

# Merge all data
data = {**experience_data, **certifications_data, **education_data, **languages_data, 'profile_image': profile_image}

# Load Template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html.j2')

# Render and Save
output = template.render(data)
with open('index.html', 'w') as f:
    f.write(output)
