import csv
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def Oliva_Visualisation_One():
    data = load_data()
    print(data)

    df = pd.DataFrame(data)

    data['Sleep_Hours_per_Night'] = data['Sleep_Hours_per_Night'].round()
    data['Study_Hours_per_Week'] = data['Study_Hours_per_Week'].round()
    data['Stress_Level (1-10)'] = data['Stress_Level (1-10)'].round()
    mean_study_hours_Sleep = df.groupby('Sleep_Hours_per_Night')['Study_Hours_per_Week'].mean().reset_index()
    mean_study_hours_Stress = df.groupby('Stress_Level (1-10)')['Sleep_Hours_per_Night'].mean().reset_index()

    fig, ax = plt.subplots()
    ax.scatter(mean_study_hours_Sleep['Sleep_Hours_per_Night'], mean_study_hours_Sleep['Study_Hours_per_Week'], label ='sleep hours', color= 'blue')

    ax.grid(True)
    ax.set_xticks(range(1, 11))
    ax.set_yticks(range(1, 30))
    ax.set_ylabel(' avg study hours per week')
    ax.set_xlabel(' sleep hours per night')
    ax.set_title('Do students who sleep less and stress more also study more?', size = 9)

    ax1= ax.twinx()
    ax1.scatter(mean_study_hours_Stress['Stress_Level (1-10)'], mean_study_hours_Stress['Sleep_Hours_per_Night'], label='stress level', color ='red')

    ax1.set_ylabel("student stress level")
    ax1.set_yticks(range(1,11))
    ax.legend(loc='upper left')
    ax1.legend(loc = 'upper right')

    plt.show()

if __name__ == "__main__":
    Oliva_Visualisation_One()

