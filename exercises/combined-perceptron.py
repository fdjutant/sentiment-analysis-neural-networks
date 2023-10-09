import numpy as np

def sigmoid_fn(x):
    return 1 / (1 + np.exp(-x))

def simple_entropy_fn(m,n):
    sum = m + n
    return (-m * np.log2(m/sum) - n * np.log2(n/sum)) / (m+n)

def entropy_fn(event):
    
    entropy = 0
    total_event = sum(event)
    for i in range(len(event)):
        p = event[i] / total_event
        entropy += -p * np.log2(p)

    return entropy

print(simple_entropy_fn(4,10))
print(entropy_fn([8, 3, 2]))

# w1 = 3
# w2 = 5
# b = -2.2
# score  = w1*0.4 + w2*0.6 + b
# print(sigmoid_fn(score))
# print(sigmoid_fn(-2))
# print(sigmoid_fn(-20))

# print(np.log(10**-9))
