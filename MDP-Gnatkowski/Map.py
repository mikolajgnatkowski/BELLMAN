from State import State

class Map(object):
    yLenght = 0
    xLength = 0
    states = []
    def __init__(self,map):
        self.createStates(map)
    def createStates(self,map):
       with open(map) as file:
           line = file.readline().split()
           self.xLength = int(line[0])
           self.yLenght = int(line[1])
           self.xSize = self.xLength - 1
           self.ySize = self.yLenght - 1
           for y in file:
               if y[1] == '\n':
                   break
               row_array = []
               for x in y.split():
                   row_array.append(State(int(x)))
               self.states.append(row_array)              
           for yidx,y in enumerate(file):              
               if y[1] == '\n':
                   break             
               for xidx, x in enumerate(y.split()):
                   self.states[yidx][xidx].setRewardAndPosition(int(x),[yidx,xidx])    
                   if (yidx == 0):
                       self.states[yidx][xidx].setBorder('U')
                   if (yidx == self.ySize):
                       self.states[yidx][xidx].setBorder('D')
                   if (xidx == 0):
                       self.states[yidx][xidx].setBorder('L')
                   if (xidx == self.xSize):
                       self.states[yidx][xidx].setBorder('R')
    def statesArray(self):
        return self.states


                                         
  
        