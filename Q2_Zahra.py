import csv
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def Zahra_Visualisation_Two():
    data = load_data()

    data['Study_Hours_per_Week'] = data['Final_Score'].round()
    df = pd.DataFrame(data)

    data['Study_Hours_per_Week'] = data['Study_Hours_per_Week']
    data['Final_Score'] = data['Final_Score']

    fig, ax = plt.subplots()
    plt.scatter(data['Study_Hours_per_Week'], data['Final_Score'], color='blue')

    plt.xlabel('Hours studied per week')
    plt.ylabel('Final Score')
    plt.title('Overall score for students with most hours studied per week.')

    plt.legend()
    plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
    plt.show()

if __name__ == "__main__":
    Zahra_Visualisation_Two()