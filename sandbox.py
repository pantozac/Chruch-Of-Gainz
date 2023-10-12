#IMPORT STATEMENTS

import math

#END IMPORT STATEMENTS

def liftRound(weight):
    if math.fmod(weight,5) >= 2.5:
        weight = weight + 5 - math.fmod(weight,5)
    else:
        weight = weight - math.fmod(weight,5)
    return weight

phase1 = [0.5, 0.7, 0.8, 0.85, 0.75, 0.65]
phase2 = []


class lift:

    def __init__(self, name):
        self.name = name
        self.maxVal = 0
        self.setArray = [0,0,0,0,0,0]

    def setMax(self, newMax):
        self.maxVal = newMax

    def calcSetsPhase_01(self):
        for index in range(6):
           self.setArray[index] = liftRound(self.maxVal * phase1[index])



mainLifts = [lift("Bench Press"), lift("Back Squat"), lift("Push Press"), lift("Deadlift")]

def initialize():
    for l in mainLifts:
        l.maxVal = int(input("Please input your max for "+l.name+": "))
        l.calcSetsPhase_01()

test=lift("test")
test.setMax(335)
test.calcSetsPhase_01()
print(test.maxVal, test.setArray)
