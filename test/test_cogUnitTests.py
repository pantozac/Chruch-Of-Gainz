import unittest
from src.Lift import Lift
from src.Timer import Stopwatch, AMRAP, Tabata, EMOM
from src import utils

class cog_UnitTests(unittest.TestCase):
    
    def test_class_Lift(self):
        testLift = Lift("Test Lift")
        self.assertEqual(testLift.name, "Test Lift", "Lift Name did not intialize")
        self.assertEqual(testLift.maxVal, 0, "setMax did not initialize with 0")
        testLift.setMax(255)
        self.assertEqual(testLift.maxVal, 255, "setMax failed to update")
        self.assertEqual(testLift.setArray, [0,0,0,0,0,0], "setArray failed to initialize correctly")
        testLift.calcSets([0.5, 0.6, 0.7, 0.8, 0.75, 0.65])
        self.assertEqual(testLift.setArray, [130.0, 155.0, 180.0, 205.0, 190.0, 165.0], "Set array calculation is wrong")
        testLift.showMe(4)
        self.assertEqual(testLift.maxVal, 245, "showMe Calculation Error")
        testLift.showMe(3)
        self.assertEqual(testLift.maxVal, 240, "showMe Calculation Error")
        testLift.showMe(2)
        self.assertEqual(testLift.maxVal, 240, "showMe Calculation Error")
        testLift.showMe(1)
        self.assertEqual(testLift.maxVal, 245, "showMe Calculation Error")
        testLift.showMe(0)
        self.assertEqual(testLift.maxVal, 250, "showMe Calculation Error")
        testLift.showMe(-1)
        self.assertEqual(testLift.maxVal, 260, "showMe Calculation Error")
        testLift.calcSets([0.5, 0.6, 0.7, 0.8, 0.75, 0.65])
        self.assertEqual(testLift.setArray, [130.0, 155.0, 180.0, 210.0, 195.0, 170.0], "Set array calculation is wrong")
    
    def test_util_liftRound(self):
        inpWeights = [122, 122.24, 122.5, 125, 127, 127.4, 127.5, 127.6]
        expOutput = [120.0, 120.0, 125.0, 125.0, 125.0, 125.0, 130.0, 130.0]
        for x in inpWeights:
            self.assertEqual(utils.liftRound(x), expOutput[inpWeights.index(x)])
    
    def test_class_AMRAP(self):
        test = AMRAP(10.00)
        self.assertTrue(test.duration==0, "Running clock, AMRAP should be initialized to 0 and not running")
        self.assertTrue(test.running==False, "AMRAP timer is running at initialization")
        self.assertTrue(test.max == 10.00, "AMRAP param failed to initialize")
        test.run()
        self.assertTrue(False, "Test Not Fully Implemented")
        

    def test_class_Tabata(self):
        test = Tabata(10.00, 5.00, 3)
        self.assertTrue(test.duration==0, "Running clock, Tabata should be initialized to 0 and not running")
        self.assertTrue(test.running==False, "Tabata timer is running at initialization")
        self.assertTrue(test.work == 10.00 and test.rest == 5.00 and test.rounds == 3, "Tabata params failed to initialize")
        self.assertTrue(False, "Test Not Fully Implemented")

    def test_class_EMOM(self):
        test = EMOM(10.00, 3)
        self.assertTrue(test.duration==0, "Running clock, EMOM should be initialized to 0 and not running")
        self.assertTrue(test.running==False, "EMOM timer is running at initialization")
        self.assertTrue(test.work == 10.00 and test.limit == 3, "EMOM params failed to initialize")
        self.assertTrue(False, "Test Not Fully Implemented")
    
if __name__ == '__main__':
    unittest.main()