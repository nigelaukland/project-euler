# -*- coding: utf-8 -*-

import sys

def euler_006(limit: int) -> int:
    """https://projecteuler.net/problem=6

    Args:
        limit: The natural number for which you would like to solve.

    Returns:
        the difference between the sum of the squares of the natural 
        numbers up to <limit> and the square of the sum.
    """

    sumSquares = sum([ i**2 for i in range(1, limit+1) ])
    squareSum = (sum(range(1, limit+1)))**2
    difference = squareSum - sumSquares
    return difference

if __name__ == "__main__":
    limit = int(sys.argv[1])
    answer = euler_006(limit)
    print(answer)
