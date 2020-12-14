# importing modules
from tkinter import*
#from tkinter import messagebox
#import math as m

class CalculatorWindow:
    def __init__(self, master):
        self.master = master
        # adding title name
        master.title('Scientific Calculator')
        # setting the size 
        master.geometry('480x568+0+0')
        # disabling the resizing of the window
        master.resizable(0,0)
        # giving background colour
        master.configure(background = "black")
        
        # adding frame to the calculator 
        calc = Frame(master)
        calc.grid()

        # making menus
        menubar = Menu(calc)

        # added file menu in which we will toggle between the two calcs
        filemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu=filemenu)
        # added the toggle button for standard calc 
        filemenu.add_command(label = "Standard")
        # added the toggle button for scientific calc
        filemenu.add_command(label = "Scientific")
        # added in a separator
        filemenu.add_separator()
        # added a exit option.
        filemenu.add_command(label = "Exit")

        # command used to call this file menu
        master.config(menu=menubar)

        # adding an edit menu from which we can cut, copy or paste
        editmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit", menu=editmenu)
        # added button for cut, copy and past
        editmenu.add_command(label = "Cut")
        editmenu.add_command(label = "Copy")
        editmenu.add_command(label = "Paste")

        # command to call this edit menu
        master.config(menu=menubar)
        # added a button to view help
        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "Help", menu=helpmenu)
        helpmenu.add_command(label = "View Help")

        master.config(menu=menubar)

        



if __name__ == '__main__':
    master = Tk()
    app = CalculatorWindow(master)
    master.mainloop()
    
