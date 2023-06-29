import pandas
from sklearn import linear_model

df = pandas.read_csv("ML/data.csv")

X = df[['Weight', 'Volume']] # general notationvfor a independent variable is writen in capital
y = df['CO2'] # dependent in Small letters

regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)


#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)
print(regr.coef_)



