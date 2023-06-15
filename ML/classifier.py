#Importing required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
#Loading datset
iris = datasets.load_iris()

#prining lables and description
#print(iris.DESCR) 

features = iris.data
labels = iris.target
#print(features[0], labels[0])

#Traing classifiler

clf = KNeighborsClassifier()
clf.fit(features, labels)

predict = clf.predict([[6.9,3.5,5.4,3.2]])
print(predict)

