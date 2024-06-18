from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.metrics import accuracy_score


'''
Outcomes(Multi class output)
1 => Normal
2 => Mild
3 => Moderate
4 => Severe
'''

#read dataset
df = pd.read_csv('data.csv')
# print(df)

#splitting dataset into x and y axis(input and output)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
# print(x)
# print(y)

#The shape of dataframe
print(x.shape)#(5000, 5)
print(y.shape)#(5000, 1)

#splitting dataset into traing and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#Analytics of dataframe
print(x_train.shape)#[4000 rows x 5 columns] it is take only 80%
print(y_train.shape)#(4000,)

#testing (20%)
print(x_test.shape)
print(y_test.shape)



#train and predict
model = LogisticRegression(solver="liblinear", max_iter=1000, random_state= 31)

#train
model.fit(x_train,y_train)

#prediction

pred = model.predict([[184,98,88,171,70]])
print("The Prediction condition of patient is: ",pred)

if pred[0] == 1:
    output = "Normal"
    print("Covid symptom is: ",output)
elif pred[0] == 2:
    output = "Mild"
    print("Covid symptom is: ",output)
elif pred[0] == 3:
    output = "Moderate"
    print("Covid symptom is: ",output)
else:
    output = "Severe"
    print("Covid symptom is: ",output)



#test
y_pred = model.predict(x_test)
#To find accuracy of the model
acc_score = accuracy_score(y_pred,y_test)
print(round(acc_score * 100))