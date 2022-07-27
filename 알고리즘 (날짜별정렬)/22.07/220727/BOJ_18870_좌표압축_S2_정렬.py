N = int(input())
arr = list(map(int, input().split()))
arr_2 = arr.copy()

arr_3 = sorted(arr)
arr_4 = sorted(list(set(arr_3))) # set을 하니 오름차순이 풀려버리는 문제점이 발생함.

for x in arr_2:
    print(arr_4.index(x), end= ' ')

# 역시 시간초과가 뜬다...


