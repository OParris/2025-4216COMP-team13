import csv
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)

data['Study_Hours_per_Week'] = data['Study_Hours_per_Week'].round()
data['Sleep_Hours_per_Night'] = data['Sleep_Hours_per_Night'].round()



y = data['Study_Hours_per_Week']
x = data['Stress_Level (1-10)']
x2 = data['Sleep_Hours_per_Night']
data_aggregated = data.groupby('Study_Hours_per_Week')['Stress_Level (1-10)'].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(10,6))

ax1.plot(x, y, color='blue', label='Stress_Level (1-10)')
ax1.set_xlabel('Stress_Level (1-10)')
ax1.set_ylabel('Study_Hours_per_Week')
ax1.legend(loc='upper left')

ax2 = ax1.twiny()
ax2.plot(x2, y, color='red', label='sleep hours')
ax2.set_ylabel('study hours')
ax1.legend(loc='upper right')

#plt.scatter(data_aggregated['Stress_Level (1-10)'], data_aggregated['Study_Hours_per_Week'], color='blue', alpha=0.7, s=50)

#plt.xlabel('stress levels')
#plt.ylabel('study hours ')
#plt.title('title')

plt.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.xlim(min(x) - 1, max(x) + 1)

ax1.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
ax1.grid(True, axis= 'x', linestyle='--', alpha= 0.7)

ax1.set_xlim(min(x) - 1, max(x) + 1)
ax2.set_xlim(min(x2) - 1, max(x2) + 1)

plt.tight_layout()
plt.show()