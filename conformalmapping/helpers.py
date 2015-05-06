import functools
import numpy as np

def suppress_warnings(f):

    @functools.wraps(f)
    def impl(*args, **kwargs):
        oldsettings = {}
        try:
            oldsettings = np.seterr(all = 'ignore')
            return f(*args, **kwargs)
        finally:
            np.seterr(**oldsettings)
    return impl
