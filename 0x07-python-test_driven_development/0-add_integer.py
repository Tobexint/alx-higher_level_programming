#!/usr/bin/python3
"""
This module defines a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
         a(int): first number(converted to int if float)
         b(int): second number(converted to int if float)

    Returns the addition of a and b on success,
    and raises a  typeerror if a and b are not integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
