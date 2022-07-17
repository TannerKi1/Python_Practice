# 아이디어

# 오름차순으로 우선 받은 다음

# len의 절반으로 앞과 뒤를 나눈다

# 그 다음에 큰 거에서 먼저 1개 작은 거에서 먼저 한 개 보내서 새로운 리스트를 만든다

T = int(input())
for x in range(1, T+1):
    N = int(input())
    unsorted_list = list(map(int, input().split()))

    unsorted_list.sort()

    sorted_list_A = unsorted_list[:N//2]
    sorted_list_B = unsorted_list[N//2:]

    answer_list = []

    i, j = 0, len(sorted_list_B)-1
    for _ in range(N//2):
        answer_list.append(sorted_list_B[j])
        answer_list.append(sorted_list_A[i])
        i += 1
        j -= 1


    result = ' '.join(map(str, answer_list[0:10]))

    print(f'#{x} {result}')
