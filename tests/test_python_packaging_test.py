#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_packaging_test` package."""


from python_packaging_test import demo_function
from python_packaging_test.python_packaging_test import (
    brach_function,
    GLOBAL_VAR,
    DemoClass,
)


def test_GLOBAL_VAR():
    assert GLOBAL_VAR == 1


def test_demo_function():
    assert demo_function() == "demo"


def test_brach_function():
    assert brach_function(True) == True
    assert brach_function(False) == False


def test_DemoClass():
    demo = DemoClass()
    assert DemoClass.class_prop == True
    assert demo.dummy_method() == True
