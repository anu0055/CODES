from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.normal(loc = 10, scale= 2, size = 100)
print(x)
sns.displot(x, kde = True)
plt.show()