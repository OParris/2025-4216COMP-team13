import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data  # your custom data loader

def Zahra_Visualisation_One():
    data = load_data()
    data = data.dropna(subset=['Age', 'Grade'])
    
    plt.figure(figsize=(12, 6))

    sns.boxplot(
        x='Grade',
        y='Age',
        data=data,
        order=['A', 'B', 'C', 'D', 'E', 'F'],
        palette='Pastel1'
    )
    plt.title('Age Distribution by Grade (Box Plot)')
    plt.xlabel('Grade')
    plt.ylabel('Age')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    Zahra_Visualisation_One()