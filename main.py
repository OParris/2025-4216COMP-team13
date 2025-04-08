import tkinter as tk
from Q1_Max import max_visualisation_one
from Jake_questions import jake_visualisation_one
from Jake_questions import jake_visualisation_two
from Jake_questions import jake_visualisation_three
from Q1_Max import max_visualisation_one  
from Q2_Max import max_visualisation_two
from Q2_Max import max_visualisation_three
from OliviaQ1 import Oliva_Visualisation_One
from OliviaQ2 import Oliva_Visualisation_Two
from Q1_Louisa import Louisa_Visualisation_One
from Q2_Louisa import Louisa_Visualisation_Two

# Max's Imported Visualisation Functions:
def run_max_visualisation_one():
    max_visualisation_one()  

def run_max_visualisation_two():
    max_visualisation_two()

def run_max_visualisation_three():
    max_visualisation_three()

# Jake's Imported Visualisation Functions:
def run_jake_visualisation_one():
    jake_visualisation_one()

def run_jake_visualisation_two():
    jake_visualisation_two()

def run_jake_visualisation_three():
    jake_visualisation_three()

# Olivia's Imported Visualisation Functions:
def run_olivia_visualisation_one():
    Oliva_Visualisation_One()

def run_olivia_visualisation_two():
    Oliva_Visualisation_Two()

# Louisa's Imported Visualisation Functions:
def run_louisa_visualisation_one():
    Louisa_Visualisation_One()

def run_louisa_visualisation_two():
    Louisa_Visualisation_Two()

# Menu title / header
root = tk.Tk()
root.title("Team 13 Visualisations")

# Frames to group each persons visualisations:

# Max's Frame:
Maxs_frame = tk.LabelFrame(root, text="Max's Visualisations", labelanchor='n', padx=10, pady=10)
Maxs_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Jake's Frame:
Jakes_frame = tk.LabelFrame(root, text="Jake's Visualisations", labelanchor='n', padx=10, pady=10)
Jakes_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Olivia's Frame:
Olivias_frame = tk.LabelFrame(root, text="Olivia's Visualisations", labelanchor='n', padx=10, pady=10)
Olivias_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Louisa's Frame:
Louisas_frame = tk.LabelFrame(root, text="Louisa's Visualisations", labelanchor='n', padx=10, pady=10)
Louisas_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Buttons in each persons frames to run their visualisations:

# Max's buttons:
btn_max_vis_one = tk.Button(Maxs_frame, text="Max Visualisation-One", command=run_max_visualisation_one)
btn_max_vis_one.pack(pady=10)

btn_max_vis_two = tk.Button(Maxs_frame, text="Max Visualisation-Two", command=run_max_visualisation_two)
btn_max_vis_two.pack(pady=10)

btn_max_vis_three = tk.Button(Maxs_frame, text="Max Visualisation-Three", command=run_max_visualisation_three)
btn_max_vis_three.pack(pady=10)

# Jake's Buttons:
btn_jake_vis_one = tk.Button(Jakes_frame,text="Jake Visualisation-One", command=jake_visualisation_one)
btn_jake_vis_one.pack(pady=10)

btn_jake_vis_two = tk.Button(Jakes_frame,text="Jake Visualisation-Two", command=jake_visualisation_two)
btn_jake_vis_two.pack(pady=10)

btn_jake_vis_three = tk.Button(Jakes_frame,text="Jake Visualisation-Three", command=jake_visualisation_three)
btn_jake_vis_three.pack(pady=10)

# Olivia's buttons:
btn_olivia_vis_one = tk.Button(Olivias_frame,text="Olivia Visualisation-One", command=Oliva_Visualisation_One)
btn_olivia_vis_one.pack(pady=10)

btn_olivia_vis_two = tk.Button(Olivias_frame,text="Olivia Visualisation-Two", command=Oliva_Visualisation_Two)
btn_olivia_vis_two.pack(pady=10)

# Louisa's buttons:
btn_louisa_vis_one = tk.Button(Louisas_frame,text="Louisa Visualisation-One", command=Louisa_Visualisation_One)
btn_louisa_vis_one.pack(pady=10)

btn_louisa_vis_two = tk.Button(Louisas_frame,text="Louisa Visualisation-Two", command=Louisa_Visualisation_Two)
btn_louisa_vis_two.pack(pady=10)




root.mainloop()