import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from logistic import LogisticRegression

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 1234)

clf = LogisticRegression(lr=0.01, n_iters=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

acc = accuracy(y_test, y_pred)
print("Accuracy:", acc)
