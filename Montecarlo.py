import pandas as pd
import numpy as np
import random

class Die:
    '''
    PURPOSE: Takes a die object that has N sides (faces) and W weights and rolls the object
    
    FUNCTIONS: 
    change_the_weight() 
       Checks to see if the face and weight passed is valid and allows you change the weight of a specific face of the die object 
    
    roll() function 
        Does a random sample from the vector of faces accoring to the weights
    
    show() function 
        Returns the current set of faces and weights in a dataframe
   
    '''
    def __init__(self, faces):
        '''
        PURPOSE: Constructs all the necessary attributes for the Die class

        INPUTS
        faces   an array of faces
        '''

        self.faces = faces 
        weights = np.ones(len(faces))
        self._facesFrame = pd.DataFrame(weights, columns = ['weights'], index = faces)
        
    def change_the_weight(self, face_value, new_weight):
        
      
        '''
        PURPOSE: Checks to see if the face passed is valid and checks to see if the weight is valid, then changes the weight of a specifice face 

        INPUTS
        face_value   int 
        new_weight   int
        
        OUTPUT
        self._facesFrame   Dataframe of the faces and weights
        '''
        self._facesFrame.loc[face_value,['weights']] = new_weight
        
        
        
        
    def roll(self, num_rolls=1):
        '''
        PURPOSE: Roll the die one or more times

        INPUTS
        num_rolls   defaults to 1
        
        OUTPUT
        outcomes    list of the rolls
        '''
        
        outcomes = random.choices(self._facesFrame.index, weights= self._facesFrame['weights'], k=num_rolls)
        return list(outcomes)
    
    def show(self):
        '''
        PURPOSE: Show the user the die's current set of faces and weights
        
        OUTPUT
        self._facesFrame   DataFrame of the current set of faces and weights
        '''
        
        return self._facesFrame

        

class Game():
    '''
     A game consists of rolling of one or more dice of the same kind one or more times.
     
     FUNCTIONS
     play()
        Rolls the dice a number of times given 
        
     show() 
        shows the user th results of the most recent play
    '''
    
    def __init__(self, Die_List):
        '''
        PURPOSE: Constructs all the necessary attributes for the Game class

        INPUTS
        Die_List    list of instantiated similar die objects

        OUTPUT
        None
        '''
        
        self.Die_list = Die_List
        return None
    
    def play(self, times_rolled):
        '''
        PURPOSE: Rolls the dice the number of times given

        INPUTS
        times_rolled    number

        OUTPUT
        self._play_df    Private Dataframe of rolls and dice
        '''
        
        
        self._play_df = pd.DataFrame()
        
        for i in range(len(self.Die_list)):
            rolled = pd.DataFrame(self.Die_list[i].roll(times_rolled), columns = [i+1], index = range(1, times_rolled +1))
            self._play_df = (pd.concat([self._play_df, rolled], axis = 1))
            
        self._play_df.index.name = 'Roll Number'
        
        return self._play_df
    
    def show(self, wide = True):
        
        '''
        PURPOSE: Shows the user the results of the most recent play in narrow or wide formate

        INPUTS
        Wide      boolean - default is True 

        OUTPUT
        narrow_df       Dataframe in narrow format 
        self._play_df   Dataframe in wide format 
        '''
        
        if wide == False: 
            narrow_df = pd.DataFrame(self._play_df.stack()) 
            narrow_df.columns = {'faces'}
            return narrow_df
            
        else: 
            return self._play_df
        
        
        
class Analyzer:
    '''
    Takes the results of a single game and computes various descriptive statistical properites about it
    
    FUNCTIONS 
        jackpot() counts how many times a roll resulted in all faces being the same 
        
        combo() counts how many combination types of faces were rolled and their counts 
        
        face_counts_per_roll() the number of times a given face appeared in each roll
        
    '''
    
    def __init__(self, game_object):
        
        '''
        PURPOSE: Constructs all the necessary attributes for the Analyzer class

        INPUTS
        game_object    Dataframe 

        '''
        
        self.game_object = game_object
        self.game = self.game_object.show()
        # Checks to see what type it is 
        faces_type = type(self.game[1]) 
        
    def jackpot(self):
        
        '''
        PURPOSE: Computes how many times the game resulted in all faces being identical


        OUTPUT
        len(self.booleans[self.booleans == True])     int
        '''
       
        self.booleans = self.game.nunique(axis = 1).eq(1)
        return len(self.booleans[self.booleans == True])
    
    def combo(self):
        
        '''
        PURPOSE: Computes the distinct combinations of faces rolled, along with their counts

        '''
        
        self.combo_df = self.game.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Counts')
        
    
    def face_counts_per_roll(self):
        
        '''
        PURPOSE: Computes how many times a given face is rolled in each event

        '''
        
        self.face_counts = (self.game.apply(pd.Series.value_counts, axis=1).fillna(0)).astype(int)
        