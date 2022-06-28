

a = [12,24,35,24,88,120,155,88,120,155]


def double():
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)

    print(b)

double()
