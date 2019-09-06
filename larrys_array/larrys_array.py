#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(arr):
	def isSorted(arr):
        n = len(arr)
        last = arr[n-1]
        
        sorted = True
        for i in range(n-2):
            if arr[i] > arr[i+1] or arr[i] > last:
                sorted = False
                break
        return sorted

    def doRotate(arr, index):
        n = len(arr)
        leftI = 0 # Index from where next scan should start
        
        if index+2 <= n-1:
            tmp = arr[index]
            arr[index] = arr[index+1]
            arr[index+1] = arr[index+2]
            arr[index+2] = tmp
            leftI = index-1 if index > 0 else index
        else:
            tmp = arr[index-1]
            arr[index-1] = arr[index]
            arr[index] = arr[index+1]
            arr[index+1] = tmp
            leftI = index-2 if index-2 > 0 else index-2
        return leftI
    # Checks if arr needs sorting and does it. Returns False if it did sorting, else True.
    def doSort(arr):
        n = len(arr)
        i = 0
        while i < n-1:
            if arr[i] > arr[i+1]:
                if i == n-2 and isSorted(arr): # Only last 2 unsorted
                    return False
                else:
                    i = doRotate(arr, i)
            else:
                i = i+1
        return True
        
    if doSort(arr):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
