"""
Module for generating pixel coordinates of oriented lines in images.
"""

import math
import numpy as np
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


def restrict(ii, jj, height, width):
    """
    Restrict the pixel coordinates of a line to the size of an image.

    Parameters
    ----------
    ii, jj : (N,) ndarray of int
        Pixel coordinates of the line.
    height, width : (int, int,)
        The size of the image.

    Returns
    -------
    ii, jj : (N,) ndarray of int
        Pixel coordinates of the line, restricted to the image size.

    Notes
    -----
    This function returns a copy of the initial pixel coordinates (i.e., the
    initial parameters `ii` and `jj` are untouched).

    """
    ii, jj = ii.copy(), jj.copy()

    left_ii = np.nonzero((ii >= height) if ii[0] >= ii[-1] else (ii < 0))[0]
    left_jj = np.nonzero((jj < 0) if jj[0] <= jj[-1] else (jj >= width))[0]
    left_ii = left_ii[-1] + 1 if left_ii.size > 0 else -1
    left_jj = left_jj[-1] + 1 if left_jj.size > 0 else -1
    left = max(left_ii, left_jj)
    if left != -1:
        ii = ii[left:]
        jj = jj[left:]

    if ii.size <= 0 or jj.size <= 0:
        return ii, jj

    right_ii = np.nonzero((ii < 0) if ii[0] >= ii[-1] else (ii >= height))[0]
    right_jj = np.nonzero((jj >= width) if jj[0] <= jj[-1] else (jj < 0))[0]
    right_ii = right_ii[0] if right_ii.size > 0 else ii.size
    right_jj = right_jj[0] if right_jj.size > 0 else jj.size
    right = min(right_ii, right_jj)
    if right < ii.size:
        ii = ii[:right]
        jj = jj[:right]

    return ii, jj
