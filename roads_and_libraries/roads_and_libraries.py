#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
from collections import deque

class graph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(set)
    def clone(self):
        g = graph()
        g.nodes = self.nodes[:]
        for n in self.nodes:
            for e in self.edges[n]:
                g.edges[n].add(e)
        return g
def bfs(g):
    nclust = 0
    used = set()

    csize = []
    
    for node in g.nodes:
        if node in used: continue
        used.add(node)

        size = 1
        Q = deque()
        Q.appendleft(node)
        while Q:
            cur = Q.pop()
            for neigh in g.edges[cur]:
                if neigh in used: continue
                used.add(neigh)
                Q.appendleft(neigh)
                size += 1
        nclust += 1
        csize.append(size)

    return nclust,csize
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n*c_lib
    
    g = graph()
    g.nodes = range(1,n+1)
    for a,b in cities:
        g.edges[a].add(b)
        g.edges[b].add(a)
    lbc, rc = bfs(g)
    return (lbc*c_lib + sum((x-1)*c_road for x in rc))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
