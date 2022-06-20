# 예제1

members = [
    {"name": "홍길동", "age": 20},
    {"name": "이순신", "age": 45},
    {"name": "강감찬", "age": 35}
]

for member in members:
    print(member["name"])

# 예제2

def create(name, age):
    return {"name": name, "age": age}

def to_str(person):
    return person["name"]

members = [
    create("김길동", 20),
    create("이선신", 45),
    create("강감춘", 35)
]

for member in members:
    print(to_str(member))