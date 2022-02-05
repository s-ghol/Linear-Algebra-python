# author: @s.gholami
# -----------------------------------------------------------------------
# test_matrix.p_y
# -----------------------------------------------------------------------
import unittest
import math
from matrix import Matrix


class MyTestCase(unittest.TestCase):
    """ Test cases for matrix.py """

    def test_matrix_init(self):
        pass

    def test_equality(self):
        """ Test equality function """
        self.assertEqual(Matrix([1, 2], [3, 4]), Matrix([1, 2], [3, 4]))
        self.assertFalse(Matrix([1, 2], [3, 4]) == Matrix([1, 2], [3, 5]))
        self.assertRaises(ValueError, Matrix([1, 2], [3, 4]).__eq__, Matrix([1, 2], [3, 4], [5, 6]))

    def test_dimension(self):
        """ Test dimension function """
        m = Matrix([1, 2, 3], [4, 5, 6])
        self.assertEqual(m.dimension(), (2, 3))

    def test_orthogonal(self):
        """ Test orthogonal function """
        self.assertTrue(Matrix([math.sqrt(3/2), -1/2], [1/2, math.sqrt(3/2)]).is_orthogonal())
        self.assertFalse(Matrix([1, 1], [1, -1]).is_orthogonal())
        self.assertTrue(Matrix([1, 0], [0, 1]).is_orthogonal())
        self.assertRaises(ValueError, Matrix([1, 0], [0, 1], [1, 0]).is_orthogonal)
        self.assertTrue(Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1]).is_orthogonal())
        self.assertFalse(Matrix([1, 2, 2], [2, 1, -2], [-2, 2, -1]).is_orthogonal())
        self.assertTrue(Matrix([1/3, 2/3, 2/3], [2/3, 1/3, -2/3], [-2/3, 2/3, -1/3]).is_orthogonal())

    def test_transpose(self):
        self.assertEqual(Matrix([1, 2, 3], [4, 5, 6]).transpose(), Matrix([1, 4], [2, 5], [3, 6]))

    def test_trace(self):
        """ Test trace function """
        A = Matrix([1, 2, 3], [4, 5, 6])
        B = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertRaises(ValueError, A.trace)
        self.assertEqual(B.trace(), 15)

    def test_add(self):
        """ Test add function """
        self.assertEqual(Matrix([1, 2], [3, 4]).__add__(Matrix([1, 2], [3, 4])), Matrix([2, 4], [6, 8]))

    def test_subtract(self):
        """ Test subtract function """
        self.assertEqual(Matrix([[1, 2], [3, 4]]).__sub__(Matrix([[1, 2], [3, 4]])), Matrix([[0, 0], [0, 0]]))

    def test_multiply(self):
        """ Test multiply function """
        A = Matrix([1, 1, 0], [0, 0, 1])
        B = Matrix([1, 0, 0], [2, 1, 0])

        C = Matrix([1, 0], [0, 1])

        D = Matrix([1, 1, 1],
                   [0, 0, 1])
        E = Matrix([1, 0, 1],
                   [1, 1, 1],
                   [0, 2, 0])

        self.assertEqual(C.__mul__(2), Matrix([2, 0], [0, 2]))
        self.assertEqual(A.__mul__(0), Matrix([0, 0, 0], [0, 0, 0]))
        self.assertEqual(C.__mul__(0), Matrix([0, 0], [0, 0]))
        self.assertEqual(D.__mul__(E), Matrix([2, 3, 2], [0, 2, 0]))

    def test_determinant(self):
        """ Test determinant function """
        self.assertEqual(Matrix([2]).determinant(), 2)
        self.assertEqual(Matrix([1, 2], [3, 4]).determinant(), -2)
        self.assertEqual(Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).determinant(), 0)
        self.assertEqual(Matrix([3, 0, 1], [1, 2, 5], [-1, 4, 2]).determinant(), -42)

    # ---------------------------------------------------------------------------------------------------------------------
    # Clas Method Tests
    def test_identity(self):
        """ Test identity function """
        self.assertEqual(Matrix.identity(2), Matrix([1, 0], [0, 1]))
        self.assertEqual(Matrix.identity(3), Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1]))
        self.assertRaises(ValueError, Matrix.identity, -1)
        self.assertEqual(Matrix.identity(4), Matrix([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]))

    def test_dot(self):
        """ Test dot function """
        u = [1, 2]
        v = [1, 1]
        self.assertEqual(Matrix.dot(u, v), 3)
