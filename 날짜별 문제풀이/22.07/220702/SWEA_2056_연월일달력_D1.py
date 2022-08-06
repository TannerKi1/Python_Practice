
# YYYYMMDD로 들어온 숫자가 유효하면 YYYY/MM/DD로 프린팅하고, 날짜가 유효하지 않으면 -1을 출력해야한다.

# 13월이나, 2월이 31일로 들어오면 x쳐야함.

T = int(input())

for i in range(1, T+1):
    x = str(input())

    year = x[0:4]
    month = x[4:6]
    day = x[6:8]

    if month <= '00' or month >= '13':
        print(f'#{i} -1')

    if month == '01':
        if '01' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '02':
        if '1' <= day <= '28':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '03':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '04':
        if '1' <= day <= '30':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '05':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '06':
        if '1' <= day <= '30':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '07':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '08':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '09':
        if '1' <= day <= '30':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '10':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '11':
        if '1' <= day <= '30':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')

    if month == '12':
        if '1' <= day <= '31':
            print(f'#{i} {year}/{month}/{day}')
        else:
            print(f'#{i} -1')


