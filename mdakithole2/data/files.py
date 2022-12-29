"""
Location of data files
======================

Use as ::

    from mdakithole2.data.files import *

"""

__all__ = [
    "MDANALYSIS_LOGO",  # example file of MDAnalysis logo
]

from pkg_resources import resource_filename

MDANALYSIS_LOGO = resource_filename(__name__, "mda.txt")
