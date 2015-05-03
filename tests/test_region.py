import unittest
from conformalmapping import *

class TestRegion(unittest.TestCase):

    def setUp(self):
        self.p = Circle(0.0, 1.0)

    def test_onearg_constructors(self):
        r = Region(outer = self.p)

    def test_interior_constructor(self):
        r = Region.interiorto(self.p)

    def test_exterior_constructor(self):
        r = Region.exteriorto(self.p)