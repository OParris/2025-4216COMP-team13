import csv
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)

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


plt.legend()
plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
plt.show()