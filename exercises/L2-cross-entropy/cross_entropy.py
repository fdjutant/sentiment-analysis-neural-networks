import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    CE = -np.sum(Y * np.log(P) + [1 - x for x in Y] * np.log([1 - k for k in P])) 
    return CE