#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["numpy"]

setup_requirements = requirements + [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    author="Sebastian Weigand",
    author_email='s.weigand.phy@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is a test project for packaging and deploying python "
    "packages with automated builds and deployment to PyPi and "
    "anaconda",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python_packaging_test',
    name='python_packaging_test',
    packages=find_packages(include=['python_packaging_test']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/s-weigand/python_packaging_test',
    version='0.0.13',
    zip_safe=False,
)
