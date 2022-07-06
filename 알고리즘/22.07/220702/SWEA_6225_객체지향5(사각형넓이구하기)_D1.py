class Rectangle:
    def __init__(self, garo, sero):
        self.garo = int(garo)
        self.sero = int(sero)

    def __repr__(self):
        return f'사각형의 면적: {self.garo * self.sero}'

print(Rectangle(5, 4))
