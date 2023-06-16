import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr1 =[]
arr2 =[]

for i in range(10):
    x = random.randint(100)
    y = random.randint(50)
    arr1.append(x)
    arr2.append(y)

plt.plot(arr1,arr2)
plt.show()
