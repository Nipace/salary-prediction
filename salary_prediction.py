
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pickle

#importing dataset 
dataset = pd.read_csv('Salary_Data.csv')

#categorical data
dataset_dummy = pd.get_dummies(dataset["Position"])

dataset_dummy = pd.concat([dataset_dummy,dataset],axis=1)

dataset_dummy.drop(["Position"], inplace = True, axis =1)

X = dataset_dummy.iloc[:, :-1].values
y = dataset_dummy.iloc[:, -1].values

#splitting the dataset into the training set nad test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train , y_test = train_test_split(X, y , test_size = 1/3, random_state = 0)

#fitting simple linear regression to training sets
from sklearn.linear_model import LogisticRegression 
regressor = LogisticRegression(max_iter=1000)
regressor.fit(X_train, y_train)

#predicting the test set results
y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('model.pkl','wb'))    


