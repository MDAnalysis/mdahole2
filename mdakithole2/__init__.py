"""
mdakithole2
A Python interface for the HOLE suite tools to analyze an ion channel pore or transporter pathway as a function of time or arbitrary order parameters.
"""

# Add imports here
from .mdakithole2 import canvas

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
