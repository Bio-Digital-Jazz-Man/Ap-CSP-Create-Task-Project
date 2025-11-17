# This entire file was made from AI
import tkinter as tk
main_frame: tk.Frame = None
extra_frame: tk.Frame = None

# We'll keep references to the main and secondary frames
main_frame = None
extra_frame = None

def init_frame_switching(main, extra):
    """Initialize the main and extra frames"""
    global main_frame, extra_frame
    main_frame = main
    extra_frame = extra

def switch_to_extra():
    """Hide main frame and show extra frame"""
    if main_frame and extra_frame:
        main_frame.pack_forget()
        extra_frame.pack(fill="both", expand=True)

def switch_to_main():
    """Hide extra frame and show main frame"""
    if main_frame and extra_frame:
        extra_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)

def create_extra_buttons():
    """Create buttons in the extra frame that return to main"""
    if extra_frame:
        # Example extra buttons
        btn1 = tk.Button(extra_frame, text="Back to Main", command=switch_to_main)
        btn2 = tk.Button(extra_frame, text="Extra Button 1", command=switch_to_main)
        btn3 = tk.Button(extra_frame, text="Extra Button 2", command=switch_to_main)
        
        # Pack them
        btn1.pack(pady=20)
        btn2.pack(pady=20)
        btn3.pack(pady=20)
