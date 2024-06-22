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


#Scatter Plot
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,5,7,6,6,8,9,9]
plt.scatter(x,y,color="orange",marker="*")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.show()