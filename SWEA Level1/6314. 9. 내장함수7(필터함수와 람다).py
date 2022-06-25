
# 1~10 까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

# filter 함수를 잘 설명한 주소: https://www.daleseo.com/python-filter/

# filter(x, y) = y라는 전체 리스트에서, x를 충족시키는 것만 뽑아낸다. 그런데 x를 람다로 설정해서 문장 하나로 할 수 있다.

a = [x for x in range(1,11)]
c = []

for even_number in filter(lambda x: x%2 ==0, a):
    c.append(even_number)
print(c)

# 말 안듣고 리스트 컴프리헨션으로 작성하면 아래와 같이 작성할 수 있음.

b = [x for x in range(1,11) if x%2 ==0]

print(b)


# filter와 람다식을 이용해 리스트를 반환한다면?

