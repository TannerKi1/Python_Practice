
# 사용자가 입력한 문장에서

# 숫자와, 문자를 구별해 카운팅을 한다...?
#
T = input()

# 그냥 str으로 받았는데, 1, 2, 3 을 어떻게 문자로 인식한담...?

m = 0
n = 0

test = [i for i in range(1, 10)]

new_k = list(map(str, test))
#
for x in T:
    if 'a' < x < 'z':
        m += 1
    elif x in new_k:
        n += 1

print(f'LETTERS {m}')
print(f'DIGITS {n}')

# 다르게 풀기

# map을 이용해서 k를 좀 더 빠르게 만들어준다? 언제까지 하드코딩을 할 수는 없잖아.





# 이렇게하면 k 바로 만들 수 있을듯