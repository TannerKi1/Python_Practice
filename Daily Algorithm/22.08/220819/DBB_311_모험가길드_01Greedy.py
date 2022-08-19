N = int(input())
array = list(map(int, input().split()))

array.sort()

'''
-----
'''
# set_array = set(array)
#
# result = 0
#
# for x in set_array:
#     k = array.count(x)
#     answer = k // x
#     result += answer
#
# print(result)


result = 0
count = 0

for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
