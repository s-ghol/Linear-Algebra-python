# author: @s.gholami
# -----------------------------------------------------------------------
# m_determinant.p_y
# -----------------------------------------------------------------------
import abc
import math
import pytest


class Vector(metaclass=abc.ABCMeta):
    """
    Base class for 2d and 3d and possible nd vectors
    """

    # Get methods
    @abc.abstractmethod
    def get_x(self):
        pass

    @abc.abstractmethod
    def get_y(self):
        pass

    # Set methods
    @abc.abstractmethod
    def set_x(self, _x):
        pass

    @abc.abstractmethod
    def set_y(self, _y):
        pass

    # Magnitude and unit vector (direction) and Scalar multiplication
    @abc.abstractmethod
    def v_magnitude(self):
        """
        Returns the magnitude of a vector
        :return: scalar
        :rt_ype: float
        """

    @abc.abstractmethod
    def v_direction(self):
        """
        Returns the unit vector
        :return: vector
        :rt_ype: tuple
        """

    @abc.abstractmethod
    def v_scalar_mult(self, scalar):
        """
        Scalar multiplication
        :param scalar: scalar
        :return: vector
        :rt_ype: tuple
        """

    # Vector addition and subtraction
    @abc.abstractmethod
    def v_add(self, other):
        """
        Vector addition
        :param other: vector
        :return: vector
        :rt_ype: tuple
        """

    @abc.abstractmethod
    def v_sub(self, other):
        """
        Vector subtraction
        :param other: vector
        :return: vector
        :rt_ype: tuple
        """

    # Vector dot product and orthogonality
    @abc.abstractmethod
    def v_dot(self, other): # other is vector
        """
        Dot product of two vectors
        :param other: vector
        :return: scalar
        :rt_ype: float
        """


    @abc.abstractmethod
    def v_is_orthogonal(self, other):
        """
        Checks if two vectors are orthogonal
        :param other: vector
        :return: boolean
        :rt_ype: bool
        """

    # Projection and Angles
    @abc.abstractmethod
    def v_angle_between(self, other):
        """
        Angle between two vectors
        :param other: vector
        :return: angle
        :rt_ype: float
        """

    @abc.abstractmethod
    def v_orthogonal_projection(self, other):  # self (u) on to  other (v)
        """
        Orthogonal projection of u onto v
        :param other: vector
        :return: vector
        :rt_ype: tuple
        """

    # to-string
    @abc.abstractmethod
    def __str__(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------

class D2Vector(Vector):

    def __init__(self, _x=0, _y=0):
        self._x = _x
        self._y = _y

    # Get
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # Set
    def set_x(self, _x):
        self._x = _x

    def set_y(self, _y):
        self._y = _y

    # Magnitude and Direction for 2d (see doc for theory)
    def v_magnitude(self):
        return math.sqrt((self._x ** 2) + (self._y ** 2))

    def v_direction(self):
        magnitude = self.v_magnitude()
        return self._x / magnitude, self._y / magnitude

    def v_scalar_mult(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return self._x * scalar, self._y * scalar
        else:
            raise TypeError('Scalar must be an int or a float')

    # Vector addition, subtraction
    def v_add(self, other):
        return self._x + other.x, self._y + other.y

    def v_sub(self, other):
        return self._x - other.x, self._y - other.y

    # dot product and orthogonality
    def v_dot(self, other):
        return self._x * other.x + self._y * other.y

    def v_is_orthogonal(self, other):
        return self.v_dot(other) == 0

    # Projection and Angles
    def v_angle_between(self, other):
        return math.acos(self.v_dot(other) / (self.v_magnitude() * other.v_magnitude()))

    def v_orthogonal_projection(self, other): # self (u) on to  other (v)
        temp = (self.v_dot(other) / (other.v_magnitude())**2)  # u.v/||v||^2
        return other.x * temp, other.y * temp
    
    # to-string
    def __str__(self):
        return '_x_y co-ordinates: ({},{})'.format(self._x, self._y)

# ----------------------------------------------------------------------------------------------------------------------

# class D3Vector(Vector):
#
#     def __init__(self, _x, _y, z):
#         Vector.__init__(self, _x, _y)
#         self.z = z
#
#     # Get
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#     def get_z(self):
#         return self._z
#
#     # Set
#     def set_x(self, _x):
#         self._x = _x
#
#     def set_y(self, _y):
#         self._y = _y
#
#     def set_z(self, z):
#         self._z = z
#
#     # Magnitude and Direction for 3d (see doc for theor_y)
#     def v_magnitude(self):
#         return math.sqrt((self._x ** 2) + (self._y ** 2) + (self._z ** 2))
#
#     def v_direction(self):
#         magnitude = self.v_magnitude()
#         return self._x / magnitude, self._y / magnitude, self._z / magnitude
#
#     # to-string
#     def __str__(self):
#         return '_x_yz co-ordinates: ({},{},{})'.format(self._x, self._y, self._z)
