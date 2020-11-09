"""
Unit and regression test for the plb_data package.
"""

# Import package, test suite, and other packages as needed
import plb_data
import pytest
import sys

def test_plb_data_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "plb_data" in sys.modules
