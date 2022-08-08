
# 파이썬으로 구현
# 리스트 5개짜리에
# input 5번이 들어와서 각각 이름을 채우고
# 그 이후에는 5번의 이름들이 순차적으로 프린팅 아웃
# 만약 특정이름이 있으면 프린팅 아웃 되는게 멈춤

n = int(input())
arr = []
for x in range(n):
    arr.append(input())

for x in arr:
    print(x)

    if x == 'tim':
        break


