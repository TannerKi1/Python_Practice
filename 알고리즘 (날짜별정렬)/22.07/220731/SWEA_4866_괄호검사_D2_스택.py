T = int(input())

for tc in range(1, T+1):
    arr = input()
    stack = []
    for x in arr:
        if x == '(':
            stack.append(x)
        elif x == '{':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                print(f'#{tc} 0')
                break
            else:
                if stack[-1] == '{':
                    print(f'#{tc} 0')
                    break
                else:
                    stack.pop(-1)
        elif x == '}':
            if len(stack) == 0:
                print(f'#{tc} 0')
                break
            else:
                if stack[-1] == '(':
                    print(f'#{tc} 0')
                    break
                else:
                    stack.pop(-1)
    else:
        if len(stack) == 0:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')

# 스택안에 남은 경우
# 스택안에 뺄 게 없는데, 빼라는 기호가 나온 경우
# 왼쪽 오른쪽 괄호의 종류가 맞지 않는 경우

