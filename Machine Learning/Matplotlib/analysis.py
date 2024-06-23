'''
Matplotlib: "It is an library used for Analysing and Visualization of dataset and dataframe"
#To convert our data into visual form/To represent Graphically


#pip install matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt
'''
#BAR GRAPHS (Analysing the result based on marks of students)
#marks of the student
x = [1,2,3,4]
y = [56,78,94,12]
labels = ['Fail','Second Class','First Class','Distinction']

plt.bar(x,y,tick_label=labels,width=0.5,color=['purple','orange','red','green'])
plt.xlabel('students')
plt.ylabel('percentages')
plt.title('RESULT')
plt.show()
'''

'''
#PIE Chart
contents = ['Animals','Plants','Humans']
slice = [3,7,8]
colors = ['purple','green','red']
plt.pie(slice,labels=contents,colors=colors,startangle=90,shadow=True,explode=(0,0,0.05),autopct="%1.0f%%")
plt.legend()
plt.title("Made by Fariya")
plt.show()
'''


# #Scatter Plot
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [2,3,4,5,7,6,6,8,9,9]
# plt.scatter(x,y,color="orange",marker="*")
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Scatter Plot')
# plt.show()




#Histogram
'''
percentages = [25,5,45,66,78,43,34,89,12,34,56,78,90,95,98,69]
range =  (0,100)
num = 10 #total bars

plt.hist(percentages,num,range,color="orange", histtype='bar',rwidth=0.5)
plt.show()

'''

#Plot the data graph from CSV(Dataset)
import csv

x = []
y = []

with open('pizza2.csv','r') as file:
    df = csv.reader(file)
    for col in df:
        # print(col[0])
        x.append(col[0])
        y.append(col[2])
        # print(col[0])
        
        
    
# plt.plot(x,y,label="Analyse",color="orange")
# plt.show()

# plt.scatter(x,y,label="Age vs Eat_PiZZA", color="orange", marker="*")
# plt.show()