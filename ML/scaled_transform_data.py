import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("ML/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X.values)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y.values)

scaled = scale.transform([[3300, 1.3]])
print(scaled)

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)