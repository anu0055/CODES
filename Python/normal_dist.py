from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.normal(size = 100)
print(x)
sns.distplot(x, hist=False)
plt.show()