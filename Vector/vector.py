# author: @s.gholami
# -----------------------------------------------------------------------
# vector.p_y
# -----------------------------------------------------------------------
import math
import sympy


class Vector(object):
    """
    Vector class
    """
    PI: float = math.pi
    STANDARD_BASIS_2D_VECTORS: tuple = ((1, 0), (0, 1))
    STANDARD_BASIS_3D_VECTORS: tuple = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def __init__(self, *args):
        """
        Initialize the  n vector
        :param args: tuple
        :type args:
        """
        if len(args) == 0:
            self.vector = (0, 0)
        else:
            # return a tuple
            self.vector = args

        # TODO: value of non-void functions should be checked by each calling function

    # Vector Norm and Direction
    def v_norm(self) -> float:
        """
        return the norm of the vector
        :return: norm of the vector
        :rtype: float
        """
        return math.sqrt(sum((v ** 2 for v in self.vector)))

    def v_normalise(self):
        """
        Normalize the vector (unit vector): (1/norm)*(vector)
        :return: normalized vector
        :rtype: Vector Object
        """
        norm = self.v_norm()
        return Vector(tuple(v / norm for v in self.vector))

    def v_inner_product(self, u) -> float:
        """
        return the inner product of the vector (dot product of u and v)
        inner dimension must match
        :param u: vector
        :type u: Vector Object
        :return: inner product
        :rtype: float
        """
        if len(u.vector) != len(self.vector):
            raise ValueError("inner dimension must match")
        else:
            return sum(x * y for x, y in zip(self.vector, u.vector))

    def v_is_orthogonal(self, u) -> bool:
        """
        return True if u is orthogonal to self
        :param u: vector
        :type u: Vector Object
        :return: True if u is orthogonal to self
        :rtype: bool
        """
        return self.v_inner_product(u) == 0

    def v_projection(self, u):  # todo: check for 0 vector.
        """
        return the projection of u on self
        :param u: vector
        :type u: Vector Object
        :return: projection of u on self
        :rtype: Vector Object
        """
        inner = self.v_inner_product(u)  # dot(u,v)
        norm = self.v_norm() ** 2  # dot(v,v)
        inner_over_norm = inner / norm  # u.v/|u|^2
        res = tuple(inner_over_norm * v for v in self.vector)
        # return Vector(tuple(res * v for v in self.vector)) # correct but returns extra (). test fails
        return self.__class__(*res)

    def v_rejection(self, u):
        """
        return the rejection of u from self
        :param u: vector
        :type u: Vector Object
        :return: rejection of u from self
        :rtype: Vector Object
        """
        return self.__class__(self - self.v_projection(u))

    def v_angle(self, u) -> float:
        """
        return the angle between u and v
        :param u: vector
        :type u: Vector Object
        :return: angle between u and v
        :rtype: float
        """
        if len(u.vector) == len(self.vector) and len(u.vector) == 2:
            return math.acos(self.v_inner_product(u) / (self.v_norm() * u.v_norm()))
        else:
            raise ValueError("Only 2d vectors are supported")

    def v_cross_product(self, u):
        """
        return the cross product of u and v
        :param u: vector
        :type u: Vector Object
        :return: cross product of u and v
        :rtype: Vector Object
        """
        if len(u.vector) != len(self.vector):
            raise ValueError("inner dimension must match")
        # for 2d, return the determinant
        elif len(u.vector) == 2:
            ux, uy = u.vector
            vx, vy = self.vector
            return Vector(*(0, 0, uy * vx - ux * vy))
        elif len(u.vector) == 3:
            ux, uy, uz = u.vector
            vx, vy, vz = self.vector
            return Vector(*(uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx))

    def v_gram_schmidt(self):
        """
        Gram-Schmidt process: Let S = {s_1, s_2, ..., s_n} be a linearly independent set of vectors. Then,
        Gram-Schmidt process is a process of orthonormalizing the set of vectors in S.
        :return: orthogonal set of vectors
        :rtype: Vector Object
        """
        pass

    # Overloading operators for vector
    def __eq__(self, other):
        """
        Overloading == operator
        :param other: vector
        :type other: Vector Object
        :return: True if vector are equal
        :rtype: bool
        """
        if isinstance(other, Vector):
            return self.vector == other.vector
        else:
            raise TypeError("unsupported operand type for ==: 'Vector' and '{}'".format(type(other)))

    def __mul__(self, other):
        """
        Overloading * operator
        :param other: vector or scalar value
        :type other: float or Vector Object
        :return: scalar product or vector product
        :rtype: float or Vector Object
        """
        if isinstance(other, Vector):  # if other is a vector
            return self.v_inner_product(other)
        elif isinstance(other, (int, float)):  # if other is a scalar
            res = tuple(other * v for v in self.vector)
            return self.__class__(*res)
            # return Vector(tuple(other * v for v in self.vector)) # correct but returns extra (). test fails
        else:
            raise TypeError("unsupported operand for multiplication: 'Vector' and '{}'".format(type(other)))

    def __add__(self, other):
        """
        Overloading + operator
        :param other: vector
        :type other: Vector Object
        :return: vector sum
        :rtype: Vector Object
        """
        if isinstance(other, Vector):
            if len(other.vector) != len(self.vector):
                raise ValueError("inner dimension must match")
            else:
                res = tuple(x + y for x, y in zip(self.vector, other.vector))
                return self.__class__(*res)
        else:
            raise TypeError("unsupported operand for addition: 'Vector' and '{}'".format(type(other)))

    def __sub__(self, other):
        """
        Overloading - operator
        :param other: vector
        :type other: Vector Object
        :return: vector difference
        :rtype: Vector Object
        """
        if isinstance(other, Vector):
            if len(other.vector) != len(self.vector):
                raise ValueError("inner dimension must match")
            else:
                res = tuple(x - y for x, y in zip(self.vector, other.vector))
                return self.__class__(*res)
        else:
            raise TypeError("unsupported operand for subtraction: 'Vector' and '{}'".format(type(other)))

    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return self.vector[item]

    def __len__(self):
        return len(self.vector)

    def __iter__(self):
        return iter(self.vector)


if __name__ == "__main__":
    pass
