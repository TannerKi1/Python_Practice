N, K = map(int, input().split())
arr = list(map(int, input().split()))

# arr을 효율적으로 오름차순 나열할 수 있는 방안을 찾아야함
# 머지 정렬 개념을 알아야 풀 수 있는 문제라고 판단함.
# sorted함수 쓰거나, 버블 정렬쓰면 시간 초과뜰 것 같음.

b = sorted(arr)

print(b[K-1])