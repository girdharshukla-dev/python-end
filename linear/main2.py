# this is through gradient descent 

import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

m, c = 0.0, 0.0

alpha = 0.01
epochs = 1000
n = len(x)

for i in range(epochs):
    y_pred = m*x + c
    dm = (1/n) * np.sum((y_pred-y)*x)
    dc = (1/n) * np.sum((y_pred-y))
    m -= alpha*dm
    c -= alpha*dc

    if i%100 == 0:
        cost = (1/(2*n))*np.mean((y_pred-y)**2)
        print(f"Iter {i} : m={m:0.4f}, c={c:0.4f}, cost={cost}")

print(f"Final: y={m:0.2f}x + {c:0.2f}")
    