N = list(map(int, input().split()))
A = N[0]
B = N[1]
C = N[2]

print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
