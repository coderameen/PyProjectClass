#Heart desease model training....
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
# breakpoint()

df = pd.read_csv('heart_dataset.csv')
# print(df)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=6)


model = LogisticRegression()
model.fit(x_train,y_train)

pred = model.predict([[34,0,1,118,210,0,1,192,0,0.7,2,0,2]])
print(pred)


y_pred = model.predict(x_test)
acc_scrore = accuracy_score(y_pred,y_test)
print(acc_scrore * 100) #86.34146341463415


#meta variable of pickle
pickle.dump(model,open('heart_model.pkl','wb'))


#pickle : it is an meta variable used to dump the predictive model inoreder to make future prediction