#!/usr/bin/python3
"""
Given an unlimited supply of coins of given denominations,
find the minimum number of coins needed to meet a given amount total.
"""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be met.

    Returns:
        int: The fewest number of coins needed to
        meet the total. If total is 0 or less, return 0.
        If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum
    # number of coins needed for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp[i] if using the current coin can
        # reduce the number of coins needed for total i
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'),
    # total cannot be met by any number of coins
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    total = 11
    print(make_change(coins, total))  # Output: 3
