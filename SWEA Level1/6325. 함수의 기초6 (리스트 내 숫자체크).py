
a = [2, 4, 6, 8, 10]

def num_check(b,a):
    if b in a:
        print(f'{b} => True')
    else:
        print(f'{b} => False')

num_check(5,a)
num_check(10,a)

# 무조건 for을 돌려야하는 것도 아님.
# if로 잡아줘도 어쨌거나 뒤의 a안에 리스트는 한번 다 돌게 됨.

