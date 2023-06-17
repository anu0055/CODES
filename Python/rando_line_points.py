

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

ypoints = []

for i in range(5):
    y = random.randint(50)
    ypoints.append(y)
# print(ypoints)
plt.plot(ypoints, linewidth = 10,  ms =10, mec = 'r', mfc ='r')
plt.show()