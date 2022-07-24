TC = int(input())

for i in range(1, TC+1):

    full_arr = input()
    empty_arr = []
    for x in full_arr:
        if len(empty_arr) == 0:
            empty_arr.append(x)
        else:
            if x != empty_arr[-1]:
                empty_arr.append(x)
            else:
                empty_arr.pop(-1)

    print(f'#{i} {len(empty_arr)}')


# pop이랑 remove 차이가 어디에서 발생했다는 뜻인데...?
# remove로 하면 맨 앞에 멀쩡히 살아있는 독립문자도 사라져버릴 수 있음!!!