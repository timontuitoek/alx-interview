#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sorting coins in descending order
    coin = sorted(coins, reverse=True)
    counter = 0

    for coin_value in coin:
        while total >= coin_value:
            counter += 1
            total -= coin_value

    if total == 0:
        return counter
    else:
        return -1
