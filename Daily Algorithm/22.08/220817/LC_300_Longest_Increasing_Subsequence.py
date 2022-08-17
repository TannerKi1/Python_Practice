from bisect import bisect_left

# nums = [10, 9 , 2,5,3,7,101,18]
nums = [0,1,0,3,2,3]

d = []
for x in nums:
    val = bisect_left(d, x)

    if val == len(d):
        d.append(x)

    else:
        d[val] = x


print(len(d))