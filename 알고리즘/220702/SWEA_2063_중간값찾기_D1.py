
# 목표 : N개의 점수가 주어졌을 때, 중간값 구하기. 크기 순으로 배열 했을 때 딱 중앙에 오는 친구를 구해야함

# N이 주어지고, N개가 주어지니까... 리스트에 받은 다음에 len(N) / 2를 인덱스로 찾으면 중간값이 되지 않을까?

T = int(input())

b = list(map(int, input().split()))
k = sorted(b)

print(k[int((T-1) * 0.5)])