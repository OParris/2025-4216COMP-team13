import pandas as pd

def load_data():
    data = pd.read_csv("Students_Grading_Dataset.csv")

    data['Study_Hours_per_Week'] = data['Study_Hours_per_Week'].round()
    return data

