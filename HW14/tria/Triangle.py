# Deep python. Homework 1.
# Task 1.
# Треугольник существует только тогда, когда сумма любых двух
# его сторон больше третьей. Дано a, b, c — стороны 
# предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы
# двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.


class SideTypeError(Exception):
    def __init__ (self, side):
        self.side = side

    def __str__ (self):
        return f'Значение длины стороны треугольника должно быть только в числовой форме. Ваше значение: {self.side}'


class SideValueError(Exception):
    def __init__ (self, side):
        self.side = side

    def __str__ (self):
        return f'Сторона треугольника не может быть меньше или равна нулю. Ваше значение: {self.side}'


class Side:
    @classmethod
    def verify_side (cls, value):
        try:
            int(value)
        except ValueError as e:
            raise SideTypeError(value)
        if int(value) <= 0:
            raise SideValueError(value)

    def __set_name__ (self, owner, name):
        self.name = "_" + name

    def __get__ (self, instance, owner):
        return instance.__dict__[self.name]

    def __set__ (self, instance, value):
        self.verify_side(value)
        instance.__dict__[self.name] = value


class Triangle:
    side_a = Side()
    side_b = Side()
    side_c = Side()

    def __init__ (self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.exist_triangle()
        self.typicality_triangle()


    def __str__(self):
        if self.type is not None:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} {self.exist} ' \
                  f'и имеет тип: {self.type}'
        else:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}  {self.exist}'
        return res

    def exist_triangle (self):
        if \
            self.side_a < self.side_b + self.side_c or \
            self.side_b < self.side_c + self.side_a or \
            self.side_c < self.side_b + self.side_a:


            self.exist = 'существует'
            self.typicality_triangle()
        else:
            self.exist = 'не существует'
            self.type = None

    def typicality_triangle (self):
        if self.side_a == self.side_b == self.side_c:
            self.type = 'равносторонний'
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a:
            self.type = 'равнобедренный'
        else:
            self.type = 'разносторонний'


if __name__ == '__main__':
    while True:
        print('Enter triangle data')
        side_a, side_b, side_c = input().split(' ')
        try:
            triangle = Triangle(side_a, side_b, side_c)
            print(triangle)
            break
        except SideValueError as e:
            print(e)
        except SideTypeError as e:
            print(e)
