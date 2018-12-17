from Action import Action

class Actions(object):     
     def __init__(self,position,states):
         self.position = position
         self.borders_n = states[position[0]][position[1]].borders_n
         self.states = states 
         self.listOfActions = []

     def calcActionsProbability(self):
         for action in self.borders_n:
             act = Action(action,self.position,self.states)
             act.calcProbability()             
             self.listOfActions.append(act)    

     def calcActionsPotentials(self):    
         for action in self.listOfActions:
            action.calcPotentialOfAction()
     
     def bestAction(self):
        max = 0
        bestA_n = ''
        self.calcActionsPotentials()
        for idxa, action in enumerate(self.listOfActions):
            if idxa == 0:
                max = action.potential
                bestA_n = action.name
                continue
            if max <= action.potential:
                max =  action.potential
                bestA_n = action.name
        return bestA_n     
