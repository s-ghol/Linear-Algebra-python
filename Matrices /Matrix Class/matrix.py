# author: @s.gholami
# -----------------------------------------------------------------------
# matrix.p_y
# -----------------------------------------------------------------------
import math
from typing import Tuple


class Matrix(object):
    """Matrix class"""

    # Class variables
    PI: float = math.pi
    ANGLE_IN_RADIAN: float = PI / 180
    # Reflection matrix
    REFLECTION_MATRIX_x = [[1, 0], [0, -1]]
    REFLECTION_MATRIX_y = [[-1, 0], [0, 1]]

    # maps (x,y,z) to (x,y, 0). Orthogonal projection xy plane
    ORTHOGONAL_PROJECTION = [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0]]
    # Rotation matrix (TRANSFORM_MATRIX)

    D3_MATRIX_ROTATION_x = [[1, 0, 0],
                            [0, math.cos(ANGLE_IN_RADIAN), -math.sin(ANGLE_IN_RADIAN)],
                            [0, math.sin(ANGLE_IN_RADIAN), math.cos(ANGLE_IN_RADIAN)]]
    D3_MATRIX_ROTATION_y = [[math.cos(ANGLE_IN_RADIAN), 0, math.sin(ANGLE_IN_RADIAN)],
                            [0, 1, 0],
                            [-math.sin(ANGLE_IN_RADIAN), 0, math.cos(ANGLE_IN_RADIAN)]]
    D3_MATRIX_ROTATION_z = [[math.cos(ANGLE_IN_RADIAN), -math.sin(ANGLE_IN_RADIAN), 0],
                            [math.sin(ANGLE_IN_RADIAN), math.cos(ANGLE_IN_RADIAN), 0],
                            [0, 0, 1]]

    def __init__(self, *args):
        """
        Matrix constructor
        :param args: list of lists
        :type args: list
        """
        # todo: test the constructor
        if len(args) == 1:  # if only one list is passed
            self.matrix = args
            self.rows = 1
            self.cols = 1

        elif len(args) == 1 and len(args[0]) > 0:  # if matrix with one row
            self.matrix = args
            self.rows = len(args)
            self.cols = len(args[0])

        # TODO: check if dim of each column is equal
        elif len(args) > 1 and len(args[0]) > 0:  # if matrix with multiple rows
            self.matrix = args
            self.rows = len(args)
            self.cols = len(args[0])

        else:
            raise ValueError("Matrix must be a list of lists")

    def dimension(self)->Tuple[int, int]:
        """
        Dimension of the matrix
        :return: dimension
        :rtype: int
        """
        return self.rows, self.cols

    def rref(self, other)->'Matrix':
        """
        Reduced row echelon form

        :param other:
        :type other:
        :return:
        :rtype:
        """
        pass

    def rank(self) -> int:
        """
        Rank of the matrix; requires rref method to identify linearly independent rows
        :return: rank
        :rtype: int
        """
        pass

    def inverse(self) -> 'Matrix':
        """
        Inverse of the matrix; calls the rrref method
        :return: inverse matrix
        :rtype: Matrix
        """
        pass

    def transpose(self) -> 'Matrix':
        """
        Transpose of the matrix
        :return: Transposed matrix
        :rtype: Matrix
        """
        t: 'transpose matrix' = [list(a) for a in zip(*self.matrix)]
        return __class__(*t)

    def trace(self):
        """
        Trace of the matrix
        :return: trace
        :rtype: float
        """
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
        else:

            trace = sum(self.matrix[i][i] for i in range(self.rows))
        return trace

    def determinant(self) -> float:
        """
        Determinant of the matrix
        :return: determinant
        :rtype: float
        """
        # todo: generalise the function for n using the determinant formula
        if self.rows == self.cols:  # check if matrix is square
            if self.rows == 1:  # if matrix is 1x1
                return self.matrix[0][0]
            elif self.rows == 2:  # if matrix is 2x2
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            elif self.rows == 3:  # if matrix is 3x3
                #  det(A) = a*e*i- a*f*h - b*d*i + b*f*g + c*d*h - c*e*g (check README for details)
                diagonal = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]
                afh = self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
                bdi = self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]
                bfg = self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]
                cdh = self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]
                ceg = self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
                res = diagonal - afh - bdi + bfg + cdh - ceg
                return res
            elif self.rows == 4:
                pass

    # Linear Transformation; Rotation
    def rotate_2d_x(self, angle: float):
        """
        Rotate 2d matrix around x axis
        :param angle: angle in degree
        :type angle: float
        :return: rotated matrix
        :rtype: Matrix
        """
        angle: float = angle * self.ANGLE_IN_RADIAN  # convert to radian
        d2_matrix_rotation = ([math.cos(angle), -math.sin(angle)],
                              [math.sin(angle), math.cos(angle)])
        if self.rows >= 1 and self.cols == 1:  # if vector size equal
            return __class__(self.matrix).__mul__(d2_matrix_rotation)
        else:
            raise TypeError("Matrix must be a vector")

    def is_orthogonal(self) -> bool:
        """
        If A is a square matrix then : A is orthogonal iff A^TA = I
        :return: True if orthogonal, False otherwise
        :rtype: bool
        """
        if self.rows == self.cols:
            return self.__mul__(self.transpose()) == Matrix.identity(self.rows)
        else:
            raise ValueError('{} is not a square matrix'.format(self.matrix))

    def is_equivalent(self, other):  # if self (A) equivalent to other (B)
        # Two matrices are equivalent iff they have the same reduced row- echelon form.
        # todo: check if A and B are the same size
        # todo: call rref or A and B then check if A and B are the same. if not return False
        """
        Check if two matrix are equivalent
        :param other: other matrix
        :type other: Matrix
        :return: True if equivalent, False otherwise
        :rtype: Boolean
        """
        pass

    def lu_decomposition(self):
        pass

    # Overloading operators
    def __add__(self, other):
        """
        Addition operator
        :param other: Matrix
        :type other: Matrix
        :return: Matrix
        :rtype: Matrix
        """
        # todo: test fails even though expected = actual
        dim_self = self.dimension()
        dim_other = other.dimension()
        res = []
        if dim_self == dim_other:
            for (i, j) in zip(self, other):
                res.append(list(map(lambda x, y: x + y, i, j)))
            return __class__(*res)
        else:
            raise ValueError("Matrix must be the same size")

    def __sub__(self, other):
        """
        Subtraction operator
        :param other: Matrix
        :type other: Matrix
        :return: Matrix
        :rtype: Matrix
        """
        dim_self = self.dimension()
        dim_other = other.dimension()
        res = []
        if dim_self == dim_other:
            for (i, j) in zip(self, other):
                res.append(list(map(lambda x, y: x - y, i, j)))
            return __class__(*res)
        else:
            raise ValueError("Matrix must be the same size")

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return str(self.matrix)

    def __getitem__(self, key):
        return self.matrix[key]

    def __eq__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return self.matrix == other.matrix
        else:
            raise ValueError("Matrix must be the same size")

    def __mul__(self, other):
        """
        Multiplication operator
        :param other: Matrix or scalar
        :type other: Matrix or (int,float)
        :return: Matrix
        :rtype: Matrix
        """
        if isinstance(other, (int, float)):
            return __class__(*((list(other * x for x in row) for row in self.matrix)))
        elif isinstance(other, Matrix) and self.cols == other.rows:
            return self.__class__(*list(list(
                Matrix.dot(row, col) for col in zip(*other.matrix))for row in self.matrix))
        else:
            raise ValueError("Matrix must be the same size")

    # Class methods
    @classmethod  # object reference not needed to call this method. only class
    def identity(cls, rows):
        """
        Generates nxn identity matrix
        :return: nxn identity matrix
        :rtype: Matrix
        """
        if isinstance(rows, int) and rows == 0:
            return __class__(cls([0]))
        elif isinstance(rows, int) and rows > 0:
            m = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
            return __class__(*m)
        else:
            raise ValueError("Matrix must be a square matrix")

    @classmethod
    def dot(cls, u, v):
        if len(u) == len(v):
            return sum([i * j for i, j in zip(u, v)])
        else:
            raise ValueError("Vector must be the same size")
