import unittest
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
            self.assertTrue(name in dir(szego))

    def test_conformal_center(self):
        szego = Szego(self.G, 1.0)
        self.assertAlmostEqual(szego.confCenter, 1.0)

        szego = Szego(self.G, 1.0j)
        self.assertAlmostEqual(szego.confCenter, 1.0j)

    def test_has_str(self):
        self.assertTrue(str(Szego(self.G, 0.0)).startswith('Szego'))

    def test_psi(self):
        szego = Szego(self.G, 0.0)
        out = szego.psi(0.0)
        self.assertTrue(type(out), np.ndarray)
        self.assertTrue(out.shape, (1,))

    def test_psi_vectorized_one(self):
        szego = Szego(self.G, 0.0)
        out = szego.psi([0.0])
        self.assertTrue(type(out), np.ndarray)
        self.assertTrue(out.shape, (1,))

    def test_psi_vectorized_many(self):
        szego = Szego(self.G, 0.0)
        out = szego.psi([0.0, 0.1])
        self.assertTrue(type(out), np.ndarray)
        self.assertTrue(out.shape, (2,))

    def test_phi(self):
        szego = Szego(self.G, 0.0)
        out = szego.phi([0.0])
        self.assertEqual(out.shape, (1,))
        assert_allclose(0.7549 + 0.4148j, out, 2)

    def test_phi_vectorised_one(self):
        szego = Szego(self.G, 0.0)
        out = szego.phi([0.0])
        self.assertEqual(out.shape, (1,))
        assert_allclose(0.7549 + 0.4148j, out, 2)

    def test_phi_vectorised_many(self):
        szego = Szego(self.G, 0.0)
        out = szego.phi([0.0, 0.1])
        self.assertEqual(out.shape, (2,))
        self.assertAlmostEqual(0.7549 + 0.4148j, out[0], 2)
        self.assertAlmostEqual(0.1227 + 0.0749j, out[1], 2)

    def test_theta0(self):
        szego = Szego(self.G, 0.0)
        assert_allclose(szego.theta0, 1.3943, 3)

    def test_saa(self):
        szego = Szego(self.G, 0.0)
        self.assertAlmostEqual(szego.Saa, 0.2032, 3)

    def test_theta(self):
        szego = Szego(self.G, 0.0)
        th = szego.theta([0.0, 0.1, 0.2, 0.4, 0.8])
        expected = np.array([
                 0,
            0.4895,
            0.5690,
           -3.8710,
           -1.7684,
        ])
        self.assertEqual(th.shape, (5, ))
        assert_allclose(th, expected, 3)

    def test_thetap(self):
        szego = Szego(self.G, 0.0)
        ts = np.arange(20) / 20.
        ts = ts
        thp = szego.thetap(ts)
        
        self.assertEqual(thp.shape, ts.shape)
        self.assertAlmostEqual(thp[0], 22.9364, 3)
        self.assertAlmostEqual(thp[1], 1.9622, 3)
        self.assertAlmostEqual(thp[4], 0.9287, 3)

    def test_invtheta(self):
        szego = Szego(self.G, 0.0)
        ts = 2 * np.pi * np.arange(20) / 20.
        out = szego.invtheta(ts)
        self.assertAlmostEqual(out[0], 0.0)
        self.assertAlmostEqual(out[1], 0.0212, 3)
        self.assertAlmostEqual(out[2], 0.2460, 3)

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
        self.assertTrue(type(kernel.zPts), np.ndarray)
        self.assertTrue(kernel.zPts.shape, (self.opts.numCollPts,))
        self.assertTrue(type(kernel.zTan), np.ndarray)
        self.assertTrue(kernel.zTan.shape, (self.opts.numCollPts,))

        # The correctness of these is implied by the specific example below
        self.assertTrue(type(kernel.zUnitTan), np.ndarray)
        self.assertTrue(kernel.zUnitTan.shape, (self.opts.numCollPts,))

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



