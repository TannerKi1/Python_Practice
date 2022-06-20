class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.__name))

# self가 가리키는 객체공간에 name, age라고 하는 필드가 생성됨.

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.__name))

    def to_str(self):
        return "{0}".format(self.__name)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise TypeError("나이는 양수의 값만 설정가능합니다")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("가나다", 40),
    Person("김삼성", 55)
]

members[0].set_age(-40900)

for member in members:
    print(member.to_str())