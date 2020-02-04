# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:46:26 2020
https://projecteuler.net/problem=3
@author: nigel
"""

# prime factors of 600851475143
# 1. Check whether divides by two.
# 2. If so, divide by two, add that as a factor.
# 3. for each odd number from 2 call A is 600851475143 % A == 0?
# 4. if so, then that is a prime factor. Divide the number by this, 
#    print the number, start again.
# 5. up to the square root of 600851475143

import math

target = 600851475143
factor = 3

# 1. Check whether divides by two.
while target % 2 == 0:
    # 2. If so, divide by two, add that as a factor.
    target /= 2
    print(2)
# 3. for each odd number from 2 call A is 600851475143 % A == 0?
# 5. up to the square root of 600851475143
while factor <= math.sqrt(target):
    while target % factor == 0:
        # 4. if so, then that is a prime factor. Divide the number by this, 
        target /= factor
        #    print the number, start again.        
        print(factor)
    factor += 2
print(target)