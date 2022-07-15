# 수가 3개니까 버블소팅해도 되고..

# 그냥 0, 1, 2 비교해서 짜는 식으로 해도 되고

unsorted_list = list(map(int, input().split()))

for i in range(len(unsorted_list)):
    for j in range(1, len(unsorted_list)-i):
        if unsorted_list[i] > unsorted_list[i+j]:
            unsorted_list[i], unsorted_list[i+j] = unsorted_list[i+j], unsorted_list[i]

for num in unsorted_list:
    print(num, end = ' ')