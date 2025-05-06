import numpy as np
import math    
import copy as cp         

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        return np.sum(self.config)

    def off(self):
        """
        Return number of bits that are on
        """
        count = 0
        for i in self.config:
            if i==0:
                count += 1
        return count

    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        if self.config[i] == 0:
            self.config[i] = 1
        else:
            self.config[i] = 0
    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        decimal = 0
        for i,bit in enumerate(reversed(self.config)):
            decimal = decimal + bit * (2**i)
        return decimal
 

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        for i,value in enumerate(s):
            self.config[i] = value
        
        

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        if dec is None:
            dec = 0
        
        for i in range(self.N):
            self.config[self.N-1-i] = dec%2
            dec /= 2
        return self