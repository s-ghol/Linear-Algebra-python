# author: @s.gholami
# -----------------------------------------------------------------------
# m_determinant.p_y
# -----------------------------------------------------------------------
import abc
import math
import pytest


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # get and set
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # Vector Norm and Direction
    def v_norm(self):
        """
        return the norm of the vector
        :return: magnitude of the vector
        :rtype: float
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def v_direction(self):
        """
        return a unit vector
        :return: vector
        :rtype: Vector object
        """
        norm = self.v_norm()
        return Vector(self.x/norm, self.y/norm, self.z/norm)

    def v_scalar_multiplication(self, scalar):
        """

        :param scalar:
        :type scalar:
        :return: Vector
        :rtype: Vector Object
        """
        return Vector(self.x*scalar, self.y*scalar, self.z*scalar)

    # Addition and Subtraction
    def v_addition(self, other):
        """
        add two vectors
        :param other: vector
        :type other: Vector
        :return: vector
        :rtype: Vector
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def v_subtraction(self, other):
        """
        subtract two vectors
        :param other: vector
        :type other: Vector
        :return: vector
        :rtype: Vector
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Dot product and Orthogonality
    def v_dot_product(self, other):
        """
        dot product of two vectors
        :param other: vector
        :type other: Vector
        :return: dot product of two vectors
        :rtype: float
        """
        return self.x*other.x + self.y*other.y + self.z*other.z

    def v_is_orthogonality(self, other):
        """
        check if two vectors are orthogonal
        :param other: vector
        :type other: Vector
        :return: True if orthogonal
        :rtype: bool
        """
        return self.v_dot_product(other) == 0

    # Projection, Rejection and Angle between two vectors
    def v_angle_between(self, other):
        """
        angle between two vectors
        :param other: vector
        :type other: Vector
        :return: angle between two vectors
        :rtype: float
        """
        return math.acos(self.v_dot_product(other)/(self.v_norm()*other.v_norm()))

    def v_projection(self, other):  # let U = self, V = other
        """
        projection of U onto V
        :param other: vector
        :type other: Vector
        :return: projection of one vector on another
        :rtype: Vector
        """
        dot_product = self.v_dot_product(other)
        norm_squared = other.v_norm()**2
        result = (dot_product/norm_squared)  # [(u.v) / (||v||^2)]
        return Vector(result*other.x, result*other.y, result*other.z)  # [(u.v) / (||v||^2)]*v

    def v_rejection(self, other):
        pass

    # to-string
    def __str__(self):
        return '_x_y co-ordinates: ({},{})'.format(str(self.x), str(self.y))








