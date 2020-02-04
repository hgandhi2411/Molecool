"""
molecool
A python package for the MSF 2020A bootcamp
"""

# Add imports here
from .functions import *
from .atom_data import atomic_weights, atom_colors
from .measure import calculate_angle, calculate_distance
from .molecule import build_bond_list
from .visualize import bond_histogram, draw_molecule

import molecool.molecool_io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
