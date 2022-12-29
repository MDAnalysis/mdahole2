from typing import Tuple

import MDAnalysis as mda
from MDAnalysis.coordinates.memory import MemoryReader
import numpy as np


def executable_not_found(*args):
    """Return ``True`` if none of the executables in args can be found.
    ``False`` otherwise (i.e. at least one was found).
    To be used as the argument of::
    @dec.skipif(executable_not_found("binary_name"), msg="skip test because binary_name not available")
    """
    # This must come here so that MDAnalysis isn't imported prematurely,
    #  which spoils coverage accounting (see Issue 344).
    import MDAnalysis.lib.util
    for name in args:
        if MDAnalysis.lib.util.which(name) is not None:
            return False
    return True
