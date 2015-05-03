import os
import sys
from setuptools import setup, find_packages

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents

# Python version specific setup
extras = {}
if sys.version_info >= (3,):
    extras['test_suite'] = 'tests'
else:
    extras['tests_require'] = ['unittest2']
    extras['test_suite'] = 'unittest2.collector'

setup(
    name         = 'conformalmapping',
    version      = '0.0.1',
    description  = 'Conformal Mapping Toolbox (ported to Python)',
    long_description = read('README.rst'),
    author       = 'Andrew Walker',
    author_email = 'walker.ab@gmail.com',
    packages     = find_packages(exclude=('tests',)),
    url          = "http://github.com/AndrewWalker/conformalmapping-py",
    license      = "BSD",
    classifiers  = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    **extras
)
