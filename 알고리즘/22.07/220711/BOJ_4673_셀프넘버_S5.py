
new_arr = []

for i in range(1, 10001):
    arr = []
    for item in str(i):

        arr.append(item)
    arr_int = map(int, arr)
    new_number = sum(arr_int) + i
    new_arr.append(new_number)



compare_a = [i for i in range(1, 10001)]
new_set = set(compare_a) - set(new_arr)
new_list = list(new_set)
new_list_sorted = sorted(new_list)

for i in new_list_sorted:
    print(i)
