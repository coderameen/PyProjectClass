from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd



df  = pd.read_csv('data.csv')
# print(df)

#To get the inforamtion about dataFrame
# print(df.info())

# print("------")
# print(type(df))

# print(df.shape)


#To check NAN values in dataFrame
totalNaNValues = df.isna().sum()
print(totalNaNValues)
