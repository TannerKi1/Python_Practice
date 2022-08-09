# 다시푸는 문제

# sort함수에 키 제대로 넣을 수 있나 보는 거임.

N = int(input())
student = []
for _ in range(N):
    student.append(input().split())


student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# - 기호의 위치에 대해서 생각해보기. 값을 음수로 받는게 아니라, 값을 내림차순으로 받겠다는 거니까 밖에 있어야 함

# 키값의 형식이 무엇인지 이야기해주어야 문자순인지, 숫자순인지 정렬할 수 있음. str 숫자인지 int 숫자인지.

for x in student:
    print(x[0])

