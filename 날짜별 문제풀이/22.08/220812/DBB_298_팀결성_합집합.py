N, M = map(int, input().split())

parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i

def parent_check(parent, x):
    if parent[x] != x:
        parent[x] = parent_check(parent, parent[x])
    return parent[x]

def union_team(parent, a, b):
    a = parent_check(parent, a)
    b = parent_check(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    order, a, b = map(int, input().split())
    if order == 0:
        union_team(parent, a, b)

    elif order == 1:
        if parent_check(parent, a) == parent_check(parent, b):
            print("YES")
        else:
            print("NO")

