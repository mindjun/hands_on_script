

G = {'a':set('f'),
     'b':set('cdf'),
     'c':set('d'),
     'd':set('ef'),
     'e':set('f'),
     'f':set()}


def naive_topsort(G, S =None):
    if S is None:
        S = set(G)
    if len(S) == 1:
        return list(S)
    v = S.pop()
    print(S)
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]:
            min_i += 1
    seq.insert(min_i, v)
    return seq

# print(naive_topsort(G))

def topsort(G):
    count = dict((u,0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S


count = dict((u,0) for u in G)
print(count)
for u in G:
    for v in G[u]:
        count[v] += 1
Q = [u for u in G if count[u] == 0]

print(count)
print(Q)