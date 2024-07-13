from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
# from sklearn.naive_bayes import GaussianNB
df = pd.read_csv('data.csv')
# print(df)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=6)


model = RandomForestClassifier(random_state=12)
model.fit(x_train,y_train)

pred = model.predict([[151,88,74,647,101]])
print(pred)


y_pred = model.predict(x_test)
acc_scrore = accuracy_score(y_pred,y_test)
print(acc_scrore * 100) #100


#meta variable of pickle
pickle.dump(model,open('model.pkl','wb'))


#pickle : it is an meta variable used to dump the predictive model inoreder to make future prediction