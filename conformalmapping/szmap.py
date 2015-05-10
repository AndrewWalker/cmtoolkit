import numpy as np
from .conformalmap import ConformalMap
from .closedcurve import ClosedCurve 
from .unitdisk import unitdisk
from .region import Region

class SzMap(ConformalMap):
    """SzMap represents a Riemann map via the Szego kernel.
    """

    def __init__(self, *args, **kwargs):
        range_ = kwargs.get('range', None)
        if isinstance(range_, ClosedCurve):
            range_ = Region(range_)
        if not range_.issimplyconnected():
            raise Exception('Region must be simply connected')
        kwargs['range'] = range_
        kwargs['domain'] = unitdisk()

        super(SzMap, self).__init__(**kwargs)

        boundary = self.range.outer

    def applyMap(self, z):
        pass
