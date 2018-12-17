from Actions import Actions

class State(object):   
    borders_n = ['U','R','D','L']

    def __init__(self,type_s):
        self.type_s = type_s
        type_s_n_a = ['obstacle','normal','endpoint']               
        self.borders = [[self.borders_n[0],False],[self.borders_n[1],False],[self.borders_n[2],False],[self.borders_n[3],False]]
        self.type_s_n = type_s_n_a[type_s]
        self.bestAction = '0'
        if self.type_s_n == 'normal':
            self.bestAction = 'U'

    def setRewardAndPosition(self,reward,position):
        self.reward = reward
        self.potential = reward
        self.position = position

    def chooseBestAction(self):
        self.bestAction = self.actions.bestAction()

    def valueOfBestAction(self):
        return self.actions.listOfActions[self.borders_n.index(self.bestAction)].potential

    def makeCalculations(self,states):
        self.states = states
        self.checkObstaclesAroundState()
        act = Actions(self.position,states)
        act.calcActionsProbability()
        self.actions = act

    def setBorder(self,direction):
        self.borders[self.borders_n.index(direction)][1] = True

    def getBorder(self,direction):
        return self.borders[self.borders_n.index(direction)][1]
       
    def checkObstaclesAroundState(self):
         states = self.states
         typeState = 'obstacle'
         if self.getBorder('U') == False:
             if states[self.position[0]-1][self.position[1]].type_s_n == typeState:
                 self.setBorder('U')
         if self.getBorder('R') == False:
             if states[self.position[0]][self.position[1]+1].type_s_n == typeState:
                 self.setBorder('R')
         if self.getBorder('D') == False:
             if states[self.position[0]+1][self.position[1]].type_s_n == typeState:
                 self.setBorder('D')
         if self.getBorder('L') == False:
             if states[self.position[0]][self.position[1]-1].type_s_n == typeState:
                 self.setBorder('L')

    def newPotentialIsVerySimilar(self,newPotential):
        difference = abs((self.potential - newPotential))
        if difference < 0.000000001:
            return True
        else:
            return False
