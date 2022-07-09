A, B = map(int, input().split())
C = int(input())

ready_new_hour = (B+C) // 60
ready_new_minute = (B+C) - (ready_new_hour * 60)

real_new_hour = A + ready_new_hour
real_new_minute = ready_new_minute

if real_new_hour == 24:
    real_new_hour = 0

if real_new_hour > 24:
    real_new_hour %= 24

print(real_new_hour, real_new_minute)





