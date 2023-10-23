#IMPORT STATEMENTS

import math

#END IMPORT STATEMENTS

def liftRound(weight):
    if math.fmod(weight,5) >= 2.5:
        weight = weight + 5 - math.fmod(weight,5)
    else:
        weight = weight - math.fmod(weight,5)
    return weight

#The tuples below are the multipliers for the max weight and the rep schemes
#Index 0 is for phase 1
#Index 1 is for phase 2

multipliers = ((0.5, 0.7, 0.8, 0.85, 0.75, 0.65), (0.5, 0.75, 0.825, 0.9, 0.85, 0.65))
reps =((10,8,6,4,6), (10,6,4,2,4))


#Phase 1: Show me set is 6-8, but only requires 6.  10 or more warrants a 10lb jump. Last set is always to failure,
#Phase 2: Show me set is 4-6, but only requires 4.  8 or more warrants a 10lb jump. Last set is always to failure,



class lift:

    def __init__(self, name):
        self.name = name
        self.maxVal = 0
        self.setArray = [0,0,0,0,0,0]

    def setMax(self, newMax):
        self.maxVal = newMax

    def calcSets(self, phase):
        for index in range(6):
            self.setArray[index] = liftRound(self.maxVal * multipliers[phase][index])

    
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
            self.setMax(int(input("You have failed every set, please input a lower 1RM. ")))
            # Case for total failure? Invoke new max flag for next week
    
    def workout(self):
        failCount = 0
        currSet = 0
        for index in range(4):
            currentWeight = self.setArray[currSet]
            currentReps = reps[phase][currSet]
            print("Set"+str(currSet+1)+": \n"+str(currentWeight)+" lbs for "+str(currentReps)+" reps.")
            check = int(input("How many reps did you do? "))
            if check < currentReps:
                failCount+=1
            else:
                print("Good Job!")
            currSet+=1
        currentWeight = self.setArray[currSet]
        currentReps = reps[phase][currSet]
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
        print("DEBUG: "+ str(self.setArray))
        self.showMe(failCount)
        self.calcSets(phase)
        print("Next week: "+str(self.setArray))
        


        

mainLifts = (lift("Bench Press"), lift("Back Squat"), lift("Push Press"), lift("Deadlift"))

phase = 0
#NEED TO FIND A WAY TO LIMIT THIS INPUT TO THE VALID PHASE STATES (mod 2?)
#GUI to limit options?

def initialize():
    for l in mainLifts:
        l.maxVal = int(input("Please input your max for "+l.name+": ")) # Will need to accept input from the View passed through controller
        l.calcSets(phase)
        print ("Your new max is "+str(l.maxVal)+" and your sets will be "+str(l.setArray)) # For debugging purposes only, delete after frontend is developed

def changePhase():
    for l in mainLifts:
        l.calcSets(phase)
        print ("Your current max is "+str(l.maxVal)+" and your sets will be "+str(l.setArray)) # For debugging purposes only, delete after frontend is developed



# Model Run Code

exitCond = False
initialize()


while exitCond != True:
    print("Welcome to the Church of Gainz!  Your current maxes are:")
    for i in range(4):
        print(mainLifts[i].name + ": "+str(mainLifts[i].maxVal))
    print("You are in Phase "+str(phase+1)+" of this program.")
    print("\n---------------------------------\n")
    inp = int(input("What would you like to do? \n1) Lift\n2) View Settings\n3) Exit\n"))
    
    # Workout Code
    
    if (inp==1):
        while True:
            inp = int(input("What would you like to do? \n1) Bench\n2) Squat\n3) Push Press\n4) Deadlift\n5) Exit\n"))
            match inp:
                case 1|2|3|4:
                    print("You have selected "+mainLifts[inp-1].name+".")
                    mainLifts[inp-1].workout()
                    break
                case 5:
                    print("Returning to Main Menu")
                    break
                case _ :
                    print("Invalid input, try again")
    
    
    # Settings Code
    
    
    elif (inp == 2):
        while True:
            inp = int(input("What would you like to do? \n1) Set Maxes\n2) Change Phase\n3) Exit\n"))
            match inp:
                
                # Set Maxes Code

                case 1:
                    set_choice = int(input("What max do you want to reset?\n1) Bench\n2) Squat\n3) Push Press\n4) Deadlift\n5) All\n"))
                    if set_choice in range(1,5):
                        mainLifts[set_choice-1].setMax(int(input("Enter new max: ")))
                        menuReturn = True
                    elif set_choice == 6:
                        initialize()
                        break
                    else:
                        print("Invalid input")
                
                # Change Phase Code

                case 2:
                    phase_choice = int(input("Which phase are you in?\n1) Phase 1\n2) Phase 2\n3) Go Back\n"))
                    if phase_choice in range (1,3):
                        phase = phase_choice - 1
                        changePhase()
                        break
                    else:
                        print ("Invalid Input")

                case 3:
                    print("Returning to Menu)")
                    break
                                             
                
    
    # Exit Condition Met


    elif (inp == 3):
        print("Proper exit.  Good bye!")
        exitCond = True
    else:
        print("Invalid option")


