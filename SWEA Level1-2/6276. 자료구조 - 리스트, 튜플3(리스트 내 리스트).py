
# 구구단인데 2단부터 9단중에 3, 7의 배수를 제외한 값을 리스트 내의 리스트로 입력

# 문제만 놓고보면 지금 2차원 리스트가 나온 상황.

#1. 일단 리스트 내 리스트로 구구단을 입력하기

# 구구단 2단 ~ 9단 구하기

# scores = []
# score = []
#
# for x in range(2, 10):
#     for y in range(1, 10):
#         print(x*y)

# 이건 그냥 한 번에 다 담는거고... 개별 리스트에 담으려면 어떻게 해야할까?

# 무식하게 하는 건, append로 x % 3, x % 7 해서 아니면 append로 i값 올려서 넣는 방법인 것 같은데.

a = []

for i in range(2, 10):
    b = []
    if i % 3 != 0 and i % 7 != 0:
        for j in range(1, 10):
            if j % 3 != 0 and j % 7 != 0:
                b.append(i*j)
            else:
                continue
    a.append(b)

print(a)


# 2차원 리스트 컴프리헨션 초기화법을 사용해보자 (이건 더 나중에 사용해보자)

# n = 8
# m = 9
# array = [[0]*m for _ in range(n)]
# # array[0] = 2단
# # array[1] = 3단
# # array[0][0] = 2x1
# # array[0][1] = 2x2
#
# for x in range(2, 10):
#     for y in range(1, 10):
#             array[x-2][y-1] = x*y
#
# print(array)
#
# # 리스트 컴프리헨션으로, 특정값 제거하는 거 가능
# # 예시. 1~20 까지의 값 중에서 홀수만 담는 것

