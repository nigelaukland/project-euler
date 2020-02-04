# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:55:22 2020
https://projecteuler.net/problem=5

@author: nigel
"""

# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
# All integers less than or equal to ten can be ignored
# check each integer greater than 20
# loop up until you find the number!

dividend = 148842440
#dividend = 20
divisorSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
divisorSet = { 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 }
#divisorSet = { 20 }
quotientSum = 0
solved = 0

while solved == 0:
    for divisor in divisorSet:
        quotientSum += dividend % divisor
        if quotientSum > 0:
            break
    if quotientSum == 0:
        print("The dividend is ", dividend) 
        solved = 1
    dividend += 20
    print(dividend)
    quotientSum = 0

    

