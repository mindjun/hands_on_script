a,b,c,d,e,f,g,h = range(8)
G1 = [
    {b,c,d,e,f},
    {c,e},
    {d},
    {e},
    {f},
    {c,g,h},
    {f,h},
    {f,g}
]


# 邻接图的连通分量
def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        diff = G[u].difference(P, S)
        for v in diff:
            Q.add(v)
            P[v] = u
    return P


# print(walk(G1, 0))

def iter_dfs(G, a):
    s, l = set(), list()
    l.append(a)
    while l:
        n = l.pop()
        if n in s:
            continue
        s.add(n)
        l.extend(G[n])
        yield n

# print(list(iter_dfs(G1, 0)))


def rec_dfs(G, a, S=None):
    if S is None:
        S = set()
    S.add(a)
    for u in G[a]:
        if u in S:
            continue
        rec_dfs(G, u, S)


# 带时间戳的dfs
def dfs(G, s, d, f, S=None, t=0):
    if S is None:
        S = set()
    d[s] = t
    t += 1
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        t = dfs(G, s, d, f, S, t)
    f[s] = t
    t += 1
    return t


d = dict()
f = dict()
dfs(G1, 0, d, f)
print(d)
print(f)
