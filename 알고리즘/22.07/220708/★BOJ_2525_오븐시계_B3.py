A, B = input().split()
C = int(input())

C_new_hour = C // 60
C_new_minute = C - (C_new_hour * 60)


# 분이 60분일 때에 대한 예외처리
if new_new_minute >= 60:
    new_new_minute -= 60
    new_new_hour += 1

    if new_new_hour >= 24:
        new_new_hour -= 24

# 시간이 24시일 때에 대한 예외처리가 필요함

print(new_new_hour, end=' ')
print(new_new_minute)






