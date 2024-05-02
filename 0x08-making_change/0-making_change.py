#!/usr/bin/python3
"""
Making Change: Determine the fewest number
of coins needed to meet a given amount total.
"""


def make_Change(coins, total):
    # If the total amount is zero or negative, return 0
    if total <= 0:
        return 0

    # Sorting coins in descending order
    coins.sort(reverse=True)
    coin_count = 0

    # Greedily choose the largest denomination coins first
    for coin_value in coins:
        while total >= coin_value:
            coin_count += 1
            total -= coin_value

    # If the total amount is fully covered by the
    # coins, return the number of coins used
    if total == 0:
        return coin_count
    else:
        return -1

if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    total = 11
    print(make_Change(coins, total))  # Output: 3
