# -*- coding: utf-8 -*-

import sys
import math

def euler_009() -> int:
    """https://projecteuler.net/problem=9

    Returns:
        A tupple containing the one Pythagorean triplet for which a + b + c = 1000.
    """

    for a in range (1, 1000):
        for b in range (1, 1000-a):
            c = 1000 - a - b
            # print('a=', a, 'b=', b, 'c=', c)
            if a*a + b*b == c*c:
                print('a=', a, 'b=', b, 'c=', c)
                return(a * b * c)

if __name__ == "__main__":
    answer = euler_009()
    print(answer)
