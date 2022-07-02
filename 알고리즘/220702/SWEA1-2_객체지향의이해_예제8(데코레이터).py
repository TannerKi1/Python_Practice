
# 변수 이름과 같은 메서드를 만들어 사용할 수 있다.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print(f'{self.__name}이 생성되었습니다.')

    def __del__(self):
        print(f'{self.__name}이 삭제되었습니다.')

    def to_str(self):
        return(f"{self.__name}\t{self.__age}")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("김기훈", 50),
    Person("고기정", 5612)
]

members[0].age = 22

for member in members:
    print(member.to_str())

