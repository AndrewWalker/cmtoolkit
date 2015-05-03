import unittest
from numpy.testing import *
from conformalmapping.cmt import *

class TestCMT(unittest.TestCase):

    def test_boundingbox(self):
        box = boundbox([-1 -1j, 1 +1j])
        assert_allclose(box, np.array([-1.0, 1.0, -1.0, 1.0]))

    def test_boundingbox2(self):
        box = boundbox([-1 -1j, 1 +1j, 2 + 2j])
        assert_allclose(box, np.array([-1.0, 2.0, -1.0, 2.0]))

    def test_plotbox(self):
        box = plotbox([-1 -1j, 1 +1j])
        assert_allclose(box, np.array([-1.2, 1.2, -1.2, 1.2]))

    def test_plotbox_scale(self):
        box = plotbox([-1 -1j, 1 +1j], scale = 2.0)
        assert_allclose(box, np.array([-2.0, 2.0, -2.0, 2.0]))
