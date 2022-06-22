
# 내가 생각한 방법

# 리스트에서 어떻게 중복된 값을 없앨까?
# 하나씩 pop으로 빼서, if문으로 안 중복되면 넣고, 중복되면 pass하는 걸 만들어볼까?

a = [1, 2, 3, 4, 3, 2, 1]
b = []

def func():
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
    return

# 굳이 pop으로 할 필요도 없고, for 문으로 훑으면서 조회를 해보면 됨

print(a)

func()