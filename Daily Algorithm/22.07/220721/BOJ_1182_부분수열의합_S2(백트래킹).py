# 부분집합 구하는 문제.


N, S = map(int, input().split())
arr = list(map(int, input().split()))

i = len(arr)

arr_2 = [0] * (1 << i)
arr_3 = []

for i in range(1 << i):
    mini = []
    for j in range(len(arr)):
        if i & (1 << j) == 0:
            mini.append(arr[j])  # 이 구문은 외워놓기. i는 전체 수, j는 len으로 받아서 이진법 진수 체크
    arr_3.append(mini)

count = 0
for x in arr_3:
    if len(x) != 0:
        if sum(x) == S:
            count += 1

print(count)


### https://seongonion.tistory.com/98 ### 효율적인 풀이 참조
### https://fre2-dom.tistory.com/402 ###