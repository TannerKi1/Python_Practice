
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    A_list = [i for i in range(1, 13)]
    whole_list = []
    for i in range(1 << len(A_list)):
        part_list = []
        for j in range(len(A_list)):
            if i & (1 << j):
                part_list.append(A_list[j])
        whole_list.append(part_list)

    count = 0
    for i in whole_list:
        if len(i) == N and sum(i) == K:
            count += 1

    print(f'#{tc} {count}')

# 모든 숫자를 2진법으로 표현하고, 진수를 카운팅하여 부분집합을 만드는 방법