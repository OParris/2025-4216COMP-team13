import tkinter as tk
from Q1_Max import max_visualisation_one  
from Q2_Max import max_visualisation_two
from Q2_Max import max_visualisation_three


def run_max_visualisation_one():
    max_visualisation_one()  

def run_max_visualisation_two():
    max_visualisation_two()

def run_max_visualisation_three():
    max_visualisation_three()

root = tk.Tk()
root.title("Team 13 Visualisations")

Maxs_frame = tk.LabelFrame(root, text="Max's Visualisations", labelanchor='n', padx=10, pady=10)
Maxs_frame.pack(padx=10, pady=10, fill="both", expand=True)

# btn_max_vis = tk.Button(group_a_frame, text="Run Max Visualisation", command=run_max_vis)
# btn_max_vis.pack(pady=5)

btn_max_vis_one = tk.Button(Maxs_frame, text="Max Visualisation-One", command=run_max_visualisation_one)
btn_max_vis_one.pack(pady=10)

btn_max_vis_two = tk.Button(Maxs_frame, text="Max Visualisation-Two", command=run_max_visualisation_two)
btn_max_vis_two.pack(pady=10)

btn_max_vis_three = tk.Button(Maxs_frame, text="Max Visualisation-Three", command=run_max_visualisation_three)
btn_max_vis_three.pack(pady=10)

root.mainloop()