# Getter와 Setter를 쓰는 대신에, 데코레이터(decorator)기능을 사용할 수 있다.

# 변수이름과 동일한 이름을 가진 '메서드'를 만들어 사용 가능
# 원래는 변수 | 메서드 인데 이게 혼용이 된다는거지.

# @property 를 사용하거나, @property의이름.setter이런 식으로 사용

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