import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Print the DataFrame
#print(df.head())

#Independent and dependent features
X=df.iloc[:, :-1]
y=iris.target

#Train Test and Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.33,random_state=42)

from sklearn.tree import DecisionTreeClassifier

#Post-prunning technique
treemodel = DecisionTreeClassifier(max_depth=2)
treemodel.fit(X_train, y_train)

from sklearn import tree
plt.figure(figsize=(15,10), dpi=67.99)
tree.plot_tree(treemodel, filled=True)
plt.show()

#Prediction
y_pred = treemodel.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score, classification_report

score = accuracy_score(y_pred, y_test)
print(score)
print(classification_report(y_pred, y_test))



