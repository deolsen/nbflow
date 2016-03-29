#!/usr/bin/env python
# coding: utf-8

# Distributed under the terms of the Modified BSD License.

import os
from distutils.core import setup

name = 'nbflow'
here = os.path.abspath(os.path.dirname(__file__))
version_ns = {}
with open(os.path.join(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name=name,
    version=version_ns['__version__'],
    description='A tool that supports one-button reproducible workflows with the Jupyter Notebook and Scons',
    author='Jessica B. Hamrick',
    author_email='jhamrick@berkeley.edu',
    license='BSD',
    url='https://github.com/jhamrick/nbflow',
    keywords=['Notebooks'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['nbflow'],
    scripts=['scripts/nbflow']
)

setup_args['install_requires'] = install_requires = []
with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)

setup(**setup_args)
