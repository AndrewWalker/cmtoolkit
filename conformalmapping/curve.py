import numpy as np
from .cmt import boundbox

class Curve(object):
    """Base class for simple planar Jordan curves
    """

    def __init__(self, positionfun = None, tangentfunc = None, bounds = None ):
        """Create a curve

        Parameters
        ----------
        positionfun : function
            a function from a real value (parameter) to a position (complex)

        tangentfun : function
            a function from a real value (parameter) to a tangent (complex)

        bounds : tuple
            a two element tuple that define the extents of the parameter

        Examples
        --------

        A simple piecewise line element

        >>> c = Curve(positionfun = lambda t: t + 1j, 
        ...           tangentfun = lambda t: 1.0
        ...           bounds = (0, 1))
        """
        self._positionfun = positionfun
        self._tangentfun = tangentfun
        self._bounds = bounds

    def boundbox(self):
        """Create a bounding box the encloses this curve

        Returns
        -------
        out : array-like
            [xmin, xmax, ymin, ymax]
        """
        tmin, tmax = self._bounds
        ts = np.linspace(tmin, tmax, 300)
        ps = self.point(ts)
        out = cmt.boundbox(ps)
        return out

    def plotbox(self, scale = 1.2):
        """Create a plot bounding box the encloses this curve

        Returns
        -------
        out : array-like
            [xmin, xmax, ymin, ymax]
        """
        tmin, tmax = self._bounds
        ts = np.linspace(tmin, tmax, 300)
        ps = self.point(ts)
        out = cmt.plotbox(ps, scale)

    def corner(self):
        raise NotImplementedError('TODO')

    def __str__(self):
        return 'curve parameterized over [%s, %s]\n' % self.bounds

    def isinf(self):
        # False unless overridden by subclass
        return False

    def point(self, ts):
        # a naive solution here is fine for the moment
        # anything better relies on building blocks that are not
        # available yet
        return np.array([ self.position(t) for t in np.asarray(ts) ])

    def xypoint(self, t):
        z = self.point(t)
        return np.array([z.real, z.imag])

    def position(self, ts):
        ts = np.asarray(ts, dtype = np.float)
        return self._positionfun(ts)

    def tangent(self, t):
        ts = np.asarray(ts, dtype = np.float)
        return self._tangentfun(ts)

