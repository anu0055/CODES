import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
y = [217245.53, 685356.92, 751782.32, 772543.69, 794065.78, 775117.53, 775330.71, 834319.78, 830345.16, 831899.62]
mymodel = np.poly1d(np.polyfit(x,y,4))
myline = np.linspace(2013,2022,1000)
plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()
print(r2_score(y, mymodel(x))) # Hence correlation b/w x and y axis is very good (i.e. 0.9856) for future predictions
income = mymodel(2024) # IF we go by this prediction, which may be wrong, but according to it the market is going to have a large crash in the year 2024
                       # So investing in blue chip funds will be benificial
print(income)