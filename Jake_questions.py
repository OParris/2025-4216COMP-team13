import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data_loader import load_data
data =load_data() # Variable created to store data held in load_data function

#Visualisation one - Does having internet access at home impact the students stress levels? 
# Does the internet access have an impact on the grade the student has received? 
def jake_visualisation_one(): # Funcion created for visualisation one

    # Methods used to format, extract and group the data by access of internet at home
    no_access = data[data['Internet_Access_at_Home'].str.strip().str.lower()=='no']
    with_access = data[data['Internet_Access_at_Home'].str.strip().str.lower()=='yes']

    # Average stress level and most frequent grade calculated and grouped
    with_access_avg = with_access['Stress_Level (1-10)'].mean()
    no_access_avg = no_access['Stress_Level (1-10)'].mean()
    with_internet_grade = with_access['Grade'].mode()[0]
    no_internet_grade = no_access['Grade'].mode()[0]
    
    # Variables printed to test the extracted data and ensure it is the appropriate format
    print(f"Students without internet access is: {len(no_access)}")
    print(f"The average stress level of students with internet access is: {with_access_avg:.2f}")
    print(f"The average stress level of students without internet access is: {no_access_avg:.2f}")
    print(f"The average grade of students with internet access is: {with_internet_grade}")
    print(f"The average grade of students without internet access is: {no_internet_grade}")

    # Creation of the visualisation boxplot, size and colour setting. Axis set to extract the data from "data" 
    # no need to use the created variable groups in this instance (benefit of Seaborn boxplot)
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Internet_Access_at_Home', y='Stress_Level (1-10)', data=data, hue='Internet_Access_at_Home', palette='coolwarm', legend=False)

    # Annotation of the boxplot using the variable groups created to add clarity to the data shown in the boxplot 
    plt.text(0, with_access_avg, f'Avg Stress: {with_access_avg:.2f}',horizontalalignment='center', color='black',fontweight='bold')
    plt.text(1, no_access_avg, f'Avg Stress: {no_access_avg:.2f}',horizontalalignment='center', color='black',fontweight='bold')

    plt.text(0, with_access_avg +0.5, f'Most frequent grade: {with_internet_grade}',horizontalalignment='center', color='black',fontweight='bold')
    plt.text(1, no_access_avg +0.5, f'Most frequent grade: {no_internet_grade}',horizontalalignment='center', color='black',fontweight='bold')

    # Annotation of the axis and print the visualisation
    plt.title('Stress Level Distribution: With vs Without internet access')
    plt.xlabel('Internet access')
    plt.ylabel('Stress level')
    plt.tight_layout()
    plt.show()

# End of function one - required to show visualisation and print to console
if __name__ == "__main__":
    jake_visualisation_one()

# Visualisation two - Do students over 21 have higher stress levels than students 21 or under? 
# Do students over 21 have a higher most frequent grade than students 21 or under? 
def jake_visualisation_two(): # Function created for visualisation two

    # Methods used to extract and group data by age
    over_21= data[data['Age'] >21]
    under_21 = data[data['Age'] <=21]

    # Average stress level and most frequent grade calculated using methods and grouped into variables
    under_21_stress = under_21['Stress_Level (1-10)'].mean()
    over_21_stress = over_21['Stress_Level (1-10)'].mean()
    under_21_grades = under_21['Grade'].mode()[0]
    over_21_grades = over_21['Grade'].mode()[0]

    # Variables printed to test the extracted data and ensure it is the appropriate format
    print(f"Students 21 or under: {len(under_21)}")
    print(f"Average stress level of students 21 or under: {under_21_stress:.2f}")
    print(f'The average grade for studnets 21 or under: {under_21_grades}')
    print(f"Students over 21: {len(over_21)}")
    print(f"Average stress level of students over 21: {over_21_stress:.2f}")
    print(f'The average grade for studnets over 21: {over_21_grades}')

    # Creation of bar chart comparing stress levels and frequent grade by age
    labels = ['21 or under ', 'over 21']
    bar_width = 0.35
    index = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(10, 6))

    # Annotation of bars with stress level and grade, format bars and annotation with colour and font
    ax.bar(index[0], under_21_stress, bar_width, label ='21 or under', color = 'skyblue')
    ax.bar(index[1], over_21_stress, bar_width, label ='Over 21', color = 'limegreen')
    ax.text(index[0], under_21_stress +0.1, f'Most frequent grade for this group: {under_21_grades}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[0], under_21_stress -1, f'{under_21_stress:.2f}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[1], over_21_stress -1, f'{over_21_stress:.2f}', ha='center', color='black', fontweight = 'bold')
    ax.text(index[1], over_21_stress +0.1, f'Most frequent grade for this group: {over_21_grades}', ha='center', color='black', fontweight = 'bold')

    # Annotate labels and show chart
    ax.set_xlabel('Group')
    ax.set_ylabel('Stress Level')
    ax.set_title('Average Stress Levels & Most Frequent Grade: 21 or Under vs Over 21')
    ax.set_xticks(index)
    ax.set_xticklabels(labels)
    ax.set_ylim(0,6)
    ax.legend()
    plt.tight_layout()
    plt.show()


#End of visualisation two function - show print statements in console and generate visualation
if __name__ == "__main__":
    jake_visualisation_two()

# Visualisation three - What are the three most chosen subjects by male and female students? 
# If the three most chosen subjects are the same, do male or female students achieve a higher average total score in these subjects? 
def jake_visualisation_three(): # Creation of function three 

    # Methods used to extract, format and create two variable groups to seperate male and female 
    male_data = data[data['Gender'].str.lower() == 'male']
    female_data = data[data['Gender'].str.lower() == 'female']

    # Variable groups created to extract top three subjects by gender
    top_3_male = male_data['Department'].value_counts().head(3).index
    top_3_female = female_data['Department'].value_counts().head(3).index

    #Variables printed to test the format of this data and check the results to decide the next action
    print("Top 3 most chosen subjects by males:", list(top_3_male))
    print("Top 3 most chosen subjects by females:", list(top_3_female))

    # Variable created to group top 3 subjects as previous print statement showed they are the same
    common_departments = list(set(top_3_male).intersection(set(top_3_female)))

    # Filter data to only include those common departments
    common_data = data[data['Department'].isin(common_departments)]

    # Group by gender and department and calculate the average total score
    avg_scores = common_data.groupby(['Gender', 'Department'])['Total_Score'].mean().reset_index()

    # Print this data to test its format
    print(f"Common subjects in both lists: {common_departments}")
    print(f"Average scores in common departments: {avg_scores}")

    # Create the barplot
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=avg_scores, x='Department', y='Total_Score', hue='Gender', palette='Set2')

    # For loop created to annotate each bar providing clarity into what the barplot is showing
    for p in ax.patches:
        height = p.get_height()
        if height >0:
            ax.annotate(f'{height:.2f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', color='black', fontweight='bold')
        
    # Annotate the title and axis
    plt.title('Average Total Score by Gender in Shared Top 3 Departments')
    plt.xlabel('Department')
    plt.ylabel('Average Total Score')
    plt.xticks(rotation=45) # Rotation of the x axis as there was a slight overlap previously
    plt.tight_layout() # Slight spacing added to prevent overlapping 
    plt.show()

# #End of visualisation three function - show print statements in console and generate visualation
if __name__ == "__main__":
    jake_visualisation_three()
    