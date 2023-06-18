#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    makechange function
    """

    if total <= 0:
        return 0

    current_total = 0
    used_coin = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        i = (total-current_total)//coin
        current_total += i*coin
        used_coin += i
        if current_total == total:
            return used_coin
    return -1
