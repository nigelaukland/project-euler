# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:40:17 2020
https://projecteuler.net/problem=4

@author: nigel
"""

# Find the largest palindrome made from the product of two 3-digit numbers.

# brute force:
# start at 999, head down to 990 in both factors of the product.
# check whether the resulting product is a palindrome


a = 999
b = 999
max_palindrome = 0

while a >= 0:
    while b >= 0:
        product = str(a * b)
        if product == product[::-1]:
            print(product, ' = ', a, ' * ', b)
            if a * b > max_palindrome:
                max_palindrome = a * b
        b -= 1
    a -= 1
    b = 999
print('max palindrome = ', max_palindrome)
    