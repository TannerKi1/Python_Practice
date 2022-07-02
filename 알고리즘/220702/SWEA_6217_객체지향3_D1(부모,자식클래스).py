
# 부모클래스에는 name 프로퍼티를 가진 Student가 있고

# 자식클래스에는 major 프로퍼티를 가진 GraduateStudent가 있고


class Parent:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f'이름: {self.__name}'


class Child(Parent):
    def __init__(self, name, major):
        self.__name = name
        self.__major = major

    def __repr__(self):
        return f'이름: {self.__name}, 전공: {self.__major}'

students = [
    Parent("홍길동"),
    Child("이순신", "컴퓨터")
]

for student in students:
    print(student)

# 과연 이게 문제에서 원하던 값일까...라는 거지