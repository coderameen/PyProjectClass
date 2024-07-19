#Diabetes Prediction Model....Training
# from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
# from sklearn import tree
# model = tree.DecisionTreeClassifier()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

df = pd.read_csv('diabetes.csv')
# print(df)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


model = GaussianNB()
model.fit(x_train,y_train)

pred = model.predict([[4,110,92,0,0,37.6,0.191,30]])
print(pred)


y_pred = model.predict(x_test)
acc_scrore = accuracy_score(y_pred,y_test)
print(acc_scrore * 100) #97%


#meta variable of pickle
pickle.dump(model,open('diabetes_model.pkl','wb'))


#pickle : it is an meta variable used to dump the predictive model inoreder to make future prediction