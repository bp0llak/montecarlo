import numpy as np
import networkx as nx
from .bitstring import BitString

class IsingHamiltonian():
    """
    Class for IsingHamiltonian functions
    """
    def __init__(self, G):
        self.G = G
        self.mu = np.zeros(len(self.G.nodes))
        self.J = np.zeros((len(G.nodes), len(G.nodes)))
        self.N = len(self.G.nodes)
        for i, j in G.edges:
            self.J[i][j] = G.edges[i, j]['weight']
            self.J[j][i] = G.edges[i, j]['weight']
    
    def energy(self, config:BitString):
        E = 0.0

        spin = 2 * config.config - 1
    
        for i, j in self.G.edges:
            weight = self.G.edges[i, j]['weight']
            E += weight * spin[config.N-i-1] * spin[config.N-j-1]

        for i in self.G.nodes:
            E += self.mu[config.N-i-1] * spin[config.N-i-1]
    
        return E
    
    def set_mu(self, mus:np.array):
        self.mu = mus
        return self

    def compute_average_values(self, T:int):

        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0

        # Write your function here!
        beta = 1/T
        N = len(self.G.nodes)

        bs = BitString(N=N)


        for i in range(2**N):
            bs.set_integer_config(i)
            spin = 2 * bs.config - 1

            weight = np.exp(-beta * self.energy(bs))

            E += self.energy(bs) * weight
            M += np.sum(spin) * weight
            EE += self.energy(bs)**2 * weight
            MM += np.sum(spin)**2 * weight
            Z += weight
        
        E = E/Z
        M = M/Z
        HC = (EE / Z - E**2) / T**2
        MS = (MM / Z - M**2) / T

        return E, M, HC, MS