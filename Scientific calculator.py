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
        
        # ================================ Numberpad ====================================

        numberpad = "789456123"
        i = 0
        btn = []
        for j in range (2,5):
            for k in range(3):
                btn.append(Button(calc, width=6, height=2, font = ('arial', 20, 'bold'),
                 bd=4, text = numberpad[i], bg = '#101820', fg='#f2aa4c' ))
                btn[i].grid(row=j , column=k, pady=1)
                i+=1
        
        # ============================= Operation buttons ===================================
        btnclear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnclear.grid(row=1, column=0, pady=1)

        btnclear_all = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='Orange', fg='#101820')
        btnclear_all.grid(row=1, column=1, pady=1)

        btnsqrt = Button(calc, text='√', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnsqrt.grid(row=1, column=2, pady=1)

        btnplus = Button(calc, text='+', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnplus.grid(row=1, column=3, pady=1)

        btnminus = Button(calc, text='-', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnminus.grid(row=2, column=3, pady=1)

        btnmultiply = Button(calc, text='x', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnmultiply.grid(row=3, column=3, pady=1)

        btndivide = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btndivide.grid(row=4, column=3, pady=1)

        btnzero = Button(calc, text='0', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnzero.grid(row=5, column=0, pady=1)

        btnpoint = Button(calc, text='.', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnpoint.grid(row=5, column=1, pady=1)

        btnplusminus = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnplusminus.grid(row=5, column=2, pady=1)

        btnequals = Button(calc, text='=', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnequals.grid(row=5, column=3, pady=1)

        # =============================== Scientific ===================================

        labelsctf = Label(calc, text = 'Scientific Calculator', font=('helvetica', 30, 'bold'),
        justify=RIGHT)
        labelsctf.grid(row=0, column=4, columnspan=4)

        btnpi = Button(calc, text='π', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnpi.grid(row=1, column=4, pady=1)

        btnCos = Button(calc, text='cos', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnCos.grid(row=1, column=5, pady=1)

        btntan = Button(calc, text='tan', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btntan.grid(row=1, column=6, pady=1)

        btnsin = Button(calc, text='sin', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnsin.grid(row=1, column=7, pady=1)

        # ============================================================================

        btn2pi = Button(calc, text='2π', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btn2pi.grid(row=2, column=4, pady=1)

        btnCosh = Button(calc, text='cosh', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnCosh.grid(row=2, column=5, pady=1)

        btntanh = Button(calc, text='tanh', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btntanh.grid(row=2, column=6, pady=1)

        btnsinh = Button(calc, text='sinh', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnsinh.grid(row=2, column=7, pady=1)

        # ============================================================================

        btnlog = Button(calc, text='log', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnlog.grid(row=3, column=4, pady=1)

        btnExp = Button(calc, text='Exp', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnExp.grid(row=3, column=5, pady=1)

        btnMod = Button(calc, text='Mod', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnMod.grid(row=3, column=6, pady=1)

        btnE = Button(calc, text='e', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnE.grid(row=3, column=7, pady=1)

        # ==============================================================================

        btnlog2 = Button(calc, text='log2', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnlog2.grid(row=4, column=4, pady=1)

        btndeg = Button(calc, text='deg', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btndeg.grid(row=4, column=5, pady=1)

        btnacosh = Button(calc, text='acosh', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnacosh.grid(row=4, column=6, pady=1)

        btnasinh = Button(calc, text='asinh', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#f2aa4c', fg='#101820')
        btnasinh.grid(row=4, column=7, pady=1)

        # ==================================================================================

        btnlog10 = Button(calc, text='log10', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnlog10.grid(row=5, column=4, pady=1)

        btnlog1p = Button(calc, text='log1p', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnlog1p.grid(row=5, column=5, pady=1)

        btnexpm1 = Button(calc, text='expm1', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btnexpm1.grid(row=5, column=6, pady=1)

        btn1gamma = Button(calc, text='1gamma', width=6, height=2, font=('arial', 20,'bold'),
        bd=4, bg='#101820', fg='#f2aa4c')
        btn1gamma.grid(row=5, column=7, pady=1)

        # ====================================================================================


if __name__ == '__main__':
    master = Tk()
    app = CalculatorWindow(master)
    master.mainloop()
    
