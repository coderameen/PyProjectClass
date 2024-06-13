#Steps:
'''
1.Import packages
2.Reading/loading Datasets
3.Splitting Dataset into X-axis(Input) and Y-axis(Output)
4.Splitting dataset into Training and testing parts
5.Call Algorithm
6.Train Model
7.Predict the outcome
'''
#1.import packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

#2.Reading/loading dataset
df = pd.read_csv('cgpa.csv')

# print(df.head())
# print(df.tail(7))

#3.Splitting dataset into input(x-axis) and output(y-axis)
x = df.iloc[:,:-1] #input syntax iloc=> index location
y = df[['CGPA']]
# print(x)
# print(y)

#4.splitting dataset into training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

#5.call algorithm
model = LinearRegression()

print("prdicting output....")
#6.Train the model
model.fit(x_train,y_train)


#7.predict outcome
# pred = model.predict([[11]])


hour_var = int(input("Enter the number of hours you studied: "))
pred = model.predict([[hour_var]])
print("The model predicted CGPA is: ",pred[0][0])