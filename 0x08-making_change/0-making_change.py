#!/usr/bin/python3
"""
Given an unlimited supply of coins of given denominations,
find the minimum number of coins needed to meet a given amount total.
"""


def make_change(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum
    # number of coins needed for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    total = 11
    print(make_change(coins, total))  # Output: 3
