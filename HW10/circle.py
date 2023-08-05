# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


from math import pi


class Circle:
    def get_name (self):
        for i, j in globals().items():
            if j is self:
                return i

    def __init__ (self, radius):
        self.radius = radius

    def __str__ (self):
        return (f'Окружность {self.get_name()} радиусом {self.radius} имеет следующие параметры:\n'
                f'Длина окружности: {round(2 * pi * self.radius, 2)}\n'
                f'Площадь окружности: {round(pi * self.radius ** 2, 2)}\n')


pupa = Circle(30)
lupa = Circle(20)
print(pupa)
print(lupa)
