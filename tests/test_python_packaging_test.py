#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_packaging_test` package."""


import python_packaging_test
from python_packaging_test import demo_function


def test_demo_function():
    assert demo_function() == "demo"

def test_version():
    print(python_packaging_test.__version__)
    assert False
