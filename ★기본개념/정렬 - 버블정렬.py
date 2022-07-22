

bubble = [1, 3, 2, 4, 7, 6, 9, 8, 5]

for j in range(len(bubble)): # len(bubble)의 값은 9
    k = len(bubble) - j
    for i in range(1, k):
        if bubble[i-1] >= bubble[i]:
            temp = bubble[i-1]
            bubble[i-1] = bubble[i]
            bubble[i] = temp

print(bubble)

# 점점 비교 단위가 짧아지면서 5가 가기 자리로 돌아오게 된다.




