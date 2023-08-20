import numpy as np

def sigmoid_fn(x):
    return 1 / (1 + np.exp(-x))

w1 = 3
w2 = 5
b = -2.2
score  = w1*0.4 + w2*0.6 + b
print(sigmoid_fn(score))
print(sigmoid_fn(-2))
print(sigmoid_fn(-20))

print(np.log(10**-9))