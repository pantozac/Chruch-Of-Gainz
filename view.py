import tkinter as tk
from tkinter import ttk

import re


LARGE_FONT= ("Verdana", 12)


#TEST VARIABLES
phase = 0
benchMax = 100
squatMax = 200
pushMax  = 300
deadMax = 400


class gainzGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (home_page, lift_home, settings_page, exercise_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home_page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()






class home_page(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        ttk.Label(self, text="Welcome to the Casa Panto Church of Gainz!", font=LARGE_FONT).pack(pady=10, padx=10)

        ttk.Button(self, text="Lift", command=lambda: controller.show_frame(lift_home)).pack()
        ttk.Button(self, text="Settings", command=lambda: controller.show_frame(settings_page)).pack()
        ttk.Button(self, text="Quit", command = quit).pack()


class lift_home(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        ttk.Label(self, text="What would you like to do?", font=LARGE_FONT).pack(pady=10, padx=10)

        ttk.Button(self, text="Bench", command=lambda: controller.show_frame(exercise_page)).pack()
        ttk.Button(self, text="Squat", command=lambda: controller.show_frame(exercise_page)).pack()
        ttk.Button(self, text="Push Press", command=lambda: controller.show_frame(exercise_page)).pack()
        ttk.Button(self, text="Deadlift", command=lambda: controller.show_frame(exercise_page)).pack()
        ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(home_page)).pack()


    #TO DO: 
    # - Ensure only integer values can be put in (entry can only accept strings, but you can restrict characters)
    # - Look into "trace" function to implement the controller - need a way to pass these values back to the controller


class exercise_page(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        ttk.Label(self, text="UNDER CONSTRUCTION", font=LARGE_FONT).pack(pady=10, padx=10)


        ## TO DO:
        # Create the view for lifts, passes through the name of the lift, the set/rep scheme, and the associated
        # weights
        # Have entry fields that can accept integer inputs

        #LONG TERM:
        # only show 1 set at a time with automated work/rest timers (include buzzer)

        ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(home_page)).pack()

class settings_page(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)

        ttk.Label(self, text="Settings", font=LARGE_FONT).grid(column=1, row = 0)

        self.ph = tk.IntVar(self, phase)

        ph1Radio = ttk.Radiobutton(self, text = "Phase 1", command = lambda: self.update_phase(), variable= self.ph, value = 0)
        ph1Radio.grid(column = 2, row = 1)
        ph2Radio = ttk.Radiobutton(self, text = "Phase 2", command = lambda: self.update_phase(), variable= self.ph, value = 1)
        ph2Radio.grid(column = 2, row = 2)

        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)

        self.bench_var= tk.StringVar(self, str(benchMax))
        self.squat_var= tk.StringVar(self, str(squatMax))
        self.push_var= tk.StringVar(self, str(pushMax))
        self.dead_var= tk.StringVar(self, str(deadMax))



        def max_field(dest, label_text, start_column, start_row, var):
            lift_label = ttk.Label(dest, text= label_text)
            lift_label.grid(column=start_column, row = start_row)
            lift_entry = ttk.Entry(dest, width = 10)
            
            lift_entry.config(
                            validate='all', 
                            validatecommand=vcmd, 
                            invalidcommand=ivcmd,
                            textvariable= var
            )
            lift_entry.insert(0, var)
            # KNOWN ISSUE: Inserting the maxes raises an Attribute Error, doesn't effect the program running just yet, but may lead
            # to problems in the future

            # Details:

# Exception in Tkinter callback
# Traceback (most recent call last):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2032.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 1948, in __call__  
#     return self.func(*args)
#            ^^^^^^^^^^^^^^^^
#   File "c:\Users\panto\Documents\02_Code Projects\Chruch-Of-Gainz\view.py", line 226, in on_invalid
#     self.show_message('Invalid character entered', 'red')
#   File "c:\Users\panto\Documents\02_Code Projects\Chruch-Of-Gainz\view.py", line 206, in show_message
#     self.label_error['text'] = error
#     ^^^^^^^^^^^^^^^^
# AttributeError: 'testPage' object has no attribute 'label_error'


            # This error showed up 4 times, I assume it's because there's a conflict with testing the insertion against a method that
            # hasn't been compiled yet.


            lift_entry.grid(column=start_column + 1, row= start_row)


        max_field(self, "Bench Press:", 0, 1, self.bench_var)
        max_field(self, "Back Squat:", 0, 2, self.squat_var)
        max_field(self, "Push Press:", 0, 3, self.push_var)
        max_field(self, "Deadlift:", 0, 4, self.dead_var)






        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(column = 0, row = 7, columnspan= 4)

        ttk.Button(self, text="Save Maxes", command= self.update_maxes).grid(column = 1, row = 5)
        ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(home_page)).grid(column = 1, row = 6)



#### HELPER FUNCTIONS####

    def show_message(self, error='', color='black'):
        self.label_error['text'] = error

    def validate(self, value):
        """
        Validat the email entry
        :param value:
        :return:
        """
        pattern = r'[\d]*'
        if re.fullmatch(pattern, value) is None:
            return False

        self.show_message()
        return True

    def on_invalid(self):
        """
        Show the error message if the data is not valid
        :return:
        """
        self.show_message('Invalid character entered', 'red')

    def update_maxes(self):
        print(self.bench_var.get(), self.squat_var.get(), self.push_var.get(), self.dead_var.get())
        return None
        
    def update_phase(self):
        print (self.ph.get())
        return None

root = gainzGUI()
root.mainloop()

