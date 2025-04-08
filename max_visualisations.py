import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

def max_visulisation_one():
    # load data:
    data = load_data()
    # print(data)
    print(data.head())

max_visulisation_one()