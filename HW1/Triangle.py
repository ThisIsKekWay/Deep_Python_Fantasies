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

class Triangle:
    def __init__ (self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_info (self):
        if self.type != None:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} {self.exist}' \
                  f' и имеет тип: {self.type}'
        else:
            res = f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}  {self.exist}'
        return res

    def exist_triangle (self):
        if self.side_a < self.side_b + self.side_c \
                or self.side_b < self.side_c + self.side_a \
                or self.side_c < self.side_b + self.side_a:
            self.exist = 'существует'
            self.typizate_triangle()
        else:
            self.exist = 'не существует'
            self.type = None

    def typizate_triangle (self):
        if self.side_a == self.side_b == self.side_c:
            self.type = 'равносторонний'
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a:
            self.type = 'равнобедренный'
        else:
            self.type = 'разносторонний'


while True:
    try:
        print('Enter triangle data')
        side_a, side_b, side_c = int(input()), int(input()), int(input())
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise Exception
        break
    except Exception:
        print('Wrong data')

triangle = Triangle(side_a, side_b, side_c)
triangle.exist_triangle()
info = triangle.get_info()
print(info)
