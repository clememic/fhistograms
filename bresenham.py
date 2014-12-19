"""
Module for generating pixel coordinates of oriented lines in images.
"""

import math
from skimage.draw import line as skimage_line


def line(theta, rho):
    """
    Return the pixel coordinates of a `theta` oriented line of length `rho`.

    Parameters
    ----------
    theta : float
        The orientation angle in radians.
    rho : float
        The length of the line from the origin.

    Returns
    -------
    ii, jj : (N,) ndarray of int
        Pixel coordinates of the line (row-column format).

    Notes
    -----
    Merely a wrapper for `skimage.draw.line` with polar coordinates.

    """
    x1, y1 = (0, 0)
    x2 = int(round(rho * math.cos(theta)))
    y2 = int(round(rho * math.sin(theta)))
    ii, jj = skimage_line(y1, x1, y2, x2)
    return ii, jj
