import tkinter as tk
from tkinter import *
import buttons 



# Creates the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x400") # Set window size (width x height)

# adds a frame for the buttons
frame1 = tk.Frame(root, background='lightblue')
frame1.pack(side="top", expand=True, fill=BOTH)


# Configure frame2's grid to expand evenly
for r in range(6):      # however many rows 
    frame1.rowconfigure(r, weight=1)

for c in range(8):      # however many columns
    frame1.columnconfigure(c, weight=1)


"""
# This is a template for adding labels 
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20) # Center the label with padding
"""

# Shows where to puts the buttons
buttons.init(frame1)

# Adds all of the buttons and their places
buttons.all_buttons()

# Packs all of the buttons for use 
buttons.place_buttons()

# Run the application
root.mainloop()
