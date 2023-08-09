import random


class Matrix:
    def __init__ (self, size_r, size_c, matrix=None):
        self.size_r = size_r
        self.size_c = size_c
        if matrix is None:
            self.matrix = [[random.randint(1, 100) for _ in range(size_c)] for _ in range(size_r)]
        else:
            self.matrix = matrix

    def __str__ (self):
        """Выводит матрицу поэлементно без знаков списков"""
        res = ''
        for i in range(self.size_r):
            sub_res = ''
            for j in range(self.size_c):
                sub_res += str(self.matrix[i][j]) + ' '
            res += sub_res + '\n'
        return res

    def __add__ (self, other):
        """Сумма матриц возможна только для матриц одной размерности"""
        if self.size_r == other.size_r and self.size_c == other.size_c:
            res = []
            for i in range(self.size_r):
                sub_res = []
                for j in range(self.size_c):
                    sub_res.append(self.matrix[i][j] + other.matrix[i][j])
                res.append(sub_res)
            return Matrix(self.size_r, self.size_c, res)
        else:
            return 'matrix measurments are unequal! sum is unreacheable'

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
            return 'matrix measurments are unequal! result is unreacheable'

    def __mul__ (self, other):
        if self.size_c == other.size_r:
            res = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other.matrix)] for row_a in self.matrix]
            return Matrix(self.size_r, other.size_c, res)
        else:
            return 'matrix measurments are unequal! result is unreacheable'


m = Matrix(1, 2)
n = Matrix(2, 1)
lst = [[1, 0]]
k = Matrix(1, 2, lst)
y = Matrix(1, 2, lst)

print(m)
print(n)
print(m * n)
# print(m+n)
# print(m == n)

# print(k)
# print(y)
# print(k == y)
