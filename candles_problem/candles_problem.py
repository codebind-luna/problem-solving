mod = 10**9 + 7
N,K = map(int,input().split())
arr = list(tuple(map(int,input().split())) for _ in range(N))

class Fenwick_tree:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.data = [0]*sz
 
    def sum(self, i):
        if i == 0: return 0
        s = 0
        while i >= 0:
            s = (s + self.data[i]) % mod
            i = (i & (i+1)) - 1
        return s
 
    def add(self, i, x):
        assert i > 0
        while i < self.size:
            self.data[i] = (self.data[i] + x) % mod
            i |= i + 1

def get_no_inc_subseq(arr):
    if len(arr) == 0: return 0
    t = Fenwick_tree(max(arr))
    dp = [1] * len(arr)
    t.add(arr[0],dp[0])
    for i in range(1,len(dp)):
        dp[i] = (dp[i] + t.sum(arr[i]-1)) % mod
        t.add(arr[i],dp[i])
    return sum(dp)

ans = 0
for colors in range(1<<K):
    carr = [h for h,c in arr if (colors & (1<<(c-1))) != 0]
    curr = get_no_inc_subseq(carr)
    if bin(colors).count("1") % 2 == K % 2:
        ans = (ans + curr) % mod
    else:
        ans = (ans - curr) % mod

print(ans)