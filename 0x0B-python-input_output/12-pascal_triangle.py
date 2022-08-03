#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    list = [[1]]
    while len(list) != n:
        x = list[-1]
        y = [1]
        for i in range(len(x) - 1):
            y.append(x[i] + x[i + 1])
        y.append(1)
        list.append(y)
    return list
