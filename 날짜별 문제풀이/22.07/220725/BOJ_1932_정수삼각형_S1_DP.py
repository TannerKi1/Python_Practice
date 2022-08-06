TC = int(input())

arr = []
for _ in range(TC):
    little_arr = [0]
    list_ = list(map(int, input().split()))
    for x in list_:
        little_arr.append(x)
    little_arr.append(0)
    arr.append(little_arr)

# 이제 dp 리스트만 만들면 될 것 같은데.

d = [[0, 7, 0]]

for i in range(TC):
    empty = []
    empty.append()

