import math

def liftRound(weight):
    if math.fmod(weight,5) >= 2.5:
        weight = weight + 5 - math.fmod(weight,5)
    else:
        weight = weight - math.fmod(weight,5)
    return weight