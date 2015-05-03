import os
from setuptools import setup, find_packages

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents

setup(
    name         = 'conformalmapping',
    version      = '0.0.1',
    description  = 'Conformal Mapping Toolbox (ported to Python)',
    long_description = read('README.rst'),
    author       = 'Andrew Walker',
    author_email = 'walker.ab@gmail.com',
    packages     = find_packages(),
    url          = "http://github.com/AndrewWalker/conformalmapping-py",
    license      = "BSD",
    classifiers  = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    tests_require=['unittest2'],
    test_suite='unittest2.collector'
)
