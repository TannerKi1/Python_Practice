# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오

n = int(input())

print(int(n*(n+1)/2))

# for 문으로 돌리려면...

# j = 0
# for x in range(1, n+1):
#     j = j + x
#
# print(j)