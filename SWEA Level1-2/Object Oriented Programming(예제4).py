class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

# self가 가리키는 객체공간에 name, age라고 하는 필드가 생성됨.

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

member = Person("기태훈", 29)

print("{0}\t{1}".format(member.name, member.age))
print(dir(member))

# 문장의 1~4 나온 순서를 눈여겨볼 필요가 있겠네.