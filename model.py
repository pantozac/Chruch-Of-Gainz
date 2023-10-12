#IMPORT STATEMENTS

import math

#END IMPORT STATEMENTS

def liftRound(weight):
    if math.fmod(weight,5) >= 2.5:
        weight = weight + 5 - math.fmod(weight,5)
    else:
        weight = weight - math.fmod(weight,5)
    return weight

multiplier_phase1 = (0.5, 0.7, 0.8, 0.85, 0.75, 0.65)
reps_phase1 =(10,8,6,4,6) #Show me is 6-8, but only requires 6.  10 or more warrants a 10lb jump. Last set is always to failure,

multiplier_phase2 = (0.5, 0.75, 0.825, 0.9, 0.85, 0.65)
reps_phase2 = (10,6,4,2,4) #Show me is 4-6, but only requires 4.  8 or more warrants a 10lb jump. Last set is always to failure,

#put the tuples into a containing tuple, the phase flag will reference the index of the tuple you want to reference
#allows code to be easily expandable if you want to add more phases later, or functionality to add more phases from the app

class lift:

    def __init__(self, name):
        self.name = name
        self.maxVal = 0
        self.setArray = [0,0,0,0,0,0]

    def setMax(self, newMax):
        self.maxVal = newMax

    def calcSets(self, phase):
        match phase:
            case 1:
                for index in range(6):
                    self.setArray[index] = liftRound(self.maxVal * multiplier_phase1[index])
            case 2:
                for index in range(6):
                    self.setArray[index] = liftRound(self.maxVal * multiplier_phase2[index])
    
    def showMe(self,missedSets):
        if missedSets < 0:
            self.maxVal+=10
        elif missedSets <= 1:
            self.maxVal+=5
        elif missedSets== 2:
            self.maxVal+=0
        elif missedSets == 3:
            self.maxVal-=5
        elif missedSets == 4:
            self.maxVal-=10
        else:
            self.setMax(input("You have failed every set, please input a lower 1RM. "))
            # Case for total failure? Invoke new max flag for next week
    
    def workout(self):
        failCount = 0
        currSet = 0
        for index in range(4):
            currentWeight = self.setArray[currSet]
            currentReps = reps_phase1[currSet]
            print("Set"+str(currSet+1)+": \n"+str(currentWeight)+" lbs for "+str(currentReps)+" reps.")
            check = int(input("How many reps did you do? "))
            if check < currentReps:
                failCount+=1
            else:
                print("Good Job!")
            currSet+=1
        currentWeight = self.setArray[currSet]
        currentReps = reps_phase1[currSet]
        print("SHOW ME SET! (Set "+str(currSet+1)+"): \n"+str(currentWeight)+" lbs for "+str(currentReps)+" reps.")
        check = int(input("How many reps did you do? "))
        if check < currentReps:
            failCount+=2
        elif check > currentReps+4:
            failCount -= 1
            print("AMAZING JOB! +10 lbs")
        else:
            print("Good Job!")
        currSet+=1
        print("Last set:"+str(self.setArray[5])+" lbs until failure")
        check = int(input("How many reps did you do? "))
        print("Good Job!")
        self.showMe(failCount)
        


        

mainLifts = [lift("Bench Press"), lift("Back Squat"), lift("Push Press"), lift("Deadlift")]

def initialize():
    for l in mainLifts:
        l.maxVal = int(input("Please input your max for "+l.name+": ")) # Will need to accept input from the View passed through controller
        l.calcSets(1)
        print ("Your new max is "+str(l.maxVal)+" and your sets will be "+str(l.setArray)) # For debugging purposes only, delete after frontend is developed


# DEBUGGING/TESTING CODE
exitCond = False
initialize()
while exitCond != True:
    print("Welcome to the Church of Gainz!  Your current maxes are:")
    for i in range(4):
        print(mainLifts[i].name + ": "+str(mainLifts[i].maxVal))
    print("\n---------------------------------\n")
    inp = int(input("What would you like to do? \n1) Lift\n2) View Settings\n3) Exit\n"))
    if (inp==1):
        inp = int(input("What would you like to do? \n1) Bench\n2) Squat\n3) Push Press\n4) Deadlift\n5) Set Maxes\n6) Exit\n"))
        match inp:
            case 1|2|3|4:
                print("You have selected "+mainLifts[inp-1].name+".")
                mainLifts[inp-1].workout()
            case 5:
                set_choice = int(input("What max do you want to reset?\n1) Bench\n2) Squat\n3) Push Press\n4) Deadlift\n5) All\n"))
                if set_choice in range(1,5):
                    mainLifts[set_choice-1].setMax(int(input("Enter new max: ")))
                else:
                    initialize()
            case _ :
                print("Invalid input, returning to main menu")
    elif (inp == 2):
        print("Settings coming soon")
    elif (inp == 3):
        print("Proper exit.  Good bye!")
        exitCond = True
    else:
        print("Invalid option, exiting program")
        exitCond = True




"""
Next Steps:
 - Ways to shift phases
 - config file/ways to save the state
 - account/user info
 - frontend


test=lift("test")
test.setMax(335)
test.calcSets(1)
print(test.maxVal, test.setArray)
test.calcSets(2)
print(test.setArray)

initialize()
"""
