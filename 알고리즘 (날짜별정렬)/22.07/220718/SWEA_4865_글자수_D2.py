T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str2_dict = dict()
    new_list = []
    for y in str2:
        if y not in str1:
            continue
        if y in str1:
            new_list.append(y) # 여기도 좀 더 깔끔하게 해결할 수 있지 않을까?

    new_list_dict = dict()
    for char in new_list:
        if char not in new_list_dict:
            new_list_dict[char] = 1
        else:
            new_list_dict[char] += 1

    print(f'#{tc} {max(new_list_dict.values())}')


### dict을 만들면 최댓값과 그 최댓값의 키는 빠르게 뽑아낼 수 있다.
# 하지만... 최댓값의 키가 여러개가 나온다면....? 그 땐 list로 받아내서 그 안에서 작업?