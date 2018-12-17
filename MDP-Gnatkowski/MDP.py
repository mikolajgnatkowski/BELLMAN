import random
from datetime import datetime

from State import State
from Map import Map

class MDP:
    def __init__(self, gamma, steps, f_map):     
        self.gamma = gamma
        self.steps = steps
        self.states = Map(f_map).statesArray()
        self.calcStatesProbability()

    def calcStatesProbability(self):
        self.normalStateIdxList = []
        for idxsR, stateRow in enumerate(self.states):
            for idxs, state in enumerate(stateRow):
                if state.type_s_n == 'normal':
                    state.makeCalculations(self.states)
                    self.normalStateIdxList.append([idxsR,idxs])

    def bestAction(self,positon):
        self.states[positon[0]][positon[1]].chooseBestAction()
        return self.states[positon[0]][positon[1]].valueOfBestAction()

    def start(self):    
        for i in range(self.steps):
            toVisitList = self.normalStateIdxList[:]   
            while len(toVisitList)>0:  
                pos = self.randomStatePos(toVisitList)                   
                best = self.bestAction(pos)
                state = self.states[pos[0]][pos[1]]
                newPot = state.reward + (self.gamma*best)              
                if state.newPotentialIsVerySimilar(newPot):
                    self.normalStateIdxList.remove(pos)
                state.potential = newPot
            toVisitList = self.normalStateIdxList[:]   
            if len(toVisitList) == 0:
                break   

    def randomStatePos(self,toVisitList):
        random.seed(datetime.now())
        randomPos = random.choice(toVisitList)
        toVisitList.remove(randomPos)
        return randomPos

    def returnMapPotentials(self):
        mapListString = ''        
        for y in self.states:               
               for x in y:      
                   mapListString += '\t' + self.cutFloatOrAddZero(x.potential,2) 
               mapListString += '\n'  
        return mapListString

    def returnMapOfMovement(self):
        mapListString = ''        
        for y in self.states: 
               mapListString += '\t'        
               for x in y:
                   if x.bestAction == '0':
                       mapListString += '0' + '\t'
                   else:
                       mapListString += str(x.borders_n.index(x.bestAction)+1) + '\t' 
               mapListString += '\n' 
        return mapListString
    
    def cutFloatOrAddZero(self,potent,cutLen):
        string = repr(potent).split('.')
        if len(string) == 1:
            return (string[0] + '.00')
        return (string[0]+'.'+string[1][:cutLen])             
            