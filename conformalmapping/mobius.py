from .mobiusbase import MobiusBase, standardmap
from .circle import Circle
from .zline import Zline
from .disk import Disk
import numpy as np
import numpy.linalg

class Mobius(MobiusBase):
    def __init__(self, **kwargs):
        super(Mobius, self).__init__(**kwargs)

    @staticmethod
    def from_matrix_elements(a, b, c, d):
        return Mobius(M = np.array([[a, b], [c, d]]))

    @staticmethod
    def from_vectors(z, w):
        z = np.asarray(z)
        w = np.asarray(w)
        A1 = standardmap(z)
        circ = Circle.from_vector(z)
        domain = None
        ran = None
        if not circ.isinf():
            domain = Disk(circ)

        A2 = standardmap(w)
        circ = Circle.from_vector(w)
        if not circ.isinf():
            ran = Disk(circ)

        matrix = np.linalg.solve(A2, A1)
        return Mobius(M = matrix, domain = domain, range = ran)

    @staticmethod
    def from_circles(z, w):
        raise NotImplementedError('todo')

    def inv(self):
        return Mobius(numpy.linalg.inv(self._M))

    def applyMap(self, z):
        if isinstance(z, Circle):
            zp = self.pole()
            if z.dist(zp) < 10 * np.spacing(np.max([zp.real, zp.imag])):
                # result appears to be a line
                zp = self.applyMap( z.point(np.array([0.5, 1.5]) * np.pi) )
                return Zline(zp)
            else:
                #zp = self.applyMap( z.point(np.array([0.5, 1.0, 1.5]) * np.pi ) )
                zs = z.point(np.array([0.0, 0.25, 0.75]) )
                zp = self.applyMap( zs )
                return Circle.from_vector(zp)
        else:
            return super(Mobius, self).applyMap(z)


