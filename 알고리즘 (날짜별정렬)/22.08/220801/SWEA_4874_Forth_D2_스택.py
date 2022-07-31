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
                two_sum = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(two_sum)

        elif i == '*':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                two_times = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(two_times)

        elif i == '-':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                two_minus = stack[-1] - stack[-2]
                stack.pop()
                stack.pop()
                stack.append(two_minus)

        elif i == '/':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            else:
                two_dev = stack[-1] / stack[-2]
                stack.pop()
                stack.pop()
                stack.append(two_dev)

        elif i == '.':
            print(f'#{tc} {stack[-1]}')