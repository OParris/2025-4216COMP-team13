import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
from data_loader import load_data

data = load_data()

# group data by extracurricular or not:
group_extrac = data[data['Extracurricular_Activities'] == 'Yes']
group_noextrac = data[data['Extracurricular_Activities'] == 'No']

# avg study hours for each group:
avg_study_extrac = group_extrac['Study_Hours_per_Week'].mean()
avg_study_noextrac = group_noextrac['Study_Hours_per_Week'].mean()
    
# avg score for each group:
avg_score_extrac = group_extrac['Total_Score'].mean()
avg_score_noextrac = group_noextrac['Total_Score'].mean()



def max_visualisation_two():

    #Visualization 1:
    print("Average Study Hours per Week:")
    print(f"  Extracurricular: {avg_study_extrac:.2f}")
    print(f"  No Extracurricular: {avg_study_noextrac:.2f}")
    print("Average Total Score:")
    print(f"  Extracurricular: {avg_score_extrac:.2f}")
    print(f"  No Extracurricular: {avg_score_noextrac:.2f}")

    # Create a figure with two subplots: one for study hours, one for total scores.
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Bar chart for average study hours
    axes[0].bar(['Extracurricular', 'No Extracurricular'],
                [avg_study_extrac, avg_study_noextrac],
                color=['lightsteelblue', 'plum'])
    axes[0].set_title("Average Study Hours per Week")
    axes[0].set_ylabel("Study Hours")

    # Bar chart for average total score
    axes[1].bar(['Extracurricular', 'No Extracurricular'],
                [avg_score_extrac, avg_score_noextrac],
                color=['cadetblue', 'tomato'])
    axes[1].set_title("Average Total Score")
    axes[1].set_ylabel("Total Score")

    plt.tight_layout()
    plt.show()


def max_visualisation_three():

 
    #Visualization 2:

    # Do students with same study hours but no extracurricular activities achieve higher or lower scores

    # avg total score of extracurricular group by study hours:
    group_extrac_by_hours = group_extrac.groupby('Study_Hours_per_Week')['Total_Score'].mean().reset_index()

    # avg total score of non-extracurricular group by study hours
    group_noextrac_by_hours = group_noextrac.groupby('Study_Hours_per_Week')['Total_Score'].mean().reset_index()

    
    plt.figure(figsize=(10, 6))
    plt.plot(group_extrac_by_hours['Study_Hours_per_Week'],
             group_extrac_by_hours['Total_Score'],
             marker='o',color='turquoise', label='Extracurricular', linestyle="none")
    plt.plot(group_noextrac_by_hours['Study_Hours_per_Week'],
             group_noextrac_by_hours['Total_Score'],
             marker='o', color='violet', label='No Extracurricular', linestyle="none")
    plt.xlabel("Study Hours per Week")
    plt.ylabel("Average Total Score")
    plt.title("Total Score vs. Study Hours (by Extracurricular Participation)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    max_visualisation_two()

if __name__ == "__main__":
    max_visualisation_three()




