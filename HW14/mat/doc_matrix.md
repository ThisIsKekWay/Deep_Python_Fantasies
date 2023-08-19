Docfile for matrix validation module
===

Description of the Matrix function.validate(matrix)
---

To validate a user-created matrix, use the validate method in the Matrix class.

During the creation of an instance of the Matrix class with a
matrix passed in manual mode, the init dunder will 
call the method itself and if the matrix is passed in the wrong form, 
it will not create an object of the class, and will also raise an exception.

>>> from MatClass import Matrix, MatrixElementsError

>>> Matrix.validate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


>>> Matrix.validate([[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]])
Traceback (most recent call last):
...
MatClass.MatrixElementsError: martix rows are not equal.
your matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]