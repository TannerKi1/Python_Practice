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

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0: # 0값일 때 처리 어떻게 할 건지 외워두기
        break

    arr = []
    original_cost = 0
    for i in range(M):
        a, b, cost = map(int, input().split())
        arr.append((cost, a, b))
        original_cost += cost

    arr.sort()
    parent = [0] * (N+1)

    for i in range(1, N+1):
        parent[i] = i


    improved_cost = 0

    for item in arr:
        cost, a, b = item
        if find_parent(parent, a) != find_parent(parent, b):
            improved_cost += cost
            union_parent(parent, a, b)

    print(original_cost - improved_cost)
