import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x,y,3)) # 3 is the degree of the polynomial
myline = np.linspace(1,22,100)
speed = mymodel(4)
plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()
print(r2_score(y, mymodel(x)),"\n", speed)