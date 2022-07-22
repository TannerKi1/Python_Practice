
T = list(map(str, input().split(',')))

kor = T[0]
eng = T[1]
math = T[2]

class Student:
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def __repr__(self):
        return f'국어, 영어, 수학의 총점: {int(self.__kor) + int(self.__eng) + int(self.__math)}'


students = [
    Student(T[0], T[1], T[2])
]

for student in students:
    print(student)

