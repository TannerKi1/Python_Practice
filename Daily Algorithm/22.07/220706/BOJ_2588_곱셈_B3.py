# 세자리 자연수 x 세자리 자연수...
A = int(input())
B = int(input())

# A, B를 받았고
# a b c
# d e f

B_new = str(B)
f = int(B_new[2])
e = int(B_new[1])
d = int(B_new[0])

print(A * f)
print(A * e)
print(A * d)
print(A * B)