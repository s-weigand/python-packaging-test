# -*- coding: utf-8 -*-

"""Top-level package for python-packaging-test."""

from python_packaging_test.python_packaging_test import demo_function  # noqa:
from _version import get_versions
__version__ = get_versions()['version']
del get_versions

__author__ = """Sebastian Weigand"""
__email__ = 's.weigand.phy@gmail.com'

# testing to __init__ imports

