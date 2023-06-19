import matplotlib.pyplot as plt
import numpy as np

x =np.array([35,25,25,15])
mylabels = ["Apples", "Babanas", "Oranges", "Mangoes"]
#Exploding the Apples char 0.3 away from the center.
#explodes = [0.3,0,0,0]
colour = ["black", "hotpink", "b", "g"]
plt.pie(x, labels = mylabels, colors = colour, shadow = True)
plt.legend(title = "Four Fruits")
plt.show()