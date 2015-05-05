import unittest
import collections
from conformalmapping import *
import numpy as np
from numpy.testing import *

class TestSzegoKernel(unittest.TestCase):

    def setUp(self):
        self.G = Splinep.from_complex_list([ 
            0.2398 + 0.6023j, 0.3567 + 1.0819j, 0.2632 + 1.5965j,
            -0.5205 + 1.7485j, -1.0585 + 1.1170j, -1.0702 + 0.5088j,
            -0.5906 + 0.0994j, -0.7778 - 0.4269j, -1.2924 - 0.6140j,
            -1.4561 - 1.2456j, -0.5439 - 1.3509j, 0.2515 - 1.0702j,
            0.3099 - 0.6023j, 0.7427 - 0.5906j, 1.1053 - 0.1813j,
            1.2807 + 0.3567j 
        ])

    def test_invalid_curve(self):
        G = None
        with self.assertRaises(Exception):
            kernel = Szego(G, 0)

    def test_has_methods(self):
        names = [
            'kerz_stein',
            'phi',
            'psi',
            'theta',
            'invtheta',
            'thetap'
        ]
        szego = Szego(self.G, 0.0)
        for name in names:
            self.assert_(name in dir(szego))

    def test_conformal_center(self):
        szego = Szego(self.G, 1.0)
        self.assertAlmostEqual(szego.confCenter, 1.0)

        szego = Szego(self.G, 1.0j)
        self.assertAlmostEqual(szego.confCenter, 1.0j)

    def test_has_str(self):
        self.assert_(str(Szego(self.G, 0.0)).startswith('Szego'))

    def test_psi(self):
        szego = Szego(self.G, 0.0)
        out = szego.psi(0.0)
        self.assert_(type(out), np.ndarray)
        self.assert_(out.shape, (1,))

    def test_psi_vectorized(self):
        szego = Szego(self.G, 0.0)
        out = szego.psi([0.0])
        self.assert_(type(out), np.ndarray)
        self.assert_(out.shape, (1,))

    def test_phi(self):
        szego = Szego(self.G, 0.0)
        out = szego.phi([0.0])
        assert_allclose(0.7549 + 0.4148j, out, 2)

    def test_kerz_stein(self):
        szego = Szego(self.G, 0.0)

        # the zero here represents the value that is
        # required for calculating phi
        out = szego.kerz_stein([0.0])

        idx = [ 0, 1, 3, 7, 15, 31, 63, 127 ]
        expected = np.array([
           0.0000 + 0.0000j, 
          -0.2240 - 0.0141j, 
          -0.7638 - 0.1288j, 
          -1.5829 - 0.4801j, 
          -1.9103 - 0.7444j, 
          -1.6548 - 0.3500j, 
          -1.3082 + 0.5812j, 
          -0.3146 + 0.7873j, 
        ])
        assert_allclose(out[0, idx], expected, 2)


class TestSzegoKernelCreation(unittest.TestCase):
    def setUp(self):
        self.G = Splinep.from_complex_list([ 
            0.2398 + 0.6023j, 0.3567 + 1.0819j, 0.2632 + 1.5965j,
            -0.5205 + 1.7485j, -1.0585 + 1.1170j, -1.0702 + 0.5088j,
            -0.5906 + 0.0994j, -0.7778 - 0.4269j, -1.2924 - 0.6140j,
            -1.4561 - 1.2456j, -0.5439 - 1.3509j, 0.2515 - 1.0702j,
            0.3099 - 0.6023j, 0.7427 - 0.5906j, 1.1053 - 0.1813j,
            1.2807 + 0.3567j 
        ])

        self.opts = SzegoOpts()

    def test_create(self):
        kernel = SzegoKernel(self.G, 0, self.opts)

        # The correctness of these is implied by the spline tests
        self.assert_(type(kernel.zPts), np.ndarray)
        self.assert_(kernel.zPts.shape, (self.opts.numCollPts,))
        self.assert_(type(kernel.zTan), np.ndarray)
        self.assert_(kernel.zTan.shape, (self.opts.numCollPts,))

        # The correctness of these is implied by the specific example below
        self.assert_(type(kernel.zUnitTan), np.ndarray)
        self.assert_(kernel.zUnitTan.shape, (self.opts.numCollPts,))

    def test_specific_example(self):
        kernel = SzegoKernel(self.G, 0, self.opts)

        # values pasted from matlab
        phiIdx = [ 0, 1, 3, 7, 15, 31, 63, 127 ]
        expected = [
           0.7549 + 0.4148j, 
           0.6909 + 0.4597j, 
           0.5686 + 0.5083j, 
           0.3845 + 0.5004j, 
           0.2061 + 0.3666j, 
           0.1226 + 0.1674j, 
           0.1460 + 0.0511j, 
           0.2239 - 0.0874j, 
        ]
        expected = np.array(expected)
        assert_allclose(kernel.phiColl[phiIdx] , expected, 3)



