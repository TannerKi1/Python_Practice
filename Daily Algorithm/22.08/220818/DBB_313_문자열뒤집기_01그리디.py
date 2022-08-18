data = input()


answer = []
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        answer.append(i)

if len(answer) % 2 != 0 :
    print(len(answer) // 2 + 1)

else:
    print(len(answer) // 2)