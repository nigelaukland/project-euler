# -*- coding: utf-8 -*-

import sys

def euler_008(inputFile: str, digits: int) -> int:
    """https://projecteuler.net/problem=8

    Args:
        digits: The number of adjacent digits for which you would like to solve.
        inputFile: The filename of the input file containing the long number.

    Returns:
        The highest product of consecutive digits in inputFile
    """

    # read file    
    longNumber = open(inputFile, "r").read()
    index = 0
    maximum = 0

    while index <= len(longNumber) - digits:
        testString = longNumber[ index : index + digits ]
        # print(testString)
        product = 1
        for i in testString:
            product *= int(i)
        # print(product)
        if product > maximum:
            maximum = product
        index += 1
    return(maximum)

if __name__ == "__main__":
    inputFile = sys.argv[1]
    digits = int(sys.argv[2])
    answer = euler_008(inputFile, digits)
    print('The highest product of', digits, 'consecutive digits is', answer)
