import numpy as np
from numpy.testing import *
import unittest
from conformalmapping import *

class TestCircle(unittest.TestCase):

    def test_invalid(self):
        with self.assertRaises(Exception):
            c = Circle(center = 0.0 + 0.0j, radius = -1)

    def test_boundbox(self):
        c = Circle(center = 0.0 + 0.0j, radius = 1.0)
        box = c.boundbox()

        # by inspection three decimal place seems ok
        assert_allclose(box, np.array([-1.0, 1.0, -1.0, 1.0]), 3)

    def test_fromVector(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        self.assertAlmostEqual(c.radius, 1.0)
        self.assertAlmostEqual(c.center, 0.0 + 0.0j)

    def test_circlestr(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        str(c)
        c = Circle.from_vector([1.0, 1.0j, np.inf])
        str(c)

    def test_circlerepr(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        repr(c)
        c = Circle.from_vector([1.0, 1.0j, np.inf])
        repr(c)

    def test_dist(self):
        c = Circle(center = 0.0 + 0.0j, radius = 1.0)
        self.assertAlmostEqual(c.dist(-3.0), 2.0)
        self.assertAlmostEqual(c.dist(-2.0), 1.0)
        self.assertAlmostEqual(c.dist(2.0), 1.0)
        self.assertAlmostEqual(c.dist(3.0), 2.0)
        self.assertAlmostEqual(c.dist(-3.0j), 2.0)
        self.assertAlmostEqual(c.dist(-2.0j), 1.0)
        self.assertAlmostEqual(c.dist(2.0j), 1.0)
        self.assertAlmostEqual(c.dist(3.0j), 2.0)

    def test_isinside(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])

        # clearly inside
        for iv in [0.5, -0.5, 0.5j, -0.5j]:
            self.assertEqual(True, c.isinside(iv))

        # clearly outside
        for ov in [2.0, -2.0, 2.0j, -2.0j]:
            self.assertEqual(False, c.isinside(ov))

    def test_threePointCheck(self):
        c = Circle.from_points(0, 5, 7j)

    def test_zlineCheck(self):
        z1 = Circle.from_points(0, 1, np.inf)
        self.assertEqual(True, np.isinf(z1.radius) )
        self.assertEqual(z1.isinf(), True)
        self.assertEqual(True, z1.isinside(1j))
        self.assertEqual(False, z1.isinside(-1j))


if __name__ == '__main__':
    unittest.begin()

