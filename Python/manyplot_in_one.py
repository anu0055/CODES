import matplotlib.pyplot as plt
import numpy as np

# plot1:

x = np.array([1,2,3,4])
y = np.array([1,2,2,3])
plt.subplot(1,2,1)
plt.title("Growth")
plt.plot(x,y)

#plot 2:

x = np.array([1,2,4,5])
y = np.array([10,20,30,50])
plt.subplot(1,2,2)
plt.title("Income")
plt.plot(x,y)

plt.suptitle("MY SHOP")
plt.show()