import numpy as np

print('numpy version: {}'.format(np.__version__))

A1 = np.zeros((2, 5))

print(A1)

D1 = np.random.rand(A1.shape[0], A1.shape[1])

print(D1)
