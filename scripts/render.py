import yaml
from jinja2 import Environment, FileSystemLoader

# Load Data
with open('data/experience.yml', 'r') as f:
    data = yaml.safe_load(f)

# Load Template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html.j2')

# Render and Save
output = template.render(data)
with open('index.html', 'w') as f:
    f.write(output)