#!/usr/bin/python3
"""Solving prime game Dialemma"""


def isWinner(x, nums):
    """Function to output prime game winner"""
    maria_Count = 0
    ben_Count = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            ben_Count += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    ben_Count += 1
                else:
                    maria_Count += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if maria_Count > ben_Count:
        return "Winner: Maria"

    if maria_Count < ben_Count:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Output True if n is prime, False elsewere"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Output prime numbers list between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
