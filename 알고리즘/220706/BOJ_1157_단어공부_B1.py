W = input()

arr = [0] * 26

w_1 = W.lower()

for k in w_1:
    x = ord(k) - 97
    arr[x] += 1

alpha = arr.index(max(arr))

if arr.count(max(arr)) >= 2:
    print("?")

else:
    print(chr(alpha+97).upper())