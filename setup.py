#!/usr/bin/env python
import sys
from setuptools import setup
from warnings import warn

if sys.version_info < (3, 7, 6):
    warn(f"Behavior is uncertain prior to Python 3.7.6.  Current version: {sys.version_info}")

setup(
    setup_requires=['pbr'],
    pbr=True,
)
