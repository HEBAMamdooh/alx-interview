#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    # Validate input
    if not nums or x <= 0 or any(n < 0 for n in nums):
        return None

    # Determine the maximum value of n in nums
    max_n = max(nums)

    # Handle edge cases where no valid game can be played
    if max_n < 2:
        return None  # No primes, no game

    # Sieve of Eratosthenes to precompute primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Game rounds and determining the winner
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:  # If n is less than 2, Ben automatically wins this round
            ben_wins += 1
        elif prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
