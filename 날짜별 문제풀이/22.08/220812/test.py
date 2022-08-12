from collections import deque
V, E = map(int, input().split())

# 부모 노드 만들기
parent = [0] * (V + 1)
for i in range(1, V+1):
    parent[i] = i

# 비용 정보 저장하기
graph = [ ]

for i in range(E):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()


# 가격 단위로 소팅완료

# 가격 낮은 것부터 부모노드 확인, 겹치지 않을 시 합쳐주기 시행

def parent_check(parent, x):
    if parent[x] != x:
        parent[x] = parent_check(parent, parent[x])
    return parent[x]


def make_union(parent, a, b):
    a = parent_check(parent, a)
    b = parent_check(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0

for item in graph:
    cost, a, b = item
    if parent_check(parent, a) != parent_check(parent, b):
        total += cost
        make_union(parent, a, b)

print(total)






