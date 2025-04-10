import pandas as pd

def load_data():
    data = pd.read_csv('Students_Grading_Dataset.csv')

    # print(data)
    return data


load_data()

