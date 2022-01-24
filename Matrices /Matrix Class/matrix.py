# author: @s.gholami
# -----------------------------------------------------------------------
# matrix.p_y
# -----------------------------------------------------------------------
import math


class Matrix(object):
    """Matrix class"""

    # Class variables
    PI = math.pi
    ANGLE_IN_RADIAN = PI / 180
    # Reflection matrix
    REFLECTION_MATRIX_x = [[1, 0], [0, -1]]
    REFLECTION_MATRIX_y = [[-1, 0], [0, 1]]

    # maps (x,y,z) to (x,y, 0). Orthogonal projection xy plane
    ORTHOGONAL_PROJECTION = [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0]]
    # Rotation matrix
    D2_MATRIX_ROTATION = [[math.cos(ANGLE_IN_RADIAN), -math.sin(ANGLE_IN_RADIAN)],
                          [math.sin(ANGLE_IN_RADIAN), math.cos(ANGLE_IN_RADIAN)]]
    D3_MATRIX_ROTATION = [[1, 0, 0],
                          [0, math.cos(ANGLE_IN_RADIAN), -math.sin(ANGLE_IN_RADIAN)],
                          [0, math.sin(ANGLE_IN_RADIAN), math.cos(ANGLE_IN_RADIAN)]]

    def __init__(self, *args):
        """
        Matrix constructor
        :param args: list of lists
        :type args: list
        """
        if len(args) == 1 and len(args[0]) == 0:  # if empty matrix
            self.matrix = [0]
            self.rows = 1
            self.cols = 1

        elif len(args) == 1 and len(args[0]) > 0:  # if matrix with one row
            self.matrix = args[0]
            self.rows = len(args)
            self.cols = len(args[0])

        # TODO: check if dim of each column is equal
        elif len(args) > 1 and len(args[0]) > 0:  # if matrix with multiple rows
            self.matrix = args
            self.rows = len(args)
            self.cols = len(args[0])

        else:
            raise ValueError("Matrix must be a list of lists")

    def rref(self, other):
        """
        Reduced row echelon form

        :param other:
        :type other:
        :return:
        :rtype:
        """
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
        if self.rows == other.rows and self.cols == other.cols:  # check if dimensions are equal
            # return Matrix(tuple([i + j for i, j in zip(self.matrix[i], other.matrix[i])] for i in range(self.rows))))
            res = []
            for i in range(self.rows):
                res.append([])
                for j in range(self.cols):
                    res[i].append(self.matrix[i][j] + other.matrix[i][j])
            return __class__(*res)
        else:
            raise ValueError("Matrices must have the same dimensions")

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return str(self.matrix)

    def __getitem__(self, key):
        return self.matrix[key]


# #
# a = Matrix([1, 2, 7], [4, 5, 1])
# # print(a)
# b = Matrix([1, 2, 6], [4, 5, 7])
# # print(b, bb)
# c = a.__add__(b)
# print(c)
# # print(a.matrix)
