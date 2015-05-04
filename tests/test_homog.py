import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestHomog(unittest.TestCase):

    def test_homog(self):
        h = Homog(-1.2-0.4j, 1.2+0.4j)
        h = h.__complex__()
        self.assertAlmostEqual(h, -1.0)

    def test_str(self):
        h = Homog(1.0j, 1.0)
        self.assertEqual(type(str(h)), str)

    def test_repr(self):
        h = Homog(1.0j, 1.0)
        self.assertEqual(type(repr(h)), str)


