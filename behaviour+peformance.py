import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)

df = pd.DataFrame(data)

data['Sleep_Hours_per_Night'] = data['Sleep_Hours_per_Night'].round()
data['Study_Hours_per_Week'] = data['Study_Hours_per_Week'].round()
data['Stress_Level (1-10)'] = data['Stress_Level (1-10)'].round()
mean_study_hours_Sleep = df.groupby('Sleep_Hours_per_Night')['Study_Hours_per_Week'].mean().reset_index()
mean_study_hours_Stress = df.groupby('Stress_Level (1-10)')['Study_Hours_per_Week'].mean().reset_index()

fig, ax = plt.subplots()
ax.scatter(mean_study_hours_Sleep['Sleep_Hours_per_Night'], mean_study_hours_Sleep['Study_Hours_per_Week'])

ax.grid(True)
ax.set_xticks(range(1, 9))
ax.set_yticks(range(1, 30))
ax.set_ylabel(' avg study hours per week')
ax.set_xlabel(' sleep hours per night')

ax1= ax.twinx()
ax1.scatter(mean_study_hours_Stress['Stress_Level (1-10)'], mean_study_hours_Stress['Study_Hours_per_Week'], color ='red')

ax.set_ylabel("avg study hours a week for sleep")

plt.show()

