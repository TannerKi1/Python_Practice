

a = [1, 2, 3, 4, 5]
b = []
def check(a):
    for x in a :
        if x % 2 == 0:
            b.append(x)
    print(b)

check(a)