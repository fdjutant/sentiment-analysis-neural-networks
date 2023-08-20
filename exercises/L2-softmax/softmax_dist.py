import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    
    denom = np.sum(np.exp(L))
    
    list_softmax = []
    for i in range(len(L)):
        list_softmax.append(np.exp(L[i])/denom)
    
    return list_softmax