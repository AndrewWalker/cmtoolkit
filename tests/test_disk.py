import unittest
import numpy as np
from numpy.testing import *
from conformalmapping import *

class TestDisk(unittest.TestCase):

    def test_unitdisk(self):
        d = unitdisk()

    def test_disk_boundbox(self):
        d = unitdisk()
        box = d.boundbox()

        # by inspection three decimal place seems ok
        assert_allclose(box, np.array([-1.0, 1.0, -1.0, 1.0]), 3)

    def test_unitdisk(self):
        d = Disk(Circle(center=1.0+1.0j, radius=1.0))

    def test_disk_grid(self):
        d = unitdisk()
        d.grid()
