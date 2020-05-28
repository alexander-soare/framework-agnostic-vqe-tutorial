"""
Helper functions for the tutorial notebookds
"""


import cmath  # for complex math operations
import numpy as np  # for matrix multiplication
import random
from typing import Tuple


class HamiltonianBuilder():
    """
    Helpere class for generating Hamiltonians from sums of single-qubit
    pauli matrices.
    """

    def __init__(self, coefficients_={}):
        # define standard single qubit puali matrices
        identity = np.eye(2)
        sigma_x = np.array([[0, 1], [1, 0]])
        sigma_y = np.array([[0, complex(0, -1)], [complex(0, 1), 0]])
        sigma_z = np.array([[1, 0], [0, -1]])
        self.pauli_matrices = {
            'i': identity,
            'x': sigma_x,
            'y': sigma_y,
            'z': sigma_z
        }
        # initialise random coefficents
        self._zero_coefficients()
        self.reset_coefficients(coefficients_)
        # build the hamiltonian
        self._build()

    def reset_coefficients(self, coefficients_={}):
        """
        coefficients_ is a dictionary expected in the form
        {
            'i': {coefficient of the identity term},
            'x': {coefficent of sigma_x}
            'y': ...
            'z': ...
        }
        not all keys need to be present
        if coefficients_ is not provided, a random set is initialised
        """
        self._zero_coefficients()
        if len(coefficients_) <= 0:
            self._init_random_coefficients()
        else:
            assert all(key in self.coefficients.keys() for key in coefficients_.keys()), \
                "Coefficients dict incorrectly formed"
            self.coefficients.update(coefficients_)
        self._build()

    def _zero_coefficients(self):
        self.coefficients = {'i': 0, 'x': 0, 'y': 0, 'z': 0}

    def _build(self):
        """
        build the hamiltonian
        """
        # initialise zeros matrix for hamiltonian
        self.hamiltonian = np.zeros(shape=(2, 2)).astype('complex128')
        # run through coefficients dict and build hamiltonian additively
        for key in self.coefficients:
            self.hamiltonian += self.coefficients[key] * \
                self.pauli_matrices[key]

    @property
    def matrix(self):
        return self.hamiltonian

    def _init_random_coefficients(self):
        for k, v in self.coefficients.items():
            self.coefficients[k] = random.randint(-3, 3)
