
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pickle
from logistic_regression import KNN
#importing dataset 

dataset = pd.read_csv('Salary_Data4.csv')

# #categorical data
dataset_dummy = pd.get_dummies(dataset["Position"])

dataset_dummy = pd.concat([dataset_dummy,dataset],axis=1)

dataset_dummy.drop(["Position"], inplace = True, axis =1)

X = dataset_dummy.iloc[:, :-1].values
y = dataset_dummy.iloc[:, -1].values

# #splitting the dataset into the training set nad test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train , y_test = train_test_split(X, y , test_size = 1/3, random_state = 0)

# #fitting simple linear regression to training sets
# from sklearn.linear_model import LinearRegression 
# regressor = LinearRegression()

# regressor.fit(X_train, y_train)
# #model = LineaRegression( learning_rate = 0.001, n_iters = 1000000 )
# #model.fit(X_train, y_train) 
# #predicting the test set results
# y_pred = regressor.predict(X_test)
# y_pred1 = clf.predict(X_test)

k = 3
clf = KNN(k=k)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

def accuracy(y_true, y_predi):
    accuracy = np.sum(y_true == y_predi) / len(y_true)
    return accuracy

mse = accuracy(y_test, y_pred)
print("MSE:", mse)
pickle.dump(clf, open('model.pkl','wb'))    


