# Train a logistic regression classifier to indentify whether a flower is iris_verginica or not

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
print(list(iris.keys()))

x= iris['data'][:,3:]
#print(x)
y = (iris['target'] == 2).astype(np.int32)
#print(y)

clf = LogisticRegression()
clf.fit(x,y)
example = clf.predict(([[7.6]]))
print(example)

#Using matplotlib to plot

x_new = np.linspace(0,3,1000).reshape(-1,1)
#print(x_new)
y_new_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_new_prob[:, 1], "-g", label = "verginica")
plt.show()
#print(iris['data'].shape)
#print(iris['target'])
#print(iris['DESCR'])
#print(iris['filename'])
