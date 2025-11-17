import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from ButtonFunctions import *

# TEST COMMIT CHANGE

# variables defined so they can be global
button_color = "lightgray"

root = None

button0 = None
button_period = None
button_enter= None
button_addition = None
button_expressions = None

button1 = None
button2 = None
button3 = None
button_subtraction = None

button4 = None
button5 = None
button6 = None
button_multiplication = None
button_update = None

button7 = None
button8 = None
button9 = None
button_division = None



# this sets the frame to everything in the file for the buttons
def init(main_frame):
    global root
    root = main_frame  # use the root created in main.py 


def all_buttons():

    # makes the buttons global so I can use them in place
    global button0
    global button_period
    global button_enter
    global button_addition
    global button_expressions

    global button1
    global button2
    global button3
    global button_subtraction

    global button4
    global button5
    global button6
    global button_multiplication
    global button_update

    global button7
    global button8
    global button9
    global button_division
    

    global Themes
    global opt
    global lbl

    def show():  
        lbl.config(text=opt.get())  

    # Dropdown options  
    Themes = ["Default", "Light Blue"]  

    opt = StringVar(value="Default")

    lbl = Label(root, text="Default", bg="lightgray")  
    
    

    # makes the buttons and adds text, and a print saying that the person had pressed the button
    button0 = tk.Button(root, text="0", background=button_color, command=lambda: print("Pressed 0"))
    button_period = tk.Button(root, text=".", background=button_color, command=lambda: print("Pressed ."))
    button_enter = tk.Button(root, text="↵", background=button_color, command=lambda: print("Pressed enter"))
    button_addition = tk.Button(root, text="+", background=button_color, command=lambda: print("Pressed +"))
    button_expressions = tk.Button(root, text="Expressions", background=button_color, command=lambda: print("Pressed Expression"))

    button1 = tk.Button(root, text="1", background=button_color, command=lambda: print("Pressed 1"))
    button2 = tk.Button(root, text="2", background=button_color, command=lambda: print("Pressed 2"))
    button3 = tk.Button(root, text="3", background=button_color, command=lambda: print("Pressed 3"))
    button_subtraction = tk.Button(root, text="-", background=button_color, command=lambda: print("Pressed -"))

    button4 = tk.Button(root, text="4", background=button_color, command=lambda: print("Pressed 4"))
    button5 = tk.Button(root, text="5", background=button_color, command=lambda: print("Pressed 5"))
    button6 = tk.Button(root, text="6", background=button_color, command=lambda: print("Pressed 6"))
    button_multiplication = tk.Button(root, text="×", background=button_color, command=lambda: print("Pressed ×"))
    button_update = tk.Button(root, text="Update", background=button_color, command=show)

    button7 = tk.Button(root, text="7", background=button_color, command=lambda: print("Pressed 7"))
    button8 = tk.Button(root, text="8", background=button_color, command=lambda: print("Pressed 8"))
    button9 = tk.Button(root, text="9", background=button_color, command=lambda: print("Pressed 9"))
    button_division = tk.Button(root, text="÷", background=button_color, command=lambda: print("Pressed ÷"))
    

    


def place_buttons():
    # places the position of the button
    button0.grid(row=5, column=0, sticky="nsew", columnspan=2)
    button_period.grid(row=5, column=2, sticky="nsew", columnspan=2)
    button_enter.grid(row=5, column=4, sticky="nsew", columnspan=2)
    button_addition.grid(row=5, column=6, sticky="nsew", columnspan=2)
    button_expressions.grid(row=5, column=8, sticky="nsew", columnspan=2)


    button1.grid(row=4, column=0, sticky="nsew", columnspan=2)
    button2.grid(row=4, column=2, sticky="nsew", columnspan=2)
    button3.grid(row=4, column=4, sticky="nsew", columnspan=2)
    button_subtraction.grid(row=4, column=6, sticky="nsew", columnspan=2)
    lbl.grid(row=4, column=8, sticky="nsew", columnspan=2, )

    button4.grid(row=3, column=0, sticky="nsew", columnspan=2)
    button5.grid(row=3, column=2, sticky="nsew", columnspan=2)
    button6.grid(row=3, column=4, sticky="nsew", columnspan=2)
    button_multiplication.grid(row=3, column=6, sticky="nswew", columnspan=2)
    button_update.grid(row=3, column=8, sticky="nswew", columnspan=2)
    

    button7.grid(row=2, column=0, sticky="nsew", columnspan=2)
    button8.grid(row=2, column=2, sticky="nsew", columnspan=2)
    button9.grid(row=2, column=4, sticky="nsew", columnspan=2)
    button_division.grid(row=2, column=6, sticky="nsew", columnspan=2)
   

    # Makes it aligned to the grid and changes the color of the dropdown (AI helped with this)
    dropdown = OptionMenu(root, opt, *Themes)
    dropdown.grid(row=2, column=8, sticky="nsew", columnspan=2)  # Dropdown menu 
    dropdown.config(bg="lightgray")  
    

 