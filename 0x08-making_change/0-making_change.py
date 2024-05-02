#!/usr/bin/python3
"""
This script calculates the fewest number of coins needed to meet a given total amount.
"""


def make_Change(coins, total):
    # If the total amount is zero or negative, return 0
    if total <= 0:
        return 0

    # Sorting coins in descending order
    coin = sorted(coins, reverse=True)
    counter = 0

    # Greedily choose the largest denomination coins first
    for coin_value in coin:
        while total >= coin_value:
            counter += 1
            total -= coin_value

    if total == 0:
        return counter
    else:
        return -1
