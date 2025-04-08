import csv 
import  pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("Students_Grading_Dataset.csv")

df = pd.DataFrame(data)

data['Fmaily_Income_Level'] = data['Family_Income_Level']
data['Attendance (%)'] = data['Attendance (%)']

#== df.groupby('Attendance (%)')['Famil_Income_Level'].mean().reset_index()

fig,ax = plt.subplots() 

plt.bar(data['Family_Income_Level'],data['Attendance (%)'])

plt.xlabel('Fmily_Income_Level')
plt.ylabel('Attendance (%)')
plt.title('How Family Income Has An Impact On Attendance')

plt.legend()
plt.show()