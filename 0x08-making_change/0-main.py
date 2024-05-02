#!/usr/bin/python3
"""
Main file for testing
"""

make_Change = __import__('0-making_change').make_Change

print(make_Change([1, 2, 25], 37))

print(make_Change([1256, 54, 48, 16, 102], 1453))
