class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

# self가 가리키는 객체공간에 name, age라고 하는 필드가 생성됨.

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return f'{self.name}\t{self.age}'

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

members[0].age = 2000

# 잘못된 값이 들어가버리는 사태가 발생할 수 있다.

for member in members:
    print(member.to_str())

# 직접 class로 들어가서 헤집는 것을 미리 방지하는 기능 정도로 정리해보자

# self.name (이건 공개)
# self.__name (이건 Private)

# Private가 등장했으면 getter / setter에 대한 고민이 같이 이루어져야한다.