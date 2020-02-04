# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:46:26 2020
https://projecteuler.net/problem=2
@author: nigel
"""

# create fibonnaci sequence
# sum all even elements

a, b = 0, 1
total = 0
while a < 4000000:
    a, b = b, a + b
    print("b = ", b)
    if b % 2 == 0:
        total += b
        print("total = ", total)