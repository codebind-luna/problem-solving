def lstin():
    return list(map(int,input().strip().split()))

def dfs(edges, root):
    stack = [(root, v) for v,d in edges[root]]
    flatten = list()
    while stack:
        u, v = stack.pop()
        flatten.append((u, v))
        stack.extend((v, w) for w,d in edges[v] if w != u)
    flatten.reverse()
    return flatten

def get_subtree(edges,is_goal,root):
    subt=is_goal[:]
    for u,v in dfs(edges, root):
        subt[u]=subt[u] or subt[v]
    return subt

def get_farthest(edges,is_goal,subtree,root):
    visited=[False for _ in edges]
    st=[(0,root)]
    visited[root]=True
    mx=0,root
    dist_all=0
    while st:
        dist,u=st.pop()
        for v,d in edges[u]:
            if not visited[v] and subtree[v]:
                elm=dist+d,v
                dist_all+=d
                if is_goal[v]:
                    mx=max(mx,elm)
                st.append(elm)
                visited[v]=True
    return dist_all,mx


N,K=lstin()
goals=lstin()
is_goal=[False]*(N+1)
for u in goals:
    is_goal[u]=True
edges=[list() for _ in range(N+1)]
for _ in range(N-1):
    u,v,d=lstin()
    edges[u].append((v,d))
    edges[v].append((u,d))

subtree=get_subtree(edges,is_goal,goals[0])
_,(_,u)=get_farthest(edges,is_goal,subtree,goals[0])
D,(d,_)=get_farthest(edges,is_goal,subtree,u)
print(2*D-d)