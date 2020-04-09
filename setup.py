from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(
    name='django_ibanfield',
    version=version,
    description='IBAN field for django with account validation',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": [
            "pytest>=5.4.1",
            "Django>=2.2.10"
        ]
    },
    url="https://github.com/KeoH/django-ibanfield",
    author="Francisco Manzano Magaña",
    author_email="keoh77@gmail.com",
)
