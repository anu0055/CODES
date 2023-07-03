import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Age':[36,42,23,52,43,44,66,35,52,35,24,18,45],
    'Experience':[10,12,4,4,21,14,3,14,13,5,3,3,9],
    'Rank':[9,4,6,4,8,5,7,9,7,9,5,7,9],
    'Nationality':['UK','USA','N','USA','USA','UK','N','UK','N','N','USA','UK','UK'],
    'Go':['NO','NO','NO','NO','YES','NO','YES','YES','YES','YES','NO','YES','YES']
}

df = pd.DataFrame(data)
file_name= 'data.csv'
df.to_csv(file_name, index=False)

#changing the string values to numerical
d={'UK':0, 'USA':1, 'N':2}
df['Nationality'] = df['Nationality'].map(d)
d= {'NO':0, 'YES':1}
df['Go'] = df['Go'].map(d)


# FOR POST-PRUNNING DATA and report printing
  #Seperating the independent an dthe dependent features
    # X= df.iloc[:,:-1]
    # y= df['Go']


#TEST TRAIN SPLIT
    # from sklearn.model_selection import train_test_split

    # X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)

    # from sklearn.tree import DecisionTreeClassifier

    # treemodel = DecisionTreeClassifier()
    # treemodel.fit(X_train,y_train)

    # from sklearn import tree
    # plt.figure(figsize=(8,10), dpi=65.99)
    # tree.plot_tree(treemodel, filled=True)
    # plt.show()

    # y_pred = treemodel.predict(X_test)

    # from sklearn.metrics import classification_report, accuracy_score
    # score = accuracy_score(y_pred, y_test)
    # print(score)
    # report = classification_report(y_pred,y_test)
    # print(report)
    
    
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)
plt.show()