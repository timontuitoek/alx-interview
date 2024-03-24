#!/usr/bin/python3
"""def minOperations(n)"""


def minOperations(n):
    """Calculates the fewest number of operations needed"""
    if n <= 0:
        return 0

    operations = 0
    copied = 0
    current = 1

    while current < n:
        if n % current == 0:
            copied = current
        current += copied
        operations += 1

    return operations


# Example usage
n = 9
print(minOperations(n))  # Output: 6
