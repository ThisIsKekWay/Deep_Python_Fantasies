import argparse
import random
from all_logger import *

class MatrixElementsError(Exception):
    def __init__ (self, matrix):
        self.mat = matrix

    def __str__ (self):
        return f'martix rows are not equal. your matrix: {self.mat}'


class Matrix:

    @staticmethod
    def validate (matrix):
        for i in range(len(matrix)):
            len_prev = len(matrix[i - 1])
            if len(matrix[i]) != len_prev:
                raise MatrixElementsError(matrix)
        return matrix

    def __init__ (self, size_r, size_c, matrix=None):
        self.size_r = size_r
        self.size_c = size_c
        if matrix is None:
            self.matrix = [[random.randint(1, 100) for _ in range(size_c)] for _ in range(size_r)]
        else:
            self.matrix = self.validate(matrix)

    def __str__ (self):
        res = ''
        for i in range(self.size_r):
            sub_res = ''
            for j in range(self.size_c):
                sub_res += str(self.matrix[i][j]) + ' '
            res += sub_res + '\n'
        return res

    def __add__ (self, other):
        if self.size_r == other.size_r and self.size_c == other.size_c:
            res = []
            for i in range(self.size_r):
                sub_res = []
                for j in range(self.size_c):
                    sub_res.append(self.matrix[i][j] + other.matrix[i][j])
                res.append(sub_res)
            return Matrix(self.size_r, self.size_c, res)
        else:
            return 'matrix measurements are unequal! sum is unreachable'

    def __eq__ (self, other):
        if self.size_r == other.size_r and self.size_c == other.size_c:
            res = False
            counter = 0
            for i in range(self.size_r):
                for j in range(self.size_c):
                    if self.matrix[i][j] == other.matrix[i][j]:
                        counter += 1
            if counter == self.size_r * self.size_c:
                res = True
            return res
        else:
            return 'matrix measurements are unequal! result is unreacheable'

    def __mul__ (self, other):
        if self.size_c == other.size_r:
            res = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other.matrix)] for row_a in self.matrix]
            return Matrix(self.size_r, other.size_c, res)
        else:
            return 'matrix measurements are unequal! result is unreacheable'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Проверяет возможность существования треугольника')
    parser.add_argument('rows', metavar='a', type=int, help='Введите число рядов матрицы')
    parser.add_argument('cols', metavar='b', type=int, help='Введите число столбцов матрицы')
    parser.add_argument('-list', metavar='c', type=list, help='Введите матрицу, если придумали', default=None)
    args = parser.parse_args()

    try:
        k = Matrix(args.rows, args.cols, args.list)
        log_info(f'Ваша матрица:\n{k}')
    except MatrixElementsError as e:
        log_warn(e)
