N = int(input())
arr = list(map(int, input().split()))

arr_2 = arr.copy()
arr_2.sort()



answer = []
for x in arr:
    answer.append(arr_2.index(x))
    arr_2[arr_2.index(x)] = -1  # 카운팅이 된 숫자는 다른 숫자로 바꿔서 중복 카운팅이 되지 않게 처리.
                                # for 문이 다 돌고 나면 arr_2의 값은 모두 -1로 바뀌게 된다.

for i in answer:
    print(i, end= ' ')

