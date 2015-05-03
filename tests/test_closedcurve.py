import unittest
import numpy as np
from conformalmapping import *

class TestRegion(unittest.TestCase):

    def test_modparam(self):
        c = ClosedCurve()
        out = c.modparam([-0.1, 0.0, 0.5, 0.9, 1.0, 1.1])
        exp = np.array([0.9, 0.0, 0.5, 0.9, 0.0, 0.1])
        np.allclose(out, exp)
