class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'{self.name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')

member = Person("강호동", 45)

print(f'{member.name} is {member.age}살 입니다')
print(dir(member))