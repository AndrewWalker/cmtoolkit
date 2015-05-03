import matplotlib.pyplot as plt
import numpy as np
from .import cmt 

class ClosedCurve(object):

    def __init__(self, *args, **kwargs):
        super(ClosedCurve, self).__init__(*args, **kwargs)
        self.paramLength = 1.0

    def length(self):
        return self.paramLength

    def modparam(self, t):
        return np.mod(t, self.paramLength)

    def boundbox(self):
        # Return bounding box for curve using evenly spaced points

        # minor errors in the size of the bounding box here should be considered
        # acceptible - the bounding box is used to identify plotboxes

        ts = np.linspace(0.0, self.paramLength, 200)
        ps = self.point(ts)
        return cmt.boundbox(ps)

    def __str__(self):
        return 'closedcurve'

    def plot(self):
        ts = np.linspace(0.0, 1.0, 200)
        zs = self.point(ts)
        plt.plot(zs.real, zs.imag, 'k-')

    def point(self, t):
        """Parametric evaluation of the closed curve 
        """
        raise NotImplementedError('ClosedCurve.point is abstract, and has not been overridden')
