TC = int(input())

for tc in range(1, TC+1):
    stack = []
    p_list = ['*', '.', '-', '/', '+']
    n_list = list(input().split())
    for i in n_list:
        if i not in p_list:
            stack.append(int(i))

        elif i == '+':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

        elif i == '*':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

        elif i == '-':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

        elif i == '/':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)

        elif i == '.':
            if len(stack) > 1:
                print('error')
            else:
                a = stack.pop()
                print(f'#{tc} {a}')