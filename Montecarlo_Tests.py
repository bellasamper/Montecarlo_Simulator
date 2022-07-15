import unittest
from Montecarlo import *


class DieTestSuite(unittest.TestCase):
    
    '''
    DieTestSuite tests the Die class to see if all the functions within it work
    
    '''
    
    def test_1_change_the_weight(self):
        '''
        test_1_change_the_weight tests the function change_the_weight() from the Die class which changes the weight of one of the faces. This test tests to see if the new weight in the dataframe is right 
        '''
        
        die1.change_the_weight(5, 6.0)
        
        expected = 6.0
                
        self.assertEqual(die1.show()['weights'][5], expected)

    def test_2_roll(self):
        '''
        test_2_roll tests the function roll() from the Die class which rolls the die a certain number of times. It is testing the length of the dataframe to make sure it is the length of how many rolls it was given
        '''
        
        length = len(die1.roll(10))
        
        expected = 10
        
        self.assertEqual(length, expected)
        
    def test_3_show(self):
        '''
        test_3_show tests the function show() from the Die class which shows the dataframe with the current weights and faces. It is testing to see if the dimensions of the dataframe is right accoring to the number of faces on a die
        '''
        
        df = die1.show()
        
        expected = [6,1]
        
        self.assertEqual(list(df.shape), expected)

        
        
class GameTestSuite(unittest.TestCase):
    
    '''
    GameTestSuite tests the Game class to see if all the functions within it work
    
    '''
    
    def test_1_play(self):
        '''
        test_1_play tests the function play() from class Game which rolls the dice the number of times it is given. It is testing to see if the length of the dataframe is the number of times it has been played.
        '''
        
        game1 = Game([die1, die1, die1])
        df = game1.play(15)
        
        expected = 15
        
        self.assertEqual(len(df[1]), expected)
        
        
    def test_2_show(self):
        '''
        test_2_show tests the function show() from the class Game which shows the dataframe of the the most recent plays. It is testing to see if the length of the dataframe is the number of times it has been played
        '''
        
        game1 = Game([die1, die1, die1])
        game1.play(15)
        df = game1.show()
        
        expected = 15
        
        self.assertEqual(len(df[1]), expected)
        
        
class AnalyzerTestSuite(unittest.TestCase):
    
    '''
    AnalyzerTestSuite tests the Analyzer class to see if all the functions within it work
    
    '''
    
    def test_1_jackpot(self):
        
        '''
        test_1_jackpot tests the function jackpot() from the class Analyzer which computes how many times the game resulted in all faces being identical. It is testing to see if the number of jackpots is greater than 0 since it is played 10000 times
        '''
        
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        num = analyzer1.jackpot()
        
        self.assertNotEqual(num, 0)
        
    def test_2_combo(self):
        
        '''
        test_2_combo tests the function combo() from the class Analyzer which computes the distinct combinations of faces rolled, along with their counts. It is testing if the sum of the counts of each combination equals the number of times played.
        '''
        
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        analyzer1.combo()
        sums = analyzer1.combo_df["Counts"].sum()
        
        self.assertEqual(sums, 10000)
        
    def test_3_face_counts_per_roll(self):
        
        '''
        test_3_face_counts_per_roll test the function face_counts_per_rool from the class Analyzer which computes how many times a given face is rolled in each event. It is testing if the length of the dataframe is equal to the number of times it has been played. 
        '''
        
        game1 = Game([die1, die1, die1])
        game1.play(10000)
        analyzer1 = Analyzer(game1)
        analyzer1.face_counts_per_roll()
        
        expected = 10000
        
        self.assertEqual(len(analyzer1.face_counts), expected)
        

if __name__ == '__main__':
    die1 = Die([1,2,3,4,5,6])
    unittest.main(verbosity=3)