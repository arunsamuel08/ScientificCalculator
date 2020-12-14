# importing modules
import tkinter as tk
#from tkinter import messagebox
#import math as m

class CalculatorWindow:
    def __init__(self, master):
        self.master = master
        # adding title name
        master.title('Scientific Calculator')
        # setting the size 
        master.geometry('500x500+0+0')
        # disabling the resizing of the window
        master.resizable(0,0)
        # giving background colour
        master.configure(background = "black")

        


if __name__ == '__main__':
    master = tk.Tk()
    app = CalculatorWindow(master)
    master.mainloop()
    
