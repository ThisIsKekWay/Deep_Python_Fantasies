# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат
class Rectanlge:

    def get_name (self):
        for i, j in globals().items():
            if j is self:
                return i

    def __init__ (self, *args):
        if len(args) == 1:
            self.side_a = self.side_b = args[0]
            self.form = 'Квадрат'
        else:
            self.side_a = args[0]
            self.side_b = args[1]
            self.form = 'Прямоугольник'

    def __str__ (self):
        return (f'{self.form} {self.get_name()} с параметрами\n '
                f'{self.side_a = } {self.side_b = } имеет следующие параметры:\n'
                f'Площадь: {self.side_a * self.side_b}\n'
                f'Периметр: {(self.side_a + self.side_b) * 2}\n')


some_rect = Rectanlge(20, 10)
some_square = Rectanlge(6)
print(some_square)
print(some_rect)
