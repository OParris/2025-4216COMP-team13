import tkinter as tk
from Q1_Max import max_visualisation_one  

# from data_loader import load_data

# load_data()

def run_max_visualisation():
    max_visualisation_one()  
    # load_data()

root = tk.Tk()
root.title("Team 13 Visualisations")

btn_max_vis = tk.Button(root, text="Max Visualisation-One", command=run_max_visualisation)
btn_max_vis.pack(pady=10)

root.mainloop()