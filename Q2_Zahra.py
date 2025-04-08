import csv
import pandas as pd
import matplotlib.pyplot as plt


# Read the data
data = pd.read_csv("Students_Grading_Dataset.csv")
print(data)

data['Final_Score'] = data['Final_Score'].round()

plt.figure(figsize=(10, 6))
plt.plot(age, final_grade, marker='o', linestyle='--' , color='green') 

plt.title('Age vs Final Grade') 
plt.xlabel('Age')
plt.ylabel('Final Grade')

plt.grid(True)
plt.tight_layout()
plt.show()

