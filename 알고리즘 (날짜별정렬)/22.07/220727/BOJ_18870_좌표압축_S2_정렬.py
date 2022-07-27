N = int(input())
arr = list(map(int, input().split()))
arr_2 = arr.copy()
#
# arr_3 = []
#
# for x in arr:
#     if x not in arr_3:
#         arr_3.append(x)
#     else:
#         continue
#
# arr_4 = sorted(arr_3)
#
# for x in arr_2:
#     print(arr_4.index(x), end= ' ')

# 역시 시간초과가 뜬다...

# dictionary로 치면?

# list와 dictionary의 순회 차이를 이해하고 있는지?...

arr_3 = list(sorted(set(arr)))

dict = {arr_3[i]:i for i in range(len(arr_3))} # 이거 잘 알아놓자. arr_3의 index값을 key로 부르고, value는 index 그 자체를 range만큼 반복함!


for x in arr_2:
    print(dict[x], end = ' ')    # x를 넣었을 때 그 value값인 index를 불러오게 된다.


# 결론 : 딕셔너리의 시간 복잡도가 리스트보다 우수하다.