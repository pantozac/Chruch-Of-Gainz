import tkinter as tk
from tkinter import ttk

import re


LARGE_FONT= ("Verdana", 12)


#TEST VARIABLES
phase = 0
benchMax = 100
squatMax = 200
pushMax = 300
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

class settings_page(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        ttk.Label(self, text="Settings", font=LARGE_FONT).grid(column=1, row = 0)

        ph = tk.IntVar(None, phase)

        ph1Radio = ttk.Radiobutton(self, text = "Phase 1", command = lambda: update_phase(), variable= ph, value = 0)
        ph1Radio.grid(column = 2, row = 1)
        ph2Radio = ttk.Radiobutton(self, text = "Phase 2", command = lambda: update_phase(), variable= ph, value = 1)
        ph2Radio.grid(column = 2, row = 2)

        ttk.Label(self, text="Bench Max", font=LARGE_FONT).grid(column = 0, row = 1, sticky = "E")
        benchEntry=ttk.Entry(self, textvariable= benchMax, width=10)
        benchEntry.insert(0, str(benchMax))
        benchEntry.grid(column = 1, row = 1, sticky = "W")

        ttk.Label(self, text="Squat Max", font=LARGE_FONT).grid(column = 0, row = 2, sticky = "E")
        squatEntry = ttk.Entry(self, textvariable= squatMax, width=10)
        squatEntry.insert(0, str(squatMax))
        squatEntry.grid(column = 1, row = 2, sticky = "W")

        ttk.Label(self, text="Push Press Max", font=LARGE_FONT).grid(column = 0, row = 3, sticky = "E")
        pushEntry = ttk.Entry(self, textvariable= pushMax, width=10)
        pushEntry.insert(0, str(pushMax))
        pushEntry.grid(column = 1, row = 3, sticky = "W")

        ttk.Label(self, text="Deadlift Max", font=LARGE_FONT).grid(column = 0, row = 4, sticky = "E")
        deadEntry = ttk.Entry(self, textvariable= deadMax, width=10)
        deadEntry.insert(0, str(deadMax))
        deadEntry.grid(column = 1, row = 4, sticky = "W")

        ttk.Button(self, text="Save Maxes", command= lambda: update_maxes()).grid(column = 1, row = 5)
        ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(home_page)).grid(column = 1, row = 6)

        def update_maxes():
            print ("Maxes Updated!")
            benchMax = benchEntry.get()
            squatMax = squatEntry.get()
            pushMax = pushEntry.get()
            deadMax = deadEntry.get()
            print("Bench: "+str(benchMax)+"\n"
              "Squat: "+str(squatMax)+"\n"
              "Push Press: "+str(pushMax)+"\n"
              "Deadlift: "+str(deadMax)+"\n"            
              )
        
        def update_phase():
            phase = ph.get()
            print ("Phase: " +str(phase))




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


root = gainzGUI()
root.mainloop()

