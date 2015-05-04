import unittest
from conformalmapping import *

class TestRegion(unittest.TestCase):

    def setUp(self):
        self.p = Circle(0.0, 1.0)

    def test_empty_constructors(self):
        r = Region()

    def test_onearg_constructors(self):
        r = Region(outer = self.p)

    def test_list_constructors(self):
        r = Region(outer = [self.p, self.p])

    def test_bad_constructor(self):
        with self.assertRaises(Exception):
            r = Region(outer = [42])

    def test_interior_constructor(self):
        r = Region.interiorto(self.p)

    def test_exterior_constructor(self):
        r = Region.exteriorto(self.p)
