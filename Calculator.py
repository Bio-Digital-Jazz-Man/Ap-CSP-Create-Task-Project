import tkinter as tk
from tkinter import *
import Buttons
from Buttons import *
from ButtonFunctions import init_frame_switching, switch_to_extra, switch_to_main, create_extra_buttons
import json 
import sys


with open("themes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)


# Creates the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x400") # Set window size (width x height)

# adds a frame for the buttons
frame1 = tk.Frame(root, background='white')
frame1.pack(side="top", expand=True, fill="both")
frame2 = tk.Frame(root, background='white')


# Configure frame1's grid to expand evenly
for r in range(6):      # however many rows 
    frame1.rowconfigure(r, weight=1)
    frame2.rowconfigure(r, weight=1)

for c in range(10):      # however many columns
    frame1.columnconfigure(c, weight=1)
    frame2.columnconfigure(c, weight=1)



"""
# This is a template for adding labels 
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20) # Center the label with padding
"""

# Shows where to puts the buttons
Buttons.init(frame1)

# Adds all of the buttons and their places
Buttons.all_buttons()

# Packs all of the buttons for use 
Buttons.place_buttons()

# Initialize extra screen (from AI)
init_frame_switching(frame1, frame2)
create_extra_buttons()

# Connect the expressions button to open extra screen (from AI)
Buttons.button_expressions.config(command=switch_to_extra)

# Run the application
root.mainloop()
