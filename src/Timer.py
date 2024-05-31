from stopwatch import Stopwatch


class AMRAP(Stopwatch):
    """
    AMRAP (As many reps/rounds as possible) -
    For workouts with known weights/distances, and a fixed time.
    Workout is scored based on the number of rounds/reps completed in the given timeframe.
    """
    def __init__(self, max: float, digits: int = 2):
        super().__init__(digits)
        self.max = max
        self.reset()
    
    def run(self):
        """this is a test"""
        self.start()
        while self.duration <= self.max:
            print(self.duration)
        self.stop()

class Tabata(Stopwatch):
    def __init__(self, work: float, rest: float, rounds: int, digits: int = 2):
        super().__init__(digits)
        self.work = work
        self.rest = rest
        self.rounds = rounds
        self.reset()

    def run(self):
        for i in range(self.rounds):
            while self.duration <= self.work:
                pass
            self.restart()
            while self.duration <= self.rest:
                pass
            self.restart()

class EMOM(Stopwatch):
    def __init__(self, work: float, limit: int, digits: int = 2):
        super().__init__(digits)
        self.work = work
        self.limit = limit
        self.reset()

    def run(self):
        for i in range(self.limit):
            self.restart()
            while self.duration <= self.work:
                pass

if __name__ == "__main__":
    x = AMRAP(3.00)
    x.run()
    # print("AMRAP END")
    #time.sleep(1)
    # print("TABATA START")
    #y = Tabata(10.00, 5.00, 3)
    #y.run()
    z = EMOM(10.00, 3)
    z.run()