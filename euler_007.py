# -*- coding: utf-8 -*-

import sys

def euler_007(limit: int) -> int:
    """https://projecteuler.net/problem=7

    Args:
        limit: The natural number for which you would like to solve.

    Returns:
        The (n)th prime number where n is the provided limit
    """
    i = 1 # i increments
    count = 0 # count tallies the number of prime numbers
    while count < limit:
        i += 1
        if is_prime(i):
            count += 1
            # print(i, ' is prime')
    # print(i, ' is prime number ', limit)
    return i

def is_prime(n: int) -> bool:
    """
    Tests a natural number to see if it is prime

    Args:
        n: The number to test

    Returns:
        True if prime, false if not
    """

    # test each number from 2 up to n/2
    # Take the Modulo of n divided by the number
    # if each modulo > 0 then number is prime 
    # (i.e. there's no divisor that results in an integer quotient)
    
    if n == 1 or n == 2 or n == 3:
        return True
    elif min([ n%i for i in range(2, n//2+1) ]) == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    limit = int(sys.argv[1])
    answer = euler_007(limit)
    print(answer)
