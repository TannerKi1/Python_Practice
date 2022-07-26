N = 10
arr = []
for x in range(10):
    arr.append(int(input()))

arr_42 = []
for y in arr:
    arr_42.append(y % 42)

print(len(set(arr_42)))


# set을 이용하면 중복을 빠르게 날릴 수 있다.