import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestHomog(unittest.TestCase):

    def test_homog(self):
        h = Homog(-1.2-0.4j, 1.2+0.4j)
        h = h.__complex__()
        self.assertAlmostEqual(h, -1.0)
