W = str(input())

array = [0] * 26

for x in W:
    array[ord(x)-97] += 1

for j in array:
    print(j, end=' ')