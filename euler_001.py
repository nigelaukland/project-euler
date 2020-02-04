# -*- coding: utf-8 -*-

# iterate up to 999
# if the remainder of dividing by 3 or 5 is 0 then add number to running sum

import sys

def euler_001(limit: int) -> int:
    """https://projecteuler.net/problem=1
    Created on Mon Jan  6 21:46:26 2020
    @author: nigel

    Args:
        limit: The integer number for which you would like to solve.

    Returns:
        Find the sum of all the multiples of 3 or 5 below supplied limit.

    """

    count = 1
    total = 0
    while count < limit:
        # print(count)
        if count % 3 == 0 or count % 5 == 0:
            total += count
        count += 1
    return total

if __name__ == "__main__":
    limit = int(sys.argv[1])
    answer = euler_001(limit)
    print(answer)
