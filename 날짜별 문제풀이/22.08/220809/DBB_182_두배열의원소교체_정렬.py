n, k = map(int, input().split())

min_arr = list(map(int, input().split()))
max_arr = list(map(int, input().split()))

min_arr.sort()
max_arr.sort(reverse=True)


life = k

for i in range(n):
    if min_arr[i] < max_arr[i]:
        min_arr[i] = max_arr[i]
        life -= 1

    if life == 0:
        break



print(min_arr)
print(life)
