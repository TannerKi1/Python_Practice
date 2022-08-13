T = int(input())

stack = []
for _ in range(T):
    x = int(input())
    if x != 0:
        stack.append(x)
    elif x == 0:
        del stack[-1]

print(sum(stack))
