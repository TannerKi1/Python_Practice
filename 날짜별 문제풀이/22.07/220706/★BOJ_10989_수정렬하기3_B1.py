# 버블소팅 연습해보기

# N의 숫자 범위를 보면... 절대!!!! 버블정렬을 쓰면 안 된다는 사실을 알 수 있다.

# 버블 정렬의 시간 복잡도는 N**2

# N+K 인 카운팅 정렬로 가야한다.


import sys
N = int(input())
arr = []

for _ in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()

for j in arr.sort():
    print(j)

