# -*- coding: utf-8 -*-
"""Utilities for working with spin as an internal degree of freedom."""

import numpy as np

sigma_0 = np.array([[1, 0], [0, 1]])
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

def spin_conductance(G, lead_out, lead_in, sigma=sigma_z):
    """Calculate the spin conductance between two leads.

    Uses the expression

        G =  Tr[ σ_{α} Γ_{q} G_{qp} Γ_{p} G^+_{qp} ]   (1)

    Where  Γ_{q} is the coupling matrix to lead q ( = i[Σ - Σ^+] )
    and G_{qp} is the submatrix of the system's Greens function
    between sites interfacing with lead p and q (not to be confused
    with the "G" on the left-hand-side, which is the spin conductance
    between the two leads).

    Parameters
    ----------
    G : `kwant.solvers.common.GreensFunction`
        The Greens function of the system as returned by
        `kwant.greens_function`.
    lead_out : positive integer
        The lead where spin current is collected
    lead_in : positive integer
        The lead where spin current is injected
    sigma : `numpy.ndarray` of shape (2, 2)
        The Pauli matrix of the quantization axis along
        which to measure the spin current

    Notes
    -----
    Assumes that the spin structure is encoded in the matrix structure
    of the Hamiltonian elements (i.e. there are not separate lattices/
    sites for the spin degree of freedom). If you have the spin degree
    of freedom on a separate lattice already you can trivially get
    the spin conductance by using separate spin up/down leads.

    See http://dx.doi.org/10.1103/PhysRevB.89.195418 for a derivation
    of equation (1).
    """
    # calculate Γ G Γ G^+
    ttdagger = G._a_ttdagger_a_inv(lead_out, lead_in)
    shp = attdagger.shape[0] // sigma.shape[0]
    # build spin matrix over whole lead interface
    sigma_matrix = np.kron(np.eye(shp), sigma)
    return np.trace(sigma_matrix.dot(ttdagger)).real
