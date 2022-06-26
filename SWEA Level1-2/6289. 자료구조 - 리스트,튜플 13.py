

# 아이디어
# 숫자열을 문자열로 바꾼다.
# 문자열을 따로 저장한다음에, 이걸 숫자로 바꿔서 더한다.

a_str = str(input())
c = []
for x in a_str:
    c.append(int(x))

print(sum(c))
