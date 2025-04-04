#from src.utils import liftRound
from typing import List
from datetime import datetime

class Exercise:
    name: str
    metric: str
    equipment: List[str]
    clockType: any
    sets: int
    reps: List[int]
    distance: int
    time: int
    score: int | datetime

        #self.metric:str = metric
        #self.clockType = "" # AMRAP, Tabata/Interval, EMOM, FOR TIME

if __name__=="__main__":
    test = Exercise("lunge", True)
    print(test.name, test.type)


###### NOTES ######
# metrics - force values: "minSets", "maxSets", "minReps", "maxReps", "completion", "minDistance", "maxDistance", "minTime", "maxTime"