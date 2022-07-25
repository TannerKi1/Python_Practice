TC = int(input())

for x in range(TC):
    stack = []
    arr = input()

    for x in arr:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop(-1)

    else: # for문이 다 돌고 나서 결과값을 정의해주게 된다!.
        if len(stack) >= 1:
            print('NO')

        if len(stack) == 0:
            print('YES')

# ------ # 무슨 차이?

# TC = int(input())
#
# for x in range(TC):
#     stack = []
#     arr = input()
#
#     for x in arr:
#         if x == '(':
#             stack.append(x)
#         elif x == ')':
#             if len(stack) == 0:
#                 print('NO')
#                 break
#             else:
#                 stack.pop(-1)
#
#
#     # 아래같이 하면 for x in arr와 상관없이 별개로 돌아가게 된다?
#     if len(stack) >= 1:
#         print('NO')
#
#     if len(stack) == 0:
#         print('YES')




