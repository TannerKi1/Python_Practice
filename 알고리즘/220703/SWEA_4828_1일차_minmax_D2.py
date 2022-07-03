T = int(input())

for x in range(1, T + 1):
    N = int(input())
    b = list(map(int, input().split()))
    m_v = max(b)
    n_v = min(b)
    print(f'#{x} {m_v - n_v}')


# 하지만 진짜라면...
# N의 개수로 [0] * N의 리스트를 만든 다음,
# list 내부의 값을 정렬한 다음에
# list[최대값] - list[0]로 정의하긴 해야함

# 버블이든, 계수이든 시간 복잡도 고려해서 만들긴해야함..! 근데 이건 숫자들이 너무 크니까 count로 하기 보다는 버블로 하나하나 비교하는 게 더 빠를것으로 예상

# pycharm에서는 오류나는데, SWEA에서는 정상적으로 작동함. 왜?
# 그냥 SWEA 예제 값이 이상했나봄. 다시 넣으니까 작동함