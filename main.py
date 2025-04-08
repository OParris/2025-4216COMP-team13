import tkinter as tk
from Q1_Max import max_visualisation_one
from Jake_questions import jake_visualisation_one
from Jake_questions import jake_visualisation_two
from Jake_questions import jake_visualisation_three
import Q1_Max
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

def run_jake_visualisation_one():
    jake_visualisation_one
btn_jake_vis = tk.Button(root,text="Jake Visualisation-One", command=jake_visualisation_one)
btn_jake_vis.pack(pady=10)

def run_jake_visualisation_two():
    jake_visualisation_two
btn_jake_vis = tk.Button(root,text="Jake Visualisation-Two", command=jake_visualisation_two)
btn_jake_vis.pack(pady=10)

def run_jake_visualisation_three():
    jake_visualisation_three
btn_jake_vis = tk.Button(root,text="Jake Visualisation-Three", command=jake_visualisation_three)
btn_jake_vis.pack(pady=10)

root.mainloop()