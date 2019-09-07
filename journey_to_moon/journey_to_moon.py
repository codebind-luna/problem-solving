#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    data = [-1 for j in range(n)]
    grpid = 0
    for pair in astronaut:
        a,b= pair[0], pair[1]

        if data[a] == data[b] == -1:
            data[a] = grpid
            data[b] = grpid
            grpid += 1
        elif data[a] != -1 and data[b] == -1:
            data[b] = data[a]
        elif data[b] != -1 and data[a] == -1:
            data[a] = data[b]
        else:
            valuea = data[a]
            for index in range(n):
                if data[index] == valuea:
                    data[index] = data[b]

    for index in range(n):
        if data[index] == -1:
            data[index] = grpid
            grpid += 1

    countrysizes = Counter(data)

    def calculatePairs(countrysizes):
        result, localsum = 0, 0
        for k, v in countrysizes.items():
            result += localsum*v
            localsum += v
        return result
    
    return calculatePairs(countrysizes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
