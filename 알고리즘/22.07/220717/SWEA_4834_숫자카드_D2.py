T = int(input())
for i in range(T):
    dict_num = dict()
    N = int(input())
    number = str(input())
    for char in number:
        if char not in dict_num:
            dict_num[char] = 1
        else:
            dict_num[char] += 1

    for key, value in dict_num.items():


