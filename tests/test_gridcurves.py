import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestGridCurves(unittest.TestCase):

    def test_str(self):
        gc = GridCurves([])
        self.assertEqual(type(str(gc)), str)

    def test_repr(self):
        gc = GridCurves([])
        self.assertEqual(type(repr(gc)), str)

    def test_no_curves(self):
        gc = GridCurves([])
        self.assertEqual(type(gc.curves), list)
        self.assertEqual(len(gc.curves), 0)

    def test_no_curves(self):
        gc = GridCurves([Circle(center=0, radius=1)])
        self.assertEqual(type(gc.curves), list)
        self.assertEqual(len(gc.curves), 1)

