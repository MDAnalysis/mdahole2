"""
mdahole2
A Python interface for the HOLE suite tools to analyze an ion channel pore or transporter pathway as a function of time or arbitrary order parameters.
"""
from . import analysis

# Handle version
from importlib.metadata import version
__version__ = version("mdahole2")
