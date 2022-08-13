N = int(input())
arr_dict = {}
arr_list = list(map(int, input().split()))
for x in arr_list:   # 불필요하게 list가 적히는 감이 없잖아 있음
    if x not in arr_dict:
        arr_dict[x] = 1
    else:
        arr_dict[x] += 1

M = int(input())
arr_list2 = list(map(int, input().split()))

answer = []
for x in arr_list2:
    if x in arr_dict:
        answer.append(arr_dict[x])
    else:
        answer.append(0)

for i in answer:
    print(i, end=' ')