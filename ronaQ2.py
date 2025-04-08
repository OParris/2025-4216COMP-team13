import matplotlib.pyplot as plt
import csv
import pandas as pd
from data_loader import load_data

def Rona_Visualisation_Two():
    data = load_data()
    data = pd.read_csv("Students_Grading_Dataset.csv")

    df = pd.DataFrame(data)


    data['Final_Score'] = data['Final_Score'].round()
    data['Midterm_Score'] = data['Midterm_Score'].round()
    data['Student_ID']= data['Student_ID']


    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 6))

    data = data.head(16)

    left.bar(data['Student_ID'], data['Midterm_Score'])
    left.set_xlabel('Student', size = 6)
    left.set_ylabel('Midterm Scores')
    left.set_title('Comparing Midterm Scores To Final Scores', size = 9)
    left.tick_params(axis='x', rotation =45)


    right.bar(data['Student_ID'], data['Final_Score'])
    right.set_xlabel('Student', size = 6)
    right.set_ylabel('Final Scores')
    right.set_title('Comparing Midterm Scores To Final Scores', size = 9)
    right.tick_params(axis='x', rotation =45)



    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    Rona_Visualisation_Two()