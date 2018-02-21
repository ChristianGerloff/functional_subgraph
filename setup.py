import io
import os
import re

from setuptools import find_packages, setup

import version

HERE = os.path.abspath(os.path.dirname(__file__))

# ==============================================================================
# Variables
# ==============================================================================

NAME = "FunctionalSubgraph"
VERSION = version.get_version()
DESCRIPTION = "FunctionalSubgraph: An ML tool for dynamic graph analysis."
with open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
PACKAGES = find_packages()
AUTHOR = "Ankit N. Khambhati"
AUTHOR_EMAIL = "akhambhati@gmail.com"
DOWNLOAD_URL = 'http://github.com/akhambhati/functional_subgraph/'
LICENSE = 'Nokia Open Source License'
INSTALL_REQUIRES = ['numpy', 'scipy', 'ipython']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Nokia Open Source License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
)
