

class Person:
    count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print(f'{self.__name}이 생성되었습니다.')

    def __del__(self):
        print(f'{self.__name}객체가 제거되었습니다.')

    def to_str(self):
        return(f'{self.__name}\t{self.__age}')

members = [
    Person("홍길동", 20),
    Person("김기훈", 50),
    Person("고기정", 5612)
]

print(f'현재 Person 클래스의 인스턴스는 총 {Person.count}개 입니다.')