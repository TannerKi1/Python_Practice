x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum_day = sum(month[:(x - 1)])+y
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(0, 7):
    if sum_day % 7 == i:
        print(day_list[i])
    else:
        continue
