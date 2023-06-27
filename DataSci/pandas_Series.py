import pandas as pd
a=[1,7,2]
myvar = pd.Series(a, ["x", "y", "z"])
print(myvar)
print(myvar["x"])

'''We can also pass a dictionary as a pandas series'''
#Code:
'''
calories = {"day1": 470, "day2": 360, "day": 370}
myvar = pd.Series(calories)
print(myvar)'''

#This will give the keys as the labels and the values as the elements coressponding to it 