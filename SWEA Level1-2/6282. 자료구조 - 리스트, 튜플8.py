k = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
b = []


def check(k):
    for x in k:
        if x % 2 == 0:
            b.append(x)
        else:
            continue

    print(b)


check(k)