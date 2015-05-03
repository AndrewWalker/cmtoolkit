from .closedcurve import ClosedCurve

class Region(object):
    """

    A region is defined by one or more closed curves. The interior of a
    region is defined to be to the left of the tangent vector of the closed
    curve. The exterior is the compliment of the interior.
    
    TBD: What does it mean for a region object to have no boundary curves?
    Currently isempty() returns true if there are no boundary curves, which
    is admittedly a bit ambiguously named. Do we mean an empty set for a
    region, or do we mean the entire plane?
    """

    def __init__(self, outer = None, inner = None, *args, **kwargs):
        self._outerboundaries = self._checkcc(outer)
        self._innerboundaries = self._checkcc(inner)

    @staticmethod
    def simply_connected_region(boundary, **kwargs):
        """Construct a region with no holes
        """
        return Region(outer = boundary, **kwargs)

    @property
    def outer(self):
        print 'outer', len(self._outerboundaries)
        if len(self._outerboundaries) == 1:
            return self._outerboundaries[0]
        else:
            return self._outerboundaries

    @property
    def inner(self):
        if len(self._innerboundaries) == 1:
            return self._innerboundaries[0]
        else:
            return self._innerboundaries

    @property
    def numinner(self):
        return len(self._innerboundaries)

    @property
    def numouter(self):
        return len(self._outerboundaries)

    @property
    def boundaries(self):
        """Return a combined list of (inner and outer) boundaries
        """
        return self._outerboundaries + self._innerboundaries


    @property
    def connectivity(self):
        return self.numinner + self.numouter

    @staticmethod
    def interiorto(*args):
        # https://github.com/tobydriscoll/conformalmapping/blob/master/region.m#L68
        pass

    @staticmethod
    def exteriorto(*args):
        # https://github.com/tobydriscoll/conformalmapping/blob/master/region.m#L70
        pass

    def _checkcc(self, suitor):
        if suitor is None:
            return []
        elif isinstance(suitor, ClosedCurve):
            return [ suitor ]
        else:
            for item in suitor:
                if not isinstance(item, ClosedCurve):
                    raise Exception('Not a list of closed curves')
            return suitor
        raise Exception('Not a list of closed curves')

    def isempty(self):
        return (self._innerboundaries != []) and (self._outerboundaries != [])

    def boundbox(self):
        #zi = np.zeros( 4 * self.numinner() )
        #for i in xrange(self.numinner()):
            #zi[np.arange(4*k, 4*k+4)] = 
        return None

    def connectivity(self):
        return self.numinner + self.numouter

    def __str__(self):
        if self.isempty():
            return 'empty region'
        else:
            raise NotImplemented('todo')

    def grid(self):
        return self.grid

    def plot(self, **kwargs):
        # This is reasonably simple minded until adapt is complete

        for b in self._innerboundaries:
            b.plot(**kwargs)

        for b in self._outerboundaries:
            b.plot(**kwargs)