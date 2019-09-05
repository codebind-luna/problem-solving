#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
	numberOfDays = len(prices)
    maximLocal = prices[numberOfDays - 1]
    stocksHeld = 0
    expenseSoFar = 0
    totalProfit = 0
    for i in range(numberOfDays-2, -1, -1):
    	currentDayPrice = prices[i]
    	if currentDayPrice >= maximLocal:
    		totalProfit += stocksHeld*maximLocal - expenseSoFar
    		expenseSoFar = 0
    		stocksHeld = 0
    		maximLocal = currentDayPrice
		else:
			expenseSoFar += currentDayPrice
			stocksHeld += 1
	if stocksHeld > 0:
		totalProfit += stocksHeld*maximLocal - expenseSoFar
	return totalProfit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
