

T = input()

k = list(map(str, T.split()))


# 중복값을 어떻게 제거할 것인가...?

y = []

for x in k:
    if x not in y:
        y.append(x)
    else:
        continue

# y의 위치에 따라서 list 값이 달라지네. for 내부인지, 외부인지에 따라서.. 내부에 있으면 y = []가 도르마무 되는군

y_sorted = sorted(y)

print(','.join(y_sorted))


