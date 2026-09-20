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

# Profile image for web version (uses public GitHub avatar, so raw image file is never committed)
profile_image = "https://github.com/xplorinrolypoly.png"

# Merge all data
data = {**experience_data, **certifications_data, **education_data, **languages_data, 'profile_image': profile_image}

# Load Template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html.j2')

# Render and Save
output = template.render(data)
with open('index.html', 'w') as f:
    f.write(output)
