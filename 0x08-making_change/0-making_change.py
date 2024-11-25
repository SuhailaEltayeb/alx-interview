#!/usr/bin/python3
"""
Solving making chage dialemma
"""


def makeChange(coins, total):
    """Determine the fewest No. of 'coins' needed to meet 'total'

    Args:
        coins [list]: Possessed list of coin values 
        total (int): Targeted amount

    Return:
        coins: The fewest number of coins to meet 'total
        0: If 'total' is 0 or less
        -1: If total cannot be met by any number of 'coins'
    """
    c_coins = x = 0

    if total < 1:
        return 0

    for coin in sorted(coins)[::-1]:
        while c_coins + coin <= total:
            c_coins += coin
            x += 1

    if c_coins != total:
        return -1

    return x
