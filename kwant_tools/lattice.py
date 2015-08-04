# -*- coding: utf-8 -*-
"""Utilities for working with Kwant lattices."""

import functools as ft
import itertools as it

import numpy as np
import kwant

def within(distance):
    """Check if sites are within a certain distance.
    
    Parameters
    ----------
    distance : positive real

    Returns
    -------
    A function which takes two sites and returns True if they
    are within `distance` of one another and False otherwise.
    """
    return lambda i, j: np.linalg.norm(j.pos - i.pos) < distance


def connections(sites, connected, sym=None):
    """Yield hoppings between sites which are connected.

    Based on the work of Sergey Slizovskiy (see
    http://comments.gmane.org/gmane.comp.science.kwant.user/442
    for details).

    Parameters
    ----------
    sites : iterable of `kwant.builder.Site`
    connected : function
        Takes a pair of `kwant.builder.Site` and returns True if
        there is a connection between the sites. Must be symmetric
        with respect to its arguments.
    sym : function or `None` (default)
        A symmetry group element to apply to one of the sites in
        the pair before checking for connectivity. It is a function
        which should take a `kwant.builder.Site` and return a
        `kwant.Builder.Site`.
    """
    for i, j in it.product(sites, repeat=2):
        if sym:
            j = sym(j)
        if i == j:
            continue
        elif connected(i, j):
            yield i, j


def group_element(symmetry, element):
    """Return an element of a symmetry group.

    Parameters
    ----------
    symmetry : `kwant.builder.Symmetry`
        The symmetry group from which to take the element.
    element : group element representation
        A representation of the group element. Usually
        (for `kwant.lattice.TranslationalSymmettry`) this
        will be a sequence of integers.

    Returns
    -------
    A function which can be applied to `kwant.builder.Site`
    and which returns `kwant.builder.Site`.
    """
    return ft.partial(symmetry.act, element)
