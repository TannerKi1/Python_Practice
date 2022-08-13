
# 부모클래스에는 name 프로퍼티를 가진 Student가 있고

# 자식클래스에는 major 프로퍼티를 가진 GraduateStudent가 있고


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f'이름: {self.name}'


class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return f'{Student.__repr__(self)}, 전공: {self.major}'


student1 = Student("홍길동")
student2 = GraduateStudent("이순신", "컴퓨터")
print(student1)
print(student2)

