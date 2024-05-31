from src.utils import liftRound
from typing import List

class Lift:

    def __init__(self, name: str):
        self.name = name
        self.maxVal = 0
        self.setArray = [0,0,0,0,0,0]

    def setMax(self, newMax: int):
        self.maxVal = newMax

    def calcSets(self, multipliers: List[float]):
        for index in range(6):
            self.setArray[index] = liftRound(self.maxVal * multipliers[index])

    
    def showMe(self, missedSets: int):
        if missedSets < 0:
            self.maxVal+=10
        elif missedSets <= 1:
            self.maxVal+=5
        elif missedSets== 2:
            self.maxVal+=0
        elif missedSets == 3:
            self.maxVal-=5
        else:
            self.maxVal-=10
            #TODO Invoke process to change 