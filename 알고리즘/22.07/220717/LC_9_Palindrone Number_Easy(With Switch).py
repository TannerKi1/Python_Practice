# reverse 함수를 쓰지 말고 한 번 풀어보자.

x = int(input())

x_string = str(x)

i = 0
j = len(x_string) - 1

while i == j:
    print(True)
    break

while i < j:
    if x_string[i] == x_string[j]:
        i += 1
        j -= 1

    elif x_string[i] != x_string[j]:
        print(False)
        break

print(True)






# 1000021 반례
# False와 True가 동시에 나와버리는데 어케 해결하지?