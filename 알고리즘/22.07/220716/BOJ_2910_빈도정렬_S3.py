N, C = map(int, input().split())
unsorted_list = map(int, input().split())
answer_dict = dict()

for num in unsorted_list:
    if num not in answer_dict:
        answer_dict[num] = 1
    else:
        answer_dict[num] += 1

print(answer_dict)

for key, values in answer_dict.items(key = values):


