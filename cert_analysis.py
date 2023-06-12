import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree, preprocessing

data = pd.read_csv("FullCertListSorted.csv")
# Dummy Encode the string data
data_encoded = pd.get_dummies(data[["IssuerOrgName", "IssuerComName", "IssuerCountry", "SubjectCountry"]])
# Drop old categorical data
data = data.drop(columns=["IssuerOrgName", "IssuerComName", "IssuerCountry", "SubjectCountry"])
# Combine old data with new encoded data
data = pd.concat([data, data_encoded], axis=1)

data_x = data.drop("Malicious", axis=1)
data_y = data["Malicious"]

depth = 3

# Perform the Training and Test the data
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2)
# Use Cross-Validation to test for overfitting or anomalies
X_train, X_val, y_train, y_val =  train_test_split(X_train, y_train, test_size=0.25)

# DECISION TREE

# dtree = DecisionTreeClassifier(max_depth=depth)
# dtree.fit(X_train, y_train)
# predictions = dtree.predict(X_test)
# acc = accuracy_score(y_test, predictions)
# print("Test accuracy score for ", depth," depth is: ", round(acc*100, 2), "%", sep="")

#RANDOM FOREST

# trees = 30
# acc = 0
# for i in range(10):
# 	rf = RandomForestClassifier(n_estimators=trees, bootstrap=False)
# 	rf.fit(X_train, y_train)
# 	predictions = rf.predict(X_test)
# 	acc = acc + accuracy_score(y_test, predictions)
# print("Test accuracy score for ", trees," depth is: ", round(acc*10, 2), "%", sep="")

#GRADIENT BOOSTING

acc = 0
for i in range(10):
	gb = GradientBoostingClassifier(max_features="log2", loss="log_loss", criterion="friedman_mse")
	gb.fit(X_train, y_train)
	predictions = gb.predict(X_test)
	acc = acc + accuracy_score(y_test, predictions)
print("Test accuracy score: ", round(acc*10, 2), "%", sep="")


scores = (cross_val_score(gb, X_val, y_val, cv=5))
print("%0.2f validation accuracy with a standard deviation of %0.2f" % (scores.mean()*100, scores.std()*100))

