import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import load_data

def Gemma_Visualisation_Two():
    
        np.random.seed(42)
        num_students = 100

        data = {
        'Participation_Score': np.random.uniform(0, 100, num_students),
        'Assignments_Avg': np.random.uniform(50, 100, num_students) + np.random.normal(0, 5, num_students),
        'Department': np.random.choice(['CS', 'Engineering', 'Business', 'Math', 'Biology'], size=num_students)
        }

        df = pd.DataFrame(data)

        sns.lmplot(
        data=df,
        x='Participation_Score',
        y='Assignments_Avg',
        hue='Department',
        aspect=1.5,
        height=6,
        scatter_kws={'alpha': 0.6},
        line_kws={'linewidth': 2}
        )

        plt.title('Participation vs Assignment Average by Department')
        plt.xlabel('Participation Score')
        plt.ylabel('Assignment Average')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    Gemma_Visualisation_Two()