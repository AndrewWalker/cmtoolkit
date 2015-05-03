import numpy as np
from numpy.testing import *
import unittest
from conformalmapping import *

class TestCircle(unittest.TestCase):

    def test_invalid(self):
        with self.assertRaises(Exception):
            c = Circle(center = 0.0 + 0.0j, radius = -1)

    def test_fromVector(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        self.assertAlmostEquals(c.radius, 1.0)
        self.assertAlmostEquals(c.center, 0.0 + 0.0j)

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
        self.assertAlmostEquals(c.dist(-3.0), 2.0)
        self.assertAlmostEquals(c.dist(-2.0), 1.0)
        self.assertAlmostEquals(c.dist(2.0), 1.0)
        self.assertAlmostEquals(c.dist(3.0), 2.0)
        self.assertAlmostEquals(c.dist(-3.0j), 2.0)
        self.assertAlmostEquals(c.dist(-2.0j), 1.0)
        self.assertAlmostEquals(c.dist(2.0j), 1.0)
        self.assertAlmostEquals(c.dist(3.0j), 2.0)

    def test_inside_circle(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        self.assertAlmostEquals(True, c.isinside(0.5))
        self.assertAlmostEquals(True, c.isinside(-0.5))
        self.assertAlmostEquals(True, c.isinside(0.5j))
        self.assertAlmostEquals(True, c.isinside(-0.5j))

    def test_outside_circle(self):
        c = Circle.from_vector([1.0, 1.0j, -1.0])
        self.assertAlmostEquals(False, c.isinside(2))
        self.assertAlmostEquals(False, c.isinside(-2))
        self.assertAlmostEquals(False, c.isinside(2j))
        self.assertAlmostEquals(False, c.isinside(-2j))

    def test_threePointCheck(self):
        c = Circle.from_points(0, 5, 7j)

    def test_zlineCheck(self):
        z1 = Circle.from_points(0, 1, np.inf)
        self.assertEquals(True, np.isinf(z1.radius) )
        self.assertEquals(z1.isinf(), True)
        self.assertEquals(True, z1.isinside(1j))
        self.assertEquals(False, z1.isinside(-1j))

