from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv('pizza2.csv')
# print(df)


x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# print(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model = LogisticRegression()


model.fit(x_train,y_train)

print("Predicting output....")


age = int(input("Enter your Age: "))
weight = int(input("Enter your weight: "))
pred = model.predict([[age,weight]])
print(pred[0])
# pred = model.predict([[22,55]])
# print(pred[0])


if pred[0] == 1:
    print("Enjoy pizza!!")
else:
    print("Go to Gym!!")