s = "loveleetcode"

dict_ = dict()

for char in s:
    if char not in dict_:
        dict_[char] = 1
    else:
        dict_[char] += 1

print(dict_)

for key, val in dict_.items():
    if val == 1:
        print(s.index(key))
        break
else:
    print(-1)