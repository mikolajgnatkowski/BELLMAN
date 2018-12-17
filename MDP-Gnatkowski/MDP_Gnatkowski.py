from MDP import MDP

mdp = MDP(0.5,1000,'map.txt')
mdp.start()
print('Mapa potencjałów:')
print(mdp.returnMapPotentials())

print('Polityka ruchu: (1, 2, 3, 4 to odpowiednio ruch do góry, w prawo, w dół, w lewo)')
print(mdp.returnMapOfMovement())