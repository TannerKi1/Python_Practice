# # import time
#
# start = time.time()
L, R = map(int, input().split())


count_list = []

for i in range(L, R+1):
    count = 0
    for x in str(i):
        if x == '8':
            count += 1

    count_list.append(count)

print(min(count_list))
# print(time.time() - start)


# 답은 나오는데, 시간 초과 나옴.
# 어떻게 해야 8의 개수를 더 효율적으로 찾을 수 있을까?

# 아이디어로 풀어야함. 전체를 다 뒤집는 것은 너무 비효율적이다.

