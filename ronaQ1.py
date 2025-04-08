import csv 
import  pandas as pd 
import matplotlib.pyplot as plt 
from data_loader import load_data

def Rona_Visualisation_One():
    data=load_data()
    df = pd.DataFrame(data)

    data['Fmaily_Income_Level'] = data['Family_Income_Level']
    data['Attendance (%)'] = data['Attendance (%)'].mean()

    #== df.groupby('Attendance (%)')['Family_Income_Level'].mean().reset_index()

    fig,ax = plt.subplots() 

    plt.bar(data['Family_Income_Level'],data['Attendance (%)'])

    plt.xlabel('Family income level')
    plt.ylabel('Attendance (%)')
    plt.title('How Family Income Has An Impact On Attendance')
    plt.ylim(0,100)


    plt.show()

if __name__ == "__main__":
    Rona_Visualisation_One()