
a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b = 'aeiou'
c = [x for x in a if x not in b]

# 이것까진했는데, print 해보면 분리되어 나오고 있는 것을 알 수 이 때
# 이걸 합쳐주는 함수를 알고 있어야 함
# join을 이용해보자
# .join 앞에는 무엇을 이용해 연결할 것인지, 괄호 안에는 연결할 값들을 다양하게 선택
# ex)

d = ['김', '단무지', '햄', '우엉']
d_comp = '-'.join(d)
d_comp2 = '---'.join(d)
print("-로 연결한 값을 출력해보겠습니다.")
print(d_comp)

print("---로 연결한 값을 출력해보겠습니다.")
print(d_comp2)

print(a)
print(''.join(c))