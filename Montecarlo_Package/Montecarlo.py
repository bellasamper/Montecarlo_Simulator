import pandas as pd
import numpy as np
import random

class Die:
    '''
    PURPOSE: 
    '''
    def __init__(self, faces):
        '''
        PURPOSE: Given a list of values, compare each value against a threshold

        INPUTS
        vals    list of ints or floats
        thresh  int or float

        OUTPUT
        bools  list of booleans
        '''

        self.faces = faces 
        weights = np.ones(len(faces))
        self._facesFrame = pd.DataFrame(weights, columns = ['weights'], index = faces)
        
    def change_the_weight(self, face_value, new_weight):
        
        self._facesFrame.loc[face_value,['weights']] = new_weight
        
    def roll(self, num_rolls=1):
        outcomes = random.choices(self._facesFrame.index, weights= self._facesFrame['weights'], k=num_rolls)
        return list(outcomes)
    
    def show(self):
        return self._facesFrame

        

class Game():
    '''
    DocString
    '''
    def __init__(self, Die_List):
        self.Die_list = Die_List
        return None
    
    def play(self, times_rolled):
        self._play_df = pd.DataFrame()
        
        for i in range(len(self.Die_list)):
            rolled = pd.DataFrame(self.Die_list[i].roll(times_rolled), columns = [i+1], index = range(1, times_rolled +1))
            self._play_df = (pd.concat([self._play_df, rolled], axis = 1))
            
        self._play_df.index.name = 'Roll Number'
        
        return self._play_df
    
    def show(self, wide = True):
        
        if wide == False: 
            narrow_df = pd.DataFrame(self._play_df.stack()) 
            narrow_df.columns = {'faces'}
            return narrow_df
            
        else: 
            return self._play_df
        
        
        
class Analyzer:
    '''
    Docstring 
    '''
    
    def __init__(self, game_object):
        self.game_object = game_object
        self.game = self.game_object.show()
        # Checks to see what type it is 
        faces_type = type(self.game[1]) 
        
    def jackpot(self):
       
        self.booleans = self.game.nunique(axis = 1).eq(1)
        return len(self.booleans[self.booleans == True])
    
    def combo(self):
        
        self.combo_df = self.game.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Counts')
        
    
    def face_counts_per_roll(self):
        
        self.face_counts = (self.game.apply(pd.Series.value_counts, axis=1).fillna(0)).astype(int)
        