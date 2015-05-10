from .conformalmap import ConformalMap

class SzMap(ConformalMap):

    def __init__(self, *args, **kwargs):

        super(SzMap, self).__init__(**kwargs)

