# author: @s.gholami
# -----------------------------------------------------------------------
# m_determinant.p_y
# -----------------------------------------------------------------------
import math


class Vector:
    """
    Vector class
    """

    def __init__(self, x, y, z):
        """
        Initialize the vector
        :param x:
        :type x:
        :param y:
        :type y:
        :param z:
        :type z:
        """
        if isinstance((x, y, z), (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError('x must be an integer or float')

        # TODO: add check for strings
        # ToDo: implement n dimensions vector

    # ------------------------------------------------------------------------------------------------------------------
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
    def v_norm(self) -> float:
        """
        return the norm of the vector
        :return: norm of the vector
        :rtype: float
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def v_normalize(self):
        """
        return a unit vector (normalized vector;provides direction)
        :return: vector
        :rtype: Vector object
        """
        norm = self.v_norm()
        return Vector(self.x / norm, self.y / norm, self.z / norm)

    def v_scalar_multiplication(self, scalar):
        """

        :param scalar:
        :return: Vector
        :rtype: Vector Object
        """
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # ----------------------------------------------------------------------------------------------------------------------
    # Overloading
    def __add__(self, other):
        """
        Overloading + operator
        :param other:
        :type other:
        :return:
        :rtype:
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # Overloading - operator
    def __sub__(self, other):
        """
        Overloading - operator
        :param other:
        :type other:
        :return:
        :rtype:
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Overloading * operator
    def __mul__(self, scalar):
        """
        Overloading * operator  (scalar multiplication)
        :param scalar:
        :type scalar:
        :return:
        :rtype: Vector
        """
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # Overloading / operator
    def __truediv__(self, scalar):
        """
        Overloading / operator (scalar division)
        :param scalar:
        :type scalar:
        :return:
        :rtype: Vector
        """
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    # Overloading == operator
    def __eq__(self, other):
        """
        Overloading == operator
        :param other:
        :type other:
        :return:
        :rtype: bool
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    # Overloading != operator
    def __ne__(self, other):
        """
        Overloading != operator
        :param other:
        :type other:
        :return:
        :rtype:
        """
        return self.x != other.x or self.y != other.y or self.z != other.z

    # Overloading to-string
    def __str__(self):
        return 'Coordinates: ({},{},{})'.format(str(self.x), str(self.y), str(self.z))

    # ----------------------------------------------------------------------------------------------------------------------
    # Dot product and Orthogonality
    def v_dot_product(self, other):
        """
        dot product of two vectors
        :param other: vector
        :type other: Vector Object
        :return: dot product of two vectors
        :rtype: float
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

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
        return math.acos(self.v_dot_product(other) / (self.v_norm() * other.v_norm()))

    def v_projection(self, other):  # let U = self, V = other
        """
        projection of U onto V
        :param other: vector
        :type other: Vector
        :return: projection of one vector on another
        :rtype: Vector
        """
        dot_uv = self.v_dot_product(other)
        dot_v = other.v_dot_product(other)
        result = (dot_uv / dot_v)  # [(u.v) / v.v]
        return Vector(other.v_scalar_multiplication(result))  # [(u.v) / v.v]*v

    def v_rejection(self, other):
        pass


if __name__ == "__main__":
    pass
