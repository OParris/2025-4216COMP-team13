import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data 

def Gemma_Visualisation_One():
    df = load_data()

    avg_quiz_by_dept = df.groupby('Department')['Quizzes_Avg'].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    avg_quiz_by_dept.plot(kind='bar', color='skyblue')

    plt.title('Average Quiz Scores by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Quiz Scores')
    plt.axhline(df['Quizzes_Avg'].mean(), color='red', linestyle='--', label='Overall Average')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    Gemma_Visualisation_One()
