

class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return f'{self.__class__.__name__}(name: {self.name} gender: {self.gender} height: {self.height})'
            # Class의 정의된 이름을 부르는 것?!
            # 객체를 뽑을 때 __repr__을 이용함

students = [
    Student("홍길동", "남", 175),
    Student("김혜민", "여", 164),
    Student("장주빈", "남", 174.4)
]

for x in students:
    print(x)
    
print("name으로 오름차순 정렬 후 ===>")
for x in sorted(students, key = lambda x: x.name):
    print(x)

print("name으로 내림차순 정렬 후 ===>")
for x in sorted(students, key = lambda x: x.name, reverse = True):
    print(x)

print("height으로 오름차순 정렬 후 ===>")
for x in sorted(students, key = lambda x: x.height):
    print(x)

print("height으로 내림차순 정렬 후 ===>")
for x in sorted(students, key = lambda x: x.height, reverse = True):
    print(x)

print(type(x))