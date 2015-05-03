import numpy as np

class Zline(object):

    def __init__(self, points, **kwargs):
        super(Zline, self).__init__(**kwargs)
        self._points = points
        self._tangent = np.diff(points)

    def position(self, t):
        ts = t / (1-t**2)
        return self._points[0] + ts * self._tangent[0]

    def tangent(self, t):
        return self._tangent
