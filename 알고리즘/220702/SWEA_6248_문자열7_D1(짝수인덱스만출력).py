

k = 'H1e2l3l4o5w6o7r8l9d'

list_k = list(k)

for x in list_k:
    b = []
    for j in range(0, len(list_k)):
        if j % 2 == 0:
            b.append(list_k[j])

print(''.join(b))



