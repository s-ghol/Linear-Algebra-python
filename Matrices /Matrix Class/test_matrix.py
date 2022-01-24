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
