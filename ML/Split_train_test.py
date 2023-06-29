import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

X = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100)/X

train_X = X[:80]
train_y = y[:80]
test_X = X[80:]
test_y = y[80:]

model = np.poly1d(np.polyfit(train_X, train_y, 4))
myline = np.linspace(0, 6, 100)
r2 = r2_score(train_y, model(train_X)) # For the training DATA
print(r2)
r2_test = r2_score(test_y, model(test_X))
print(r2_test)
# predicting a new value
print(model(5))

plt.scatter(train_X, train_y)
plt.plot(myline, model(myline))
plt.show()

# The example predicted the customer to spend 22.88 dollars, as seems to correspond to the diagram: