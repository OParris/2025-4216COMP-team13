import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data_loader import load_data

def jake_visualisation_one():
    data =load_data()
    no_access = data[data['Internet_Access_at_Home'].str.strip().str.lower()=='no']
    with_access = data[data['Internet_Access_at_Home'].str.strip().str.lower()=='yes']
    with_access_avg = with_access['Stress_Level (1-10)'].mean()
    no_access_avg = no_access['Stress_Level (1-10)'].mean()
    with_internet_grade = with_access['Grade'].mode()[0]
    no_internet_grade = no_access['Grade'].mode()[0]
    with_access_total_score = with_access['Total_Score'].mean()
    no_access_total_score = no_access['Total_Score'].mean()
    
    print(f"Students without internet access is: {len(no_access)}")
    print(f"The average stress level of students with internet access is: {with_access_avg:.2f}")
    print(f"The average stress level of students without internet access is: {no_access_avg:.2f}")
    print(f"The average grade of students with internet access is: {with_internet_grade}")
    print(f"The average grade of students without internet access is: {no_internet_grade}")
    print(f"The average total score for studnets with internet access is: {with_access_total_score:.2f}")
    print(f"The average total score for students without internet access is: {no_access_total_score:.2f}")

    plt.figure(figsize=(10,6))
    sns.boxplot(x='Internet_Access_at_Home', y='Stress_Level (1-10)', data=data, hue='Internet_Access_at_Home', palette='coolwarm', legend=False)

    plt.text(0, with_access_avg, f'Avg Stress: {with_access_avg:.2f}',horizontalalignment='center', color='black',fontweight='bold')
    plt.text(1, no_access_avg, f'Avg Stress: {no_access_avg:.2f}',horizontalalignment='center', color='black',fontweight='bold')

    plt.text(0, with_access_avg +0.5, f'Most frequent grade: {with_internet_grade}',horizontalalignment='center', color='black',fontweight='bold')
    plt.text(1, no_access_avg +0.5, f'Most frequent grade: {no_internet_grade}',horizontalalignment='center', color='black',fontweight='bold')

    plt.title('Stress Level Distribution: With vs Without internet access')
    plt.xlabel('Internet access')
    plt.ylabel('Stress level')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    jake_visualisation_one()

def jake_visualisation_two():
    data = load_data()
    over_21= data[data['Age'] >21]
    under_21 = data[data['Age'] <=21]
    under_21_stress = under_21['Stress_Level (1-10)'].mean()
    over_21_stress = over_21['Stress_Level (1-10)'].mean()
    under_21_grades = under_21['Grade'].mode()[0]
    over_21_grades = over_21['Grade'].mode()[0]

    print(f"Students 21 or under: {len(under_21)}")
    print(f"Average stress level of students 21 or under: {under_21_stress:.2f}")
    print(f'The average grade for studnets 21 or under: {under_21_grades}')
    print(f"Students over 21: {len(over_21)}")
    print(f"Average stress level of students over 21: {over_21_stress:.2f}")
    print(f'The average grade for studnets over 21: {over_21_grades}')

    labels = ['21 or under ', 'over 21']
    bar_width = 0.35
    index = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(index[0], under_21_stress, bar_width, label ='21 or under', color = 'skyblue')
    ax.bar(index[1], over_21_stress, bar_width, label ='Over 21', color = 'limegreen')
    ax.text(index[0], under_21_stress +0.1, f'Most frequent grade for this group: {under_21_grades}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[0], under_21_stress -1, f'{under_21_stress:.2f}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[1], over_21_stress -1, f'{over_21_stress:.2f}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[1], over_21_stress +0.1, f'Most frequent grade for this group: {over_21_grades}', ha='center', color='black', fontweight = 'bold')
    ax.set_xlabel('Group')
    ax.set_ylabel('Stress Level')
    ax.set_title('Average Stress Levels & Most Frequent Grade: 21 or Under vs Over 21')
    ax.set_xticks(index)
    ax.set_xticklabels(labels)
    ax.set_ylim(0,6)
    ax.legend()
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    jake_visualisation_two()

def jake_visualisation_three():
    data = load_data()
    department_gender_score = data.groupby(['Gender', 'Department'])['Total_Score'].mean().reset_index(name='Total_Score')

    top_3_departments = data.groupby('Department').size().sort_values(ascending=False).head(3).index
    filtered_data = department_gender_score[department_gender_score['Department'].isin(top_3_departments)]

    print("Total score for the top 3 subjects by gender: ")
    for _, row in filtered_data.iterrows():
        print(f"Department: {row['Department']}, Gender: {row['Gender']}, Average Total Score: {row['Total_Score']:.2f}")

    plt.figure(figsize=(12, 6))
    ax=sns.barplot(data=filtered_data, x='Department', y='Total_Score', hue='Gender', palette='Set2')

    for p in ax.patches:
        height = p.get_height()
        if height >0:
            ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    xytext=(0, 5),  # Offset the text slightly above the bar
                    textcoords='offset points',
                    ha='center', va='center', color='black', fontweight='bold')
    

    plt.title('Total Score for the Top 3 Subjects by Gender')
    plt.xlabel('Department')
    plt.ylabel('Total Score')
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()

    plt.show()
    

if __name__ == "__main__":
    jake_visualisation_three()
    