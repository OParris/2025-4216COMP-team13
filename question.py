import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)

data['Attendance (%)'] = data['Midterm_Score'].round()
df = pd.DataFrame(data)

data['Attendance (%)'] = data['Attendance (%)']
data['Midterm_Score'] = data['Midterm_Score']

fig, ax = plt.subplots()
plt.scatter(data_aggregated['Attendance (%)'], data_aggregated['Midterm_Score'], color='blue', alpha=0.7, s=50)

plt.xlabel('Attendance by term')
plt.ylabel('Midterm Score')
plt.title('Overall score for students with high attendance.')

plt.legend()
plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
plt.show()
