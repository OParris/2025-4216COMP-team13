import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Students_Grading_Dataset.csv")

data['Final_Score'] = data['Final_Score'].round()
data['Internet_Access_at_Home'] = data['Internet_Access_at_Home']
df = pd.DataFrame(data)

fig, ax = plt.subplots()

plt.bar(data['Final_Score'], data['Internet_Access_at_Home'])

plt.xlabel('Final Score')
plt.ylabel('Internet Access from home')
plt.title('Students that have internet access from home.')

plt.legend()
plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
plt.show()
