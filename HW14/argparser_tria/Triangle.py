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

from all_logger import log_info, log_warn
import argparse

class SideTypeError(Exception):
    def __init__ (self, side):
        self.side = side

    def __str__ (self):
        return f'Значение длины стороны треугольника должно быть только в натуральных числах и в числовой форме. ' \
               f'Ваше значение: {self.side}'


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
        except ValueError:
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
        self.typicality_triangle()
        self.exist_triangle()

    def __str__ (self):
        if self.type is not None:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} {self.exist} ' \
                  f'и имеет тип: {self.type}'
        else:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} {self.exist}'
        return res

    def exist_triangle (self):
        if \
                self.side_a < self.side_b + self.side_c and \
                        self.side_b < self.side_c + self.side_a and \
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
    parser = argparse.ArgumentParser(description='Проверяет возможность существования треугольника')
    parser.add_argument('a', metavar='a', type=int, help='Введите сторону А треугольника')
    parser.add_argument('b', metavar='b', type=int, help='Введите сторону B треугольника')
    parser.add_argument('c', metavar='c', type=int, help='Введите сторону C треугольника')
    args = parser.parse_args()
    try:
        t = Triangle(args.a, args.b, args.c)
        log_info(t)
    except SideValueError as e:
         log_warn(e)
    except SideTypeError as e:
         log_warn(e)

    # while True:
    #     print('Enter triangle data')
    #     side_a, side_b, side_c = input().split(' ')
    #     try:
    #         triangle = Triangle(side_a, side_b, side_c)
    #         log_info(triangle)
    #         break
    #     except SideValueError as e:
    #         log_warn(e)
    #     except SideTypeError as e:
    #         log_warn(e)
