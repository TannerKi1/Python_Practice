# 딕셔너리로 정렬?
# ㄴㄴ 리스트도 튜플 값이면 튜플 값을 지정해서 리스트 내부로 정렬할 수 있다.

# 이후 .sort()를 이용하고 괄호안에 key를 넣어서 무엇을 기준으로 정렬할 것인지도 정할 수 있음.
# 딕셔너리가 아니다..!

import sys
N = int(input())
empty_arr = []
for i in range(N):
    age, name = input().split()
    empty_arr.append((int(age), name))

empty_arr.sort(key= lambda x: x[0])

for x, y in empty_arr:
    print(f'{x} {y}')

