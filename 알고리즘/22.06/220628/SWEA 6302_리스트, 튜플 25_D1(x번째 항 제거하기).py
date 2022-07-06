

a = [12, 24, 35, 70, 88, 120, 155]

# a[0], a[4], a[5]를 제거한 값을 리스트 출력을 해야하는 상황


# index라는 함수를 몰라서 일어난 사건....!!!!


b = [i for i in a if a.index(i) == 1 or a.index(i) == 2 or a.index(i) == 3 or a.index(i) == 6 ]

print(b)


