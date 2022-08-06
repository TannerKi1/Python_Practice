
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'{self.name}객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.name}객체가 제거되었습니다.')

    def to_str(self):
        return(f'{self.name}\t{self.age}')

members = [
    Person("홍길동", 29),
    Person("김기훈", 50),
    Person("고기정", 5234),
]

for member in members:
    print(member.to_str())
