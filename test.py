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

fig, (left, right) = plt.subplots(1, 2)

left.scatter(mean_study_hours_Sleep['Sleep_Hours_per_Night'], mean_study_hours_Sleep['Study_Hours_per_Week'], label ='sleep hours', color= 'blue')
left.set_ylabel('study hours per week')
left.set_xlabel('sleep hours per night')



right.scatter(mean_study_hours_Stress['Stress_Level (1-10)'], mean_study_hours_Stress['Study_Hours_per_Week'], label='stress level', color ='red')
right.set_ylabel('study hours per week')
right.set_xlabel('stress levels')
plt.show()