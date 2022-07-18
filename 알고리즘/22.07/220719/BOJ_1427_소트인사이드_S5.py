N = str(input())

empty_arr = []
for x in N:
    empty_arr.append(x)

new_arr = list(map(int, empty_arr))

new_arr.sort(reverse = True)

for x in new_arr:
    print(x, end='')




