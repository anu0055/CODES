import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.plot(x,y)
plt.grid(axis='x', color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()