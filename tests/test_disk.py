import unittest
from conformalmapping import *

class TestDisk(unittest.TestCase):

    def test_unitdisk(self):
        d = unitdisk()

    def test_unitdisk(self):
        d = Disk(Circle(center=1.0+1.0j, radius=1.0))

    def test_disk_grid(self):
        d = unitdisk()
        d.grid()
