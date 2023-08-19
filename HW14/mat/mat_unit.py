import unittest
from MatClass import Matrix, MatrixElementsError


class MyTestCase(unittest.TestCase):

    def test_bad_matrix(self):
        mat = [[1, 2, 3], [4, 5, 6, 0], [7, 8, 9]]
        self.assertRaises(MatrixElementsError, Matrix.validate, mat)

    def test_good_matrix(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(Matrix.validate(mat), mat, msg='Случилось невероятное')


if __name__ == '__main__':
    unittest.main()
