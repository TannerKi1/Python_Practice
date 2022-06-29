
# 리스트의 원소를 key로 받고, 그 원소의 len값을 value로 받아보자.
    # key = 원소로 정의
    # value = 원소의 len(   ) 값을 받아온다.

# 원소의 공백은 제거되어야 한다.
    # strip()함수를 쓰면 되지 않을까?


fruit = ['   apple    ','banana','  melon']
new_fruit = []

for x in fruit:
    new_fruit.append(x.strip())

# 1단계 완료

d_fruit = {}

for y in new_fruit:
    d_fruit[y] = len(y)

# dict에는 append가 없다!!! 저렇게 그냥 등호로 같다고 정리해주면 값이 계속 들어가게 된다.

print(d_fruit)


