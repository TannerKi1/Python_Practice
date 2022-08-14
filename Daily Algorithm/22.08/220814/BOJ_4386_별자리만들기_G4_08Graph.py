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


N = int(input())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

### 부모 노드 초기화 끝

star = []

for _ in range(N):
    x, y = map(float, input().split())
    star.append((x, y))

cost = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        cost[i][j] = (abs(star[i][0] - star[j][0])**2 + abs(star[i][1] - star[j][1])**2) ** 0.5

real_cost = []

for i in range(N):
    for j in range(N):
        real_cost.append((cost[i][j], i+1, j+1))

real_cost.sort()




total = 0


for item in real_cost:
    money, x, y = item
    if find_parent(parent, x) != find_parent(parent, y):
        total += money
        union_parent(parent, x, y)

print(f'{total:.2f}')




