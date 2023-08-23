import pytest
from HW14.argparser_tria.Triangle import *


def test_str_bad ():
    right_ans = 'Треугольник со сторонами 10, 5, 3 не существует'
    assert str(Triangle(10, 5, 3)) == right_ans, 'Что-то не так'


def test_str_good ():
    right_ans = 'Треугольник со сторонами 3, 4, 5 существует и имеет тип: разносторонний'
    assert str(Triangle(3, 4, 5)) == right_ans, 'Что-то не так'


def test_value ():
    with pytest.raises(SideValueError):
        assert Triangle(10, 5, 0)
        assert Triangle(10, 5, -5)


def test_type ():
    with pytest.raises(SideTypeError):
        assert Triangle(10, 'двенадцать', 5)


if __name__ == '__main__':
    pytest.main()
