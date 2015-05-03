import unittest
import numpy 
from conformalmapping import *

class TestSplinep(unittest.TestCase):

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

    def test_shape(self):
        s = Splinep.from_complex_list(self.pts)
        self.assertEquals(len(s.zpts), 13)

    def test_translation(self):
        s = Splinep.from_complex_list([0, 1, 1j])
        t = s + complex(1, 1)

    def test_chordlength(self): 
        s = Splinep.from_complex_list(self.pts)
        self.assertAlmostEquals(s.chordalArcLength, 9.2018, 4)
        self.assertAlmostEquals(s.arclength(), 9.2018, 4)

    def test_point0(self):
        s = Splinep.from_complex_list(self.pts)
        self.assertAlmostEquals(s.point(0), self.pts[0])

    def test_multi_point0(self):
        s = Splinep.from_complex_list(self.pts)
        ts = [0., 0.]
        ps = [ self.pts[0], self.pts[0] ]
        qs = s.point(ts)
        self.assertAlmostEquals(ps[0], qs[0])
        self.assertAlmostEquals(ps[1], qs[1])

    def test_second0(self):
        s = Splinep.from_complex_list(self.pts)
        out = s.second(0)
        res = numpy.complex(-1.0476e+02, - 7.9734e+01)

        self.assertAlmostEquals(out.imag, res.imag, 2)
        self.assertAlmostEquals(out.real, res.real, 2)

    def test_tangent0(self):
        s = Splinep.from_complex_list(self.pts)
        out = s.tangent(0)
        res = numpy.complex(-4.9952, 7.8044)

        self.assertAlmostEquals(out.imag, res.imag, 2)
        self.assertAlmostEquals(out.real, res.real, 2)


    def test_splineParams(self):
        s = Splinep.from_complex_list(self.pts)
        pp = s.ppArray
        self.assertEquals(len(pp.keys()), 6)

