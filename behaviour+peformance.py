import csv
import pandas as pd
import matplotlib.pyplot as plt

#with open('Students_Grading_Dataset.csv' , 'r') as f:
  #  csv_reader = csv.reader(f)
   # header_row = next(csv_reader)
    #print(header_row)

data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)
#for i in range(len(header_row)):
 #   print(i,':', header_row[i])

#data = data.dropna(subset=['Study_Hours_per_Week', 'Stress_Level (1-10)'])
# Round specific columns to whole numbers
data['Study_Hours_per_Week'] = data['Study_Hours_per_Week'].round()



y = data['Study_Hours_per_Week']
x = data['Stress_Level (1-10)']
data_aggregated = data.groupby('Study_Hours_per_Week')['Stress_Level (1-10)'].mean().reset_index()

plt.scatter(data_aggregated['Stress_Level (1-10)'], data_aggregated['Study_Hours_per_Week'], color='blue', alpha=0.7, s=50)

plt.xlabel('stress levels')
plt.ylabel('study hours ')
plt.title('title')

plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.xlim(min(x) - 1, max(x) + 1)
#x = [4, 6, 8, 10, 12, 14, 16, 18, 20]
#y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



plt.legend()
plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)


plt.show()