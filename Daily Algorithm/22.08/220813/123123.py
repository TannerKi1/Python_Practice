def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for _ in range(T):
    cnt = 0
    v, e = map(int, input().split())
    parent = [0] * (v+1)

    for i in range(1, v + 1):
        parent[i] = i

    graph = []

    for _ in range(e):
        a, b = map(int, input().split())
        graph.append((a, b))

    for item in graph:
        x, y = item
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            cnt += 1
        else:
            continue

    print(cnt)





