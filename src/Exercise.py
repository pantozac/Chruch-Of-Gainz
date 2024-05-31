#from src.utils import liftRound
#from typing import List

class Exercise:
    def __init__(self, name: str, isLift: bool):
        self.name: str = name
        self.type: bool = isLift
        #self.metric:str = metric
        #self.clockType = "" # AMRAP, Tabata/Interval, EMOM, FOR TIME

if __name__=="__main__":
    test = Exercise("lunge", True)
    print(test.name, test.type)


###### NOTES ######
# metrics - force values: "minSets", "maxSets", "minReps", "maxReps", "completion", "minDistance", "maxDistance", "minTime", "maxTime"