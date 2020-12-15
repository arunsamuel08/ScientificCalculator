# importing modules
from tkinter import*
from tkinter import messagebox
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

        #============================= Menus =================================  
        # class method to add the code to exit the application
        def iExit():
            iExit = messagebox.askyesno("Scientific Calculator", "Do you want to exit?")
            if iExit > 0:
                master.destroy()
                return
        # class method  for the standard button
        def Standard():
            master.resizable(0,0)
            master.geometry("480x568+0+0")
            return

        # class method for scientific button and toggling purpose
        def Scientific():
            master.resizable(0,0)
            master.geometry("944x568+0+0")
            return
    
        # making menus
        menubar = Menu(calc)

        # added file menu in which we will toggle between the two calcs
        filemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu=filemenu)
        # added the toggle button for standard calc 
        filemenu.add_command(label = "Standard", command = Standard)
        # added the toggle button for scientific calc
        filemenu.add_command(label = "Scientific", command = Scientific)
        # added in a separator
        filemenu.add_separator()
        # added a exit option.
        filemenu.add_command(label = "Exit", command = iExit)

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

        # ================================= Display ==================================

        self.input_field = Entry(calc, font = ('arial', 20, 'bold'), bg='#101820',
        bd=30, width=28, justify=RIGHT, fg='#f2aa4c')
        self.input_field.grid(row=0, column=0, pady=1, columnspan=4)
        self.input_field.insert(0, "0")
        
        # ================================ Buttons ====================================

        numberpad = "789456123"
        i = 0
        btn = []
        for j in range (2,5):
            for k in range(3):
                btn.append(Button(calc, width=6, height=2, font = ('arial', 20, 'bold'),
                 bd=4, text = numberpad[i], bg = '#101820', fg='#f2aa4c' ))
                btn[i].grid(row=j , column=k, pady=1)
                i+=1





        

if __name__ == '__main__':
    master = Tk()
    app = CalculatorWindow(master)
    master.mainloop()
    
