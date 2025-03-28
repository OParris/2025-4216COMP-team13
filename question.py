import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)
data['Attendance (%)'] = data['Midterm_Score'].round()

y = data['Attendance_per_week']
x = data['Final_Score']

plt.scatter(data_aggregated['Attendance (%))'], data_aggregated['Midterm_Score'], color='blue', alpha=0.7, s=50)

plt.xlabel('Attendance')
plt.ylabel('Midterm Score')
plt.title('Overall score for students with high attendance.')

plt.legend()
plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
plt.show()