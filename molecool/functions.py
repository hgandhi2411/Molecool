"""
functions.py
A python package for the MSF 2020A bootcamp

Handles the primary functions
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)
    Replace this function and doc string for your own project
    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from
    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def new_function():
    """ New change to test travis"""
    a1 =  5

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
