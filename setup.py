#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='celery-redundant-scheduler',
    version='0.0.1',
    description='Celery beat scheduler with redundency',
    author='Mikhail Antonov',
    author_email='atin65536@gmail.com',
    long_description=open('README.md').read(),
    url='https://github.com/MnogoByte/celery-redundant-scheduler',
    packages=find_packages(),
    install_requires=["celery>=3.1"],
    keywords=['celery', 'celerybeat', 'scheduler', 'failover', 'redundancy'],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
    license="BSD"
)
