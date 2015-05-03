from .gridcurves import GridCurves

class ConformalMap(object):
    def __init__(self, domain = None, range = None, *args):
        self._domain = domain
        self._range  = range

    @property
    def range(self):
        return self._range

    @property
    def domain(self):
        return self._domain

    def __call__(self, z):
        return self.apply(z)

    def apply(self, z):
        if isinstance(z, GridCurves):
            return GridCurves([ self.applyMap(c) for c in z.curves ])
        else:
            return self.applyMap(z)

    def applyMap(self, z):
        return z

    def __str__(self):
        return '**conformalmap object**\n\n'

    def plot(self, *args, **kwargs):
        self(self.domain).plot()


