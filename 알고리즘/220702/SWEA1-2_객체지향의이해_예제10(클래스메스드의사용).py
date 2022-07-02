
class Person:
    count = 0


    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
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

    @classmethod
    def get_info(cls):
        return(f'현재 Person 클래스의 인스턴스는 총 {cls.count}개 입니다.')

members = [
    Person("홍길동", 20),
    Person("김기훈", 50),
    Person("고기정", 5612)
]

print(Person.get_info())