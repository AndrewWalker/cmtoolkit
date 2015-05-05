import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestMobius(unittest.TestCase):
    def test_from_matrix(self):
        Mobius.from_matrix_elements(1,1,1,1)

    def test_call_operator(self):
        # The mobius identify matrix should map points to themselves
        cm = Mobius(M = np.identity(2))
        lst = [ 1., 2., -1., -2., 1.0j, 2.0j, -1.0j, 2.0j ]
        for v in lst:
            self.assertAlmostEqual(v, cm(v))

class TestMobiusCombined(unittest.TestCase):
    def setUp(self):
        z3 = [1, 1j, -1]
        w3 = [-1, -2j, 0]
        self.cm = Mobius.from_vectors(z3, w3)

    def test_mobius_from_vectors(self):
        M = np.array([[-0.6-0.2j, -0.6-0.2j], [0.1+0.7j, 1.1-0.3j]])
        assert_allclose(self.cm.matrix, M)

    def test_mobius_vectorised_call(self):
        self.cm(1.0)
        self.cm(np.array([1.0, 2.0]))

    def test_map_domain(self):
        gc = self.cm.domain.grid()
        self.cm(gc)

    def test_map_range(self):
        r = self.cm.range
        c = self.cm(r.outer)
        self.assertAlmostEqual(c.center, -0.3333 - 0.0j, 4)
        self.assertAlmostEqual(c.radius, 0.33333, 4)
