import numpy as np
import networkx as nx
from .bitstring import BitString
from .isinghamiltonian import IsingHamiltonian

class MonteCarlo():
    """
    Class for IsingHamiltonian functions
    """
    def __init__(self, ham):
        self.ham = ham
    
    def run(self, T, n_samples, n_burn):
        bits = BitString(len(self.ham.G.nodes))
        bits_E = self.ham.energy(bits)

        energies = []
        magnetizations = []

        for i in range(n_samples + n_burn):
            original = BitString(bits.N)
            original.config = bits.config.copy()

            index = np.random.randint(len(bits))
            original.flip_site(index)

            original_E = self.ham.energy(original)
            dE = original_E - bits_E

            if dE < 0 or np.random.rand() < np.exp(-dE/T):
                bits = original
                bits_E = original_E

            if i>=n_burn:
                energies.append(bits_E)
                magnetizations.append(np.sum(2 * bits.config - 1))

        return energies, magnetizations