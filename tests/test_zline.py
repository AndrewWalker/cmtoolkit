import numpy as np
from numpy.testing import *
import unittest
from conformalmapping import *

class TestZline(unittest.TestCase):

    def test_create(self):
        line = Zline(np.array([0.0, 1.0j]))

    def test_position(self):
        line = Zline(np.array([0.0, 1.0j]))
        pt = line.position(0)
        assert_allclose(pt, 0.0 )

    def test_tangent(self):
        line = Zline(np.array([0.0, 1.0j]))
        t = line.tangent(0)
        assert_allclose(t, 1.0j)
