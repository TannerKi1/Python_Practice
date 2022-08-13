class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __repr__(self):
        return f'원의 면적: {3.14 * int(self.__radius) * int(self.__radius)}'


print(Circle(2))
