import csv
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data


def Oliva_Visualisation_Two():
    data = load_data
    print(data)

    data['Final_Score'] = data['Final_Score'].round()

    fig, axs = plt.subplots(2, 2, figsize=(14,12))


    phd_data = data[data['Parent_Education_Level'] == 'PhD']
    axs[0, 0].boxplot(phd_data['Final_Score'], vert=False, patch_artist=True, boxprops=dict(facecolor='blue', color='black'))
    axs[0, 0].set_title("PhD Against Final Score")
    axs[0, 0].set_xlabel("Final Score")
    axs[0, 0].set_ylabel("Parent Education Level")


    masters_data = data[data['Parent_Education_Level'] == "Master's"]
    axs[0, 1].boxplot(masters_data['Final_Score'],vert=False, patch_artist=True, boxprops=dict(facecolor='green', color='black'))
    axs[0, 1].set_title("Masters Against Final Score")
    axs[0, 1].set_xlabel("Final Score")
    axs[0, 1].set_ylabel("Parent Education Level")


    bachelors_data = data[data['Parent_Education_Level'] == "Bachelor's"]
    axs[1, 0].boxplot(bachelors_data['Final_Score'], vert=False, patch_artist=True, boxprops=dict(facecolor='red', color='black'))
    axs[1, 0].set_title("Bachelors Against Final Score")
    axs[1, 0].set_xlabel("Final Score")
    axs[1, 0].set_ylabel("Parent Education Level")


    highschool_data = data[data['Parent_Education_Level'] == 'High School']
    axs[1, 1].boxplot(highschool_data['Final_Score'], vert=False, patch_artist=True, boxprops=dict(facecolor='purple', color='black'))
    axs[1, 1].set_title("High School Against Final Score")
    axs[1, 1].set_xlabel("Final Score")
    axs[1, 1].set_ylabel("Parent Education Level")

    for ax in axs.flat:
        ax.grid(True)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    plt.tight_layout()
    plt.show()

