class Action(object):   
    def __init__(self,name,position,states):
        self.name = name
        self.position = position
        self.states = states 
        self.probability = [ [0] * len(states[0]) for _ in range(len(states))]
        self.possibleSubAcions_n = self.states[position[0]][position[1]].borders_n[:]  
        self.borders_n = self.states[position[0]][position[1]].borders_n[:]    
        self.borders =  self.states[position[0]][position[1]].borders[:] 
                      
    def calcProbability(self):
        if self.name == 'U': 
            self.sortForwardMoveAndRemove('U','D')          
        elif self.name == 'R':
            self.sortForwardMoveAndRemove('R','L')           
        elif self.name == 'D': 
            self.sortForwardMoveAndRemove('D','U')          
        elif self.name == 'L':            
            self.sortForwardMoveAndRemove('L','R')           
        self.calcProbabilityOfAction()

    def calcProbabilityOfAction(self):
        probability = 0
        mustStay = False
        noPosibleMove = []
        for idxdOM, directionOfMove in enumerate(self.possibleSubAcions_n):
            if self.borders[self.borders_n.index(directionOfMove)][1]  == False:
                if idxdOM == 0:
                    self.setProbabilityToSPrime(directionOfMove,0.8)
                else:
                    self.setProbabilityToSPrime(directionOfMove,0.1)
            elif self.borders[self.borders_n.index(directionOfMove)][1]  == True:
                if idxdOM == 0:
                    probability = probability + 0.8
                else:
                    probability = probability + 0.1
                mustStay = True
                noPosibleMove.append(directionOfMove)
        if mustStay:
            for noPosMov in noPosibleMove:
                self.possibleSubAcions_n.remove(noPosMov) 
            self.possibleSubAcions_n.append('S')
            self.setProbabilityToSPrime('S',probability)


    def setProbabilityToSPrime(self,direction,value):
        pos = self.getPositionOfTransition(direction)
        self.probability[pos[0]][pos[1]] = value       

    def calcPotentialOfAction(self):
        self.potential = 0
        for posibleSubA in self.possibleSubAcions_n:
            pos = self.getPositionOfTransition(posibleSubA)
            self.potential += self.probability[pos[0]][pos[1]] * self.states[pos[0]][pos[1]].potential
     
    def sortForwardMoveAndRemove(self,forwardMove,removeMove):
        self.possibleSubAcions_n.remove(removeMove) 
        newList = []
        newList.append(forwardMove)
        self.possibleSubAcions_n.remove(forwardMove)
        for old in self.possibleSubAcions_n:
            newList.append(old)
        self.possibleSubAcions_n = newList

    def getPositionOfTransition(self,direction):
        if direction == 'U':
            return [(self.position[0]-1),(self.position[1])]
        elif direction == 'R':
            return [(self.position[0]),(self.position[1]+1)]
        elif direction == 'D':
            return [(self.position[0]+1),(self.position[1])]
        elif direction == 'L':
            return [(self.position[0]),(self.position[1]-1)]
        elif direction == 'S':
            return [(self.position[0]),(self.position[1])]
