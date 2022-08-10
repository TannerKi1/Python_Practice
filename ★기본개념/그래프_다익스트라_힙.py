import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 1) 개선된 다익스트라














#2 기본 다익스트라

# graph = [[] for _ in range( n + 1)] # 노드 그래프 만들기, +1의 이유는 앞에 0노드 만들어서 직관 대응해주려고
# visited = [False] * (n + 1) # 방문 그래프
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
#
# 여기까지 사전 정보 입력 완료.
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1): # 1번 노드부터 , n + 1 노드까지 순회
#         if visited[i] == False and distance[i] < min_value:
#             min_value = distance[i] # 가장 작은 거리값이 distance[i]로 초기화되고
#             index = i # 그에 해당하는 i값이 노드 인덱스로 들어온다. 하지만...
#     return index # for문을 다 돌고 나서 가장 작은 값이 확정된다.
#
# # 그 노드가 갈 수 있는 노드 중에서 가장 비용이 작은 노드를 선택하는 함수
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]  # 노드2까지 거리는 2, 노드3까지 거리는 5, 노드4까지 거리는 1로 distance 초기화
#
#     for _ in range(n - 1): # 시작 노드 제외한 n-1개 노드만큼 반복해주는 것임. 위의 i와는 다르게 써야함
#         now = get_smallest_node() # 맨 처음 돌 때는 4와, 거리 1이 들어오게 된다.
#         visited[now] = True # 4의 visited가 True로 바뀌게 된다.
#
#         for j in graph[now]: # 4와 연결된 그래프들을 본다. 여기서는 (2, 3), (6, 5)가 참조된다.
#             cost = distance[now] + j[1] # 4를 거쳐 2까지가는 거리가 1+3 그리고 6까지가는 거리가 1+5로 나온다.
#
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost # 만약 기존에 가지고 있는 값보다 더 적다면 cost만큼으로 초기화 시켜준다.
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])






