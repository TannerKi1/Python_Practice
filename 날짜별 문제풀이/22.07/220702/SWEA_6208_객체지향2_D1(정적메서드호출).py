
class Korean:
    @staticmethod
    def printNationality():
        return "대한민국"

print(Korean.printNationality())
print(Korean.printNationality())

# 정적메소드는
# @staticmethod 라고 함!

#
# class Korean:
#     def __init__(self, name, nationality):
#         self.__name = name
#         self.__nationality = nationality
#
#     def __repr__(self):
#         return f'{self.__nationality}'
#
# Students = [
#     Korean("기태훈", "대한민국")
# ]
#
# for student in Students:
#     print(student)
#     print(student)