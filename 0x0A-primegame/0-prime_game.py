#!/usr/bin/python3
""" A function that decides winner of a prime game """


def isWinner(x, nums):
    """
    Determines the winner of each round of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper
        limit for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """
    if not nums or x < 1:
        return None

    # Helper to compute primes using the Sieve of Eratosthenes
    def sieve(max_num):
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_num**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, max_num + 1, i):
                    primes[multiple] = False
        return primes

    max_n = max(nums)
    prime_flags = sieve(max_n)

    # Precompute prime counts up to each number for efficient lookup
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
