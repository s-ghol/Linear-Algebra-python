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

    def determinant(self) -> float:
        """
        Determinant of the matrix
        :return: determinant
        :rtype: int
        """
        if self.rows == self.cols:  # check if matrix is square
            if self.rows == 1:  # if matrix is 1x1
                return self.matrix[0][0]
            elif self.rows == 2:  # if matrix is 2x2
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            elif self.rows == 3:  # if matrix is 3x3
                #  {det}(A)=a*e*i- a*f*h - b*d*i + b*f*g + c*d*h - c*e*g (check README for details)
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
    def rotate_2d_x(self, angle: float) -> Vector:
        """
        Rotate 2d matrix around x axis
        :param angle: angle in degree
        :type angle: float
        :return: rotated matrix
        :rtype: Matrix
        """
        # requires a vector
        angle = angle * self.ANGLE_IN_RADIAN  # convert to radian
        D2_MATRIX_ROTATION = [[math.cos(angle), -math.sin(angle)],
                              [math.sin(angle), math.cos(angle)]]
        if self.rows >= 1 and self.cols == 1:  # if vector size
            return Matrix(self.matrix).__mul__(D2_MATRIX_ROTATION)
        else:
            raise TypeError("Matrix must be a vector")

    def lu_decomposition(self):
        pass

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

    def __mul__(self, other):
        pass


