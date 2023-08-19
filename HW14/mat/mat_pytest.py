import pytest
from MatClass import Matrix, MatrixElementsError


def test_bad_matrix ():
    mat = [[1, 2, 3], [4, 5, 6, 0], [7, 8, 9]]
    with pytest.raises(MatrixElementsError):
        assert Matrix.validate(mat)


def test_good_matrix ():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Matrix.validate(mat) == mat


if __name__ == '__main__':
    pytest.main()
