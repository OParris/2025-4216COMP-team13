import csv
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def Louisa_Visualisation_One():
    data = load_data
    data = pd.read_csv("Students_Grading_Dataset.csv")
    print(data)

    data['Attendance (%)'] = data['Midterm_Score'].round()
    df = pd.DataFrame(data)

    data['Attendance (%)'] = data['Attendance (%)']
    data['Midterm_Score'] = data['Midterm_Score']

    fig, ax = plt.subplots()
    plt.scatter(data['Attendance (%)'], data['Midterm_Score'], color='blue')

    plt.xlabel('Attendance by term')
    plt.ylabel('Midterm Score')
    plt.title('Overall score for students with high attendance.')

    plt.legend()
    plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
    plt.show()

if __name__ == "__main__":
    Louisa_Visualisation_One()
