import unittest
from Montecarlo import *


class DieTestSuite(unittest.TestCase):
    
    
    def test_1_change_the_weight(self):
        # create a die and change the weight of one of the faces 
        
        die1.change_the_weight(5, 6.0)
        
        expected = 6.0
                
        self.assertEqual(die1.show()['weights'][5], expected)

    def test_2_roll(self):
        
        length = len(die1.roll(10))
        
        expected = 10
        
        self.assertEqual(length, expected)
        
    def test_3_show(self):
        
        df = die1.show()
        
        expected = [6,1]
        
        self.assertEqual(list(df.shape), expected)

        
        
class GameTestSuite(unittest.TestCase):
    
    def test_1_play(self):
        game1 = Game([die1, die1, die1])
        df = game1.play(15)
        
        expected = 15
        
        self.assertEqual(len(df[1]), expected)
        
        
    def test_2_show(self):
        game1 = Game([die1, die1, die1])
        game1.play(15)
        df = game1.show()
        
        expected = 15
        
        self.assertEqual(len(df[1]), expected)
        
        
class AnalyzerTestSuite(unittest.TestCase):
    
    def test_1_jackpot(self):
        
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        num = analyzer1.jackpot()
        
        self.assertNotEqual(num, 0)
        
    def test_2_combo(self):
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        analyzer1.combo()
        sums = analyzer1.combo_df["Counts"].sum()
        
        self.assertEqual(sums, 10000)
        
    def test_3_face_counts_per_roll(self):
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        analyzer1.face_counts_per_roll()
        
        expected = 10000
        
        self.assertEqual(len(analyzer1.face_counts), expected)
        

if __name__ == '__main__':
    die1 = Die([1,2,3,4,5,6])
    unittest.main(verbosity=3)