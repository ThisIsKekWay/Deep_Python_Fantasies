import unittest
from Triangle import *


class MyTestCase(unittest.TestCase):
    def test_str_bad (self):
        right_ans = 'Треугольник со сторонами 10, 5, 3 не существует'
        self.assertEqual(str(Triangle(10, 5, 3)), right_ans, 'Что-то не так')

    def test_str_good (self):
        right_ans = 'Треугольник со сторонами 3, 4, 5 существует и имеет тип: разносторонний'
        self.assertEqual(str(Triangle(3, 4, 5)), right_ans, 'Что-то не так')

    def test_value (self):
        self.assertRaisesRegex(SideValueError,
                               'Сторона треугольника не может быть меньше или равна нулю. Ваше значение: 0', Triangle,
                               10, 5, 0)

        self.assertRaisesRegex(SideValueError,
                               'Сторона треугольника не может быть меньше или равна нулю. Ваше значение: -5', Triangle,
                               10, 5, -5)

    def test_type (self):
        self.assertRaisesRegex(SideTypeError,
                               'Значение длины стороны треугольника должно быть только '
                               'в натуральных числах и в числовой форме. '
                               'Ваше значение: двенадцать', Triangle, 10, 'двенадцать', 0)


if __name__ == '__main__':
    unittest.main()
