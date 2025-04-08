import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data_loader import load_data


def max_visualisation_one():
    # load data:
    data = load_data()
    # print(data)
    # print(data.head())
    
    # group for parent education level bachelor's or above and high income:
    group_A = data[
    (data["Parent_Education_Level"].isin(["Bachelor's", "Master's", "PhD"])) & 
    (data["Family_Income_Level"] == "High")
    ]

    # group for parents education level below bachelor's and low income:
    group_B = data[
        (data["Parent_Education_Level"].isin(["None", "High School"])) &
        (data["Family_Income_Level"] == "Low")
    ]

    print(f"group A:\n {group_A}")
    print(f"group_B:\n {group_B}")

    group_A_Count = group_A["Student_ID"].count()
    print(f"Amount of people in group A: {group_A_Count}")

    group_B_Count = group_B["Student_ID"].count()
    print(f"Amount of people in group B: {group_B_Count}")


    # average total score for each group:
    group_A_avg_total_score = group_A["Total_Score"].mean()
    group_B_avg_total_score = group_B["Total_Score"].mean()

    print(f"Group A (parents bachelor's or above + high income) avg total score: {group_A_avg_total_score}")
    print(f"Group B (parents below bachelor's + low income) avg total score: {group_B_avg_total_score}")

    group_A_avg_stress = group_A["Stress_Level (1-10)"].mean()
    group_B_avg_stress = group_B["Stress_Level (1-10)"].mean()
    print(f"Group A Stress Level: {group_A_avg_stress:.2f}")
    print(f"Group B Stress Level: {group_B_avg_stress:.2f}")

    group_A_avg_sleep = group_A['Sleep_Hours_per_Night'].mean()
    group_B_avg_sleep = group_B['Sleep_Hours_per_Night'].mean()
    print(f"Group A avg sleep: {group_A_avg_sleep:.2f}")
    print(f"Group B avg sleep: {group_B_avg_sleep:.2f}")

    print("Group A (Parents with Bachelor's or above and High Income) Averages:")
    print(f"  Total Score: {group_A_avg_total_score:.2f}")
    print(f"  Stress Level: {group_A_avg_stress:.2f}")
    print(f"  Sleep Hours: {group_A_avg_sleep:.2f}")

    print("\nGroup B (Parents with below Bachelor's and Low Income) Averages:")
    print(f"  Total Score: {group_B_avg_total_score:.2f}")
    print(f"  Stress Level: {group_B_avg_stress:.2f}")
    print(f"  Sleep Hours: {group_B_avg_sleep:.2f}")

    # group data for charts:
    metrics = ['Total Score', 'Stress Level', 'Sleep Hours']
    group_A_means = [group_A_avg_total_score, group_A_avg_stress, group_A_avg_sleep]
    group_B_means = [group_B_avg_total_score, group_B_avg_stress, group_B_avg_sleep]

    
    x = np.arange(len(metrics))  
    width = 0.35  
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, group_A_means, width, label="Student's: parents educated to bachelor's or above and high income")
    rects2 = ax.bar(x + width/2, group_B_means, width, label="Student's: parents educated below bachelor's and low income")
    
    # Set labels and title
    ax.set_ylabel('Average Values')
    ax.set_title('Comparison between Group A and Group B')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    # Function to attach value labels to each bar
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.1f}',
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        # offset above the bar
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)

    ax.plot()
    plt.show()
  
    


if __name__ == "__main__":
    max_visualisation_one()