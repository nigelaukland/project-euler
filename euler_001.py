# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:46:26 2020
https://projecteuler.net/problem=1
@author: nigel
"""

# iterate up to 999
# if the remainder of dividing by 3 or 5 is 0 then add number to running sum

count = 1
total = 0
while count < 1000:
    print(count)
    if count % 3 == 0 or count % 5 == 0:
        total += count
    count += 1
print(total)    