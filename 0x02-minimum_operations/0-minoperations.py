#!/usr/bin/python3
"""
Solving Minimum operations Python Dialemma
"""


def minOperations(n):
    """
    Finds the fewest No. of operations

    Args:
        n (number): A number to run operations with

    Return:
        integer or 0 if n is impossible to achieve
    """
    if not n or n == 0:
        return 0

    current = 1
    copy = 0
    operations = 0

    while current < n:
        if n % current == 0:
            copy = current
            current += copy
            operations += 2
        else:
            current += copy
            operations += 1

    return operations
