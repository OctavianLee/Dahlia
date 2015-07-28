# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

url="https://github.com/OctavianLee/Dahlia"
VERSION = "0.0.1"

setup(
    name="dahlia",
    version=VERSION,
    license='MIT',
    description="Algorithms implemented by Python.",
    author="Octavian Lee",
    author_email="octavianlee1@gmail.com",
    url = url,
    packages=find_packages('dahlia'),
    package_dir = {'': 'dahlia'}
)
