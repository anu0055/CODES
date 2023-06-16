import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,0,100,100,0])
ypoints = np.array([0,100,100,0,0])
zpoints = np.array([50,50,0,0,100,100,50])
wpoints = np.array([0,100,100,50,50,0,0])

plt.plot(xpoints,ypoints)
plt.plot(zpoints, wpoints)
plt.show()

