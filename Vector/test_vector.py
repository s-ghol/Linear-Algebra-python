import math
import unittest
from vector import Vector


class MyTestCase(unittest.TestCase):
    """
    Test cases for Vector class
    """

    # Test Vector Norm and Direction
    def test_v_norm(self):
        v1 = Vector(1, -2, 3)
        self.assertEqual(v1.v_norm(), math.sqrt(14))

        v2 = Vector(math.sin(0), math.cos(0), 4)
        self.assertEqual(v2.v_norm(), math.sqrt(17))

        v3 = Vector(0, 0, 0)
        self.assertEqual(v3.v_norm(), 0)

    def test_v_direction(self):
        v1 = Vector(1, -2, 3)
        self.assertEqual(v1.v_direction(), Vector(1 / math.sqrt(14), -2 / math.sqrt(14), 3 / math.sqrt(14)))

# ----------------------------------------------------------------------------------------------------------------------
    # Orthogonality
    def test_v_dot(self):
        v1 = Vector(1, -2, -3)
        v2 = Vector(1, 1, 2)
        self.assertEqual(v1.v_dot_product(v2), -7)

    def test_v_is_orthogonal(self):
        self.assertTrue(Vector(1, 0, 0).v_is_orthogonality(Vector(0, -1, 0)))


if __name__ == '__main__':
    unittest.main()
