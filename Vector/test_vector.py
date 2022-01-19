# author: @s.gholami
# -----------------------------------------------------------------------
# vector.p_y
# -----------------------------------------------------------------------
import math
import unittest
import vector


class MyTestCase(unittest.TestCase):
    """
    Test cases for Vector class
    """

    # Test Vector Norm and Direction
    def test_norm(self):
        v = vector.Vector(1, 2, 3)
        self.assertEqual(v.v_norm(), math.sqrt(14))

        v2 = vector.Vector(0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(v2.v_norm(), 0)

    def test_v_normalise(self):
        v = vector.Vector(1, 2)
        # self.assertEqual(v.v_normalise(), vector.Vector(1/math.sqrt(5), 2/math.sqrt(5)))
        self.assertIsInstance(v.v_normalise(), vector.Vector)

    def test_v_inner_product(self):
        v = vector.Vector(1, 2, 3)
        self.assertEqual(v.v_inner_product(vector.Vector(4, 5, 6)), 32)
        self.assertRaises(ValueError, v.v_inner_product,
                          vector.Vector(4, 5, 6, 7))  # check if the vector is of the same length

    def test_v_is_orthogonal(self):
        v = vector.Vector(3, 2)
        v2 = vector.Vector(1, 2)
        self.assertEqual(v.v_is_orthogonal(vector.Vector(7, -5)), False)
        self.assertEqual(v2.v_is_orthogonal(vector.Vector(2, -1)), True)
        self.assertEqual(v.v_is_orthogonal(vector.Vector(0, 0)), True)

    def test_v_projection(self):  # ToDo: fix result of projection
        v = vector.Vector(1, 0)
        v2 = vector.Vector(1, 2, 3)
        self.assertEqual(v.v_projection(vector.Vector(2, 1)), vector.Vector(2, 0))
        # self.assertEqual(v2.v_projection(vector.Vector(1, 1, 2)), vector.Vector(9/14, 9/7, 27/14))

    def test__mul__(self):
        v = vector.Vector(1, 2, 3)
        self.assertEqual(v.__mul__(2), vector.Vector(2, 4, 6))
        self.assertEqual(v.__mul__(vector.Vector(2, 2, 2)), 12)

    def test_v_angle(self):
        v = vector.Vector(1, 0)
        v2 = vector.Vector(1, 1)
        self.assertEqual(v.v_angle(v2), math.acos(1/math.sqrt(2)))


if __name__ == '__main__':
    unittest.main()
