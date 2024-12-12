#!/usr/bin/python3
"""Prime Game Module"""


def sieve_of_eratosthenes(limit):
    """Generate a list of primes up to 'limit'
    using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def prime_game(n):
    """Simulate the prime game for a given 'n'
    and return the winner ('Maria' or 'Ben')."""
    primes = sieve_of_eratosthenes(n)
    available = [True] * (n + 1)
    turn = 0  # 0 for Maria's turn, 1 for Ben's turn

    while True:
        for prime in primes:
            if prime <= n and available[prime]:
                # The current player picks this prime
                #  and removes it and its multiples
                for i in range(prime, n + 1, prime):
                    available[i] = False
                # Switch turns
                turn = 1 - turn
                break
        else:
            # No more primes to pick, game over, current player loses
            return 'Maria' if turn == 1 else 'Ben'


def isWinner(x, nums):
    """Determine the winner of x rounds given the nums array."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
