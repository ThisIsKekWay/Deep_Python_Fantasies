Docfile for matrix validation module
===

Description of the Triangle class
---

The triangle class accepts three positional arguments denoting the sides of the triangle.
During initialization, dunder init checks the existence of a triangle and its type. 
In case of incorrect input, exceptions are raised depending on the type of incorrect input.

>>> from Triangle import *
 
>>> print(Triangle(10, 5, 2))
Треугольник со сторонами 10, 5, 2 существует и имеет тип: разносторонний
 
>>> print(Triangle(10, 5, 0))
Traceback (most recent call last):
...
Triangle.SideValueError: Сторона треугольника не может быть меньше или равна нулю. Ваше значение: 0

>>> print(Triangle(10, 5, -5))
Traceback (most recent call last):
...
Triangle.SideValueError: Сторона треугольника не может быть меньше или равна нулю. Ваше значение: -5

>>> print(Triangle(10, 5, 10))
Треугольник со сторонами 10, 5, 10 существует и имеет тип: равнобедренный

>>> print(Triangle(10, 'двенадцать', 5))
Traceback (most recent call last):
...
Triangle.SideTypeError: Значение длины стороны треугольника должно быть только в числовой форме. Ваше значение: двенадцать