import unittest
from conformalmapping import *
import numpy as np
from numpy.testing import *

class TestSzMap(unittest.TestCase):

    def setUp(self):
        self.G = Splinep.from_complex_list([ 
            0.2398 + 0.6023j, 0.3567 + 1.0819j, 0.2632 + 1.5965j,
            -0.5205 + 1.7485j, -1.0585 + 1.1170j, -1.0702 + 0.5088j,
            -0.5906 + 0.0994j, -0.7778 - 0.4269j, -1.2924 - 0.6140j,
            -1.4561 - 1.2456j, -0.5439 - 1.3509j, 0.2515 - 1.0702j,
            0.3099 - 0.6023j, 0.7427 - 0.5906j, 1.1053 - 0.1813j,
            1.2807 + 0.3567j 
        ])

    def test_init(self):
        m = SzMap(range = self.G)
