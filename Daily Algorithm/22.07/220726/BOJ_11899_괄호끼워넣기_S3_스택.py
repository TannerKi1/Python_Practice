arr = input()


count = 0
stack = []
for x in arr:
    if x == ')':
        if len(stack) == 0:
            count += 1
        else:
            stack.pop(-1)

    elif x == '(':
        stack.append(x)


print(count + len(stack))