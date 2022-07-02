
# getter : 멤버를 읽어오는 메서드
# setter : 멤버를 변경하는 메서드

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print(f'{self.__name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.__name} 객체가 삭제되었습니다.')

    def to_str(self):
        return (f'{self.__name}\t{self.__age}')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 56)
]

members[0].set_age(2512341)

for member in members:
    print(member.to_str())
