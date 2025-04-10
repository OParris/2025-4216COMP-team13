import csv
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def Louisa_Visualisation_Two():
    data = load_data()

    df = pd.DataFrame(data)

    data['Final_Score'] = data['Final_Score'].mean()
    data['Internet_Access_at_Home'] = data['Internet_Access_at_Home']

    Mean_Final_Score = df.groupby('Internet_Access_at_Home')['Final_Score'].mean().reset_index()

    fig, ax = plt.subplots()

    plt.bar(Mean_Final_Score['Internet_Access_at_Home'], Mean_Final_Score['Final_Score'])

    plt.xlabel('Internet access from home')
    plt.ylabel('Final score')
    plt.title('Students that have internet access from home.')
    ax.set_yticks(range(0, 100, 10))

    plt.legend()
    plt.grid(True, axis= 'y', linestyle='--', alpha= 0.7)
    plt.show()

if __name__ == "__main__":
    Louisa_Visualisation_Two()
