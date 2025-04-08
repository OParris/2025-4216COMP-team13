import matplotlib.pyplot as plt
import csv
import pandas as pd

data = pd.read_csv("Students_Grading_Dataset.csv")

df = pd.DataFrame(data)


data['Final_Score'] = data['Final_Score'].round()
data['Midterm_Score'] = data['Midterm_Score'].round()
data['Student_ID']= data['Student_ID']


fig, (left, right) = plt.subplots(1, 2, figsize=(12, 6))

data = data.head(16)

left.bar(data['Student_ID'], data['Midterm_Score'])
left.set_xlabel('Students', size = 6)
left.set_ylabel(' midterm Scores')
left.set_title('Comparing Midterm_Scores To Final_Scores', size = 9)
left.tick_params(axis='x', rotation =45)


right.bar(data['Student_ID'], data['Final_Score'])
right.set_xlabel('Students', size = 6)
right.set_ylabel('Scores')
right.set_title('Comparing Midterm_Scores To Final_Scores', size = 9)
right.tick_params(axis='x', rotation =45)



plt.tight_layout()
plt.show()