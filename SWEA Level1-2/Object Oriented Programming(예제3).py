class Person:
    pass


member = Person()

if isinstance(member, Person):

# 첫 번째 인자의 객체가 두 번째 인자의 클래스 인스턴스인지 검사함.
    print("member는 Person 클래스의 인스턴스입니다.")


# 클래스 '생성자' 매서드 정의

class 클래스명:
    def __init__(self, 매개변수목록):

# 클래스 '소멸자' 매서드 정의

class 클래스명:
    def __del__(self):
        
