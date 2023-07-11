from setuptools import setup, find_packages
import os

def get_gitignore_patterns():
    gitignore_file = os.path.join(os.path.dirname(__file__), '.gitignore')
    patterns = []

    with open(gitignore_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                patterns.append(line)

    return patterns

with open('requirements.txt') as req:
    requirements = req.read().splitlines()

setup(
    name='django_blog',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
    exclude=get_gitignore_patterns(),
)
