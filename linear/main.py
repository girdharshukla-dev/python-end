import numpy as np 

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

mean_x = np.mean(x)
mean_y = np.mean(y)

m = np.sum(((x-mean_x)*(y-mean_y))/np.sum((x-mean_x)**2))
c = mean_y - m*mean_x

print(f"y={m:.2f}x + {c:.2f}")
