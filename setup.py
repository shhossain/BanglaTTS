from setuptools import setup, find_packages

version = '0.0.2'
description = 'An open-source offline text-to-speech package for Bangla language. Convert text to speech in male or female voice.'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

name = 'BanglaTTS'
author = 'sifat (shhossain)'
email = '<hossain@gmail.com>'

with open('requirements.txt') as f:
    required = f.read().splitlines()



keywords = ['python','text to speech','bangla text to speech', 'bangla tts', 'offline bangla tts', 'offline bangla text to speech']

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Utilities',
    'Operating System :: OS Independent',
]

projects_links = {
    "Documentation": "https://github.com/shhossain/BanglaTTS",
    "Source": "https://github.com/shhossain/BanglaTTS",
    "Bug Tracker": "https://github.com/shhossain/BanglaTTS/issues",
}

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=author,
    author_email=email,
    url="https://github.com/shhossain/BanglaTTS",
    project_urls=projects_links,
    packages=find_packages(),
    install_requires=required,
    keywords=keywords,
    classifiers=classifiers,
    python_requires='>=3.6',
)