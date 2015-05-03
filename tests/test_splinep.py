import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestSplinep(unittest.TestCase):

    # TODO - reconsider implementing this in terms of data loaded
    #        from a MATLAB workspace. It would make doing a wider
    #        range of tests (and regressions) much simpler

    def setUp(self):
        # we'll specifically choose the example points given 
        # in the MATLAB spec-file
        self.pts = [
             0.5896  + 1.2486j,
             -0.1426 + 1.5954j,
             -0.9133 + 1.1561j,
             -0.8465 + 0.3536j,
             -1.1116 - 0.2398j, 
             -1.2695 - 0.9643j,
             -0.5660 - 1.1075j,
              0.2013 - 0.7552j,
              0.8362 - 0.9634j,
              1.5838 - 0.7013j,
              1.3141 + 0.4008j,
              0.8474 + 0.7291j ]
        self.spline = Splinep.from_complex_list(self.pts)

    def test_shape(self):
        self.assertEqual(len(self.spline.zpts), 13)

    def test_translation(self):
        t = self.spline + complex(1, 1)

    def test_chordlength(self): 
        self.assertAlmostEqual(self.spline.chordalArcLength, 9.2018, 4)
        self.assertAlmostEqual(self.spline.arclength(), 9.2018, 4)

    def test_point0(self):
        self.assertAlmostEqual(self.spline.point(0), self.pts[0])

    def test_multi_point0(self):
        ts = [0., 0.]
        ps = [ self.pts[0], self.pts[0] ]
        qs = self.spline.point(ts)
        self.assertAlmostEqual(ps[0], qs[0])
        self.assertAlmostEqual(ps[1], qs[1])

    def test_second0(self):
        out = self.spline.second(0)
        res = -1.0476e+02 -7.9734e+01j
        assert_allclose(out, res, 2)

    def test_tangent0(self):
        out = self.spline.tangent(0)
        res = np.complex(-4.9952, 7.8044)
        assert_allclose(out, res, 3)

    def test_splineParams(self):
        pp = self.spline.ppArray
        self.assertEqual(len(pp.keys()), 6)

