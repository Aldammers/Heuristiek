from classes import *
from random import randint

myProtein = Protein('HHPPHPPHH')
myProtein.reveal()
myProtein.grit.reveal()

def RandomFold(protein):
    directions = ['up', 'down', 'left', 'right']
    lastcoordinate = [len(protein.sequence) + 1, len(protein.sequence) +1]
    for amino in protein.sequence:
        direction = directions[randint(0, 3)]
        print(direction)
        
RandomFold(myProtein)
    


    
