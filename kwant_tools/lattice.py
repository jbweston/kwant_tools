import numpy as np
import itertools as it
import kwant

def within(distance):
    """Check if sites are within a certain distance.
    
    Parameters
    ----------
    distance: positive real

    Returns
    -------
    A function which takes two sites and returns True if they
    are within `distance` of one another and False otherwise.
    """
    return lambda i, j: np.linalg.norm(j.pos - i.pos) < distance


def connections(sites, connected, sym=kwant.builder.NoSymmetry()):
    """Yield hoppings between sites which are connected.

    Parameters
    ----------
    sites: iterable of `kwant.builder.Site`
    connected: function
        Takes a pair of `kwant.builder.Site` and returns True if
        there is a connection between the sites. Must be symmetric
        with respect to its arguments.
    sym: `kwant.builder.Symmetry` (default: `kwant.builder.NoSymmetry`)
        A symmetry to apply to one of the sites in the pair before
        checking for connectivity.
    """
    for i, j in it.product(sites, repeat=2):
        j = sym(j)
        if i == j:
            continue
        elif connected(i, j):
            yield i, j