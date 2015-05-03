import matplotlib.pyplot as plt
import numpy as np

class ClosedCurve(object):

    def __init__(self, *args, **kwargs):
        super(ClosedCurve, self).__init__(*args, **kwargs)
        self.paramLength = 1.0

    def length(self):
        return self.paramLength

    def modparam(self, t):
        return np.mod(t, self.paramLength)

    def boundbox(self):
        ts = np.linspace(0.0, self.paramLength, 200)
        ps = self.point(ts)

    def corners(self):
        raise NotImplementedError('closedcurve.corners')

    def ctranspose(self):
        # It may be possible to break this out as a free function instead
        raise NotImplementedError('closedcurve.ctranspose')

    def __str__(self):
        return 'closedcurve'

    def plot(self):
        ts = np.linspace(0.0, 1.0, 200)
        zs = self.point(ts)
        plt.plot(zs.real, zs.imag, 'k-')

    def point(self, t):
        """Parametric evaluation of the closed curve 
        """
        raise NotImplementedError('Point is Abstract')
