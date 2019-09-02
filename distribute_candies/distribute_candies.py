#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candiesArray = [1 for _ in range(n)]

    for i in range(1, n, 1):
        if arr[i] > arr[i-1]:
            candiesArray[i] = candiesArray[i-1] + 1

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and candiesArray[i] <= candiesArray[i+1]:
           candiesArray[i] = candiesArray[i+1] + 1
    
    return sum(candiesArray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
