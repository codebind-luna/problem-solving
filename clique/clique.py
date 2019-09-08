import math
def s1(n, m):
    ga = n%m
    gb = m-ga
    sa = n//m+1
    sb = n//m
    return ga*gb*sa*sb+ga*(ga-1)*sa*sa//2+gb*(gb-1)*sb*sb//2
def s(n,c):
    l = 1
    h = n+1
    while l+1 < h:
        m = l+(h-l)//2
        k = s1(n,m)
        if k < c:
            l = m
        else:
            h = m
    return h
t = int(input())
for i in range(t):
    n,m=[int(j) for j in input().split()]
    print(s(n,m))