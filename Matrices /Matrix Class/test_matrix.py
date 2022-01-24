# author: @s.gholami
# -----------------------------------------------------------------------
# test_matrix.p_y
# -----------------------------------------------------------------------
import unittest
from matrix import Matrix


class MyTestCase(unittest.TestCase):
    """ Test cases for matrix.py """

    def test_add(self):
        """ Test add function """
        self.assertEqual(Matrix([[1, 2], [3, 4]]).__add__(Matrix([[1, 2], [3, 4]])), Matrix([[2, 4], [6, 8]]))

    def test_determinant(self):
        """ Test determinant function """
        self.assertEqual(Matrix([2]).determinant(), 2)
        self.assertEqual(Matrix([1, 2], [3, 4]).determinant(), -2)
        self.assertEqual(Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).determinant(), 0)
        self.assertEqual(Matrix([3, 0, 1], [1, 2, 5], [-1, 4, 2]).determinant(), -42)
