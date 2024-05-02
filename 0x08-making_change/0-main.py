#!/usr/bin/python3
"""
Main file for testing
"""

make_change = __import__('0-making_change').make_change


print(make_change([1, 2, 25], 37))

print(make_change([1256, 54, 48, 16, 102], 1453))
