N = int(input())
import sys
list_ = []
for _ in range(N):
    list_.append(int(sys.stdin.readline()))

list_.sort()

def value_count(list):
    dict_ = {}
    for x in list_:
        if x not in dict_:
            dict_[x] = 1
        else:
            dict_[x] += 1

    max_key = []
    for key, val in dict_.items():
        if val == max(dict_.values()):
            max_key.append(key)

    max_key.sort()

    if len(max_key) == 1:
        return max_key[0]

    elif len(max_key) >= 2:
        return max_key[1]

print(round(sum(list_)/len(list_)))
print(list_[(len(list_) - 1) // 2])
print(value_count(list_))
print(list_[-1] - list_[0])
