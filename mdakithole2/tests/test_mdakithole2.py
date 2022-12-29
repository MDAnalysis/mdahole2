"""
Unit and regression test for the mdakithole2 package.
"""

# Import package, test suite, and other packages as needed
import mdakithole2
import pytest
import sys


def test_mdakithole2_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mdakithole2" in sys.modules


def test_mdanalysis_logo_length(mdanalysis_logo_text):
    """Example test using a fixture defined in conftest.py"""
    logo_lines = mdanalysis_logo_text.split("\n")
    assert len(logo_lines) == 46, "Logo file does not have 46 lines!"
