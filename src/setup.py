#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'paho-mqtt',
    'influxdb'
    # TODO: Put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(sdague): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

setup(
    name='nypower',
    version='0.1.0',
    description="NY ISO power app",
    long_description=readme + '\n\n' + history,
    author="Sean Dague",
    author_email='sean@dague.net',
    url='https://github.com/sdague/nypower',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ny-power-pump=nypower.cmd.pump:main',
            'ny-power-archive=nypower.cmd.archive:main',
            'ny-power-backlog=nypower.cmd.backlog:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='nypower',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
