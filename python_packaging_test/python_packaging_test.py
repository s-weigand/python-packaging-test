# -*- coding: utf-8 -*-

"""Main module."""

GLOBAL_VAR = 1


def demo_function():
    return "demo"


def brach_function(var):
    if var:
        return True
    else:
        return False


class DemoClass:
    class_prop = True

    def dummy_method(self):
        return True
