import classes as c
from random import randint
import copy

def RandomPiece(protein, p, startingpoint, sequence, start):
    
    directions = []
    last_coordinate = startingpoint
    
    for i in range(len(sequence)):

        # looks which directions are available
        directions = protein.grit.is_valid(last_coordinate[0], last_coordinate[1])

        # if there are free directions, pick one and place the amino acid there
        if len(directions) > 0 :

            # place the amino acid on the correct coordinates
            direction = directions[randint(0, len(directions) - 1)]
            protein.coordinates[p + i] = [last_coordinate[0] + direction[0], last_coordinate[1] + direction[1]]
            protein.grit.grit[protein.coordinates[p + i][0]][protein.coordinates[p + i][1]] = sequence[i]

            # place the correct connection on the correct position
            connection = [int((last_coordinate[0] + protein.coordinates[p + i][0]) / 2), int((last_coordinate[1] + protein.coordinates[p + i][1]) / 2)]
            if not start :
                if connection[0] != last_coordinate[0]:
                    protein.grit.grit[connection[0]][connection[1]] = '|'
                else:
                    protein.grit.grit[connection[0]][connection[1]] = '-'
            start = False

            # change the last coordinate
            last_coordinate = protein.coordinates[p + i]

        # otherwise, give up and return a score of 0
        else :
            return 1.0
        
    return protein.folded_score()

def RandomPiece_n(protein, n, startingpoint, stepsize):

    protein.grit.reset()
    
    #instantiate variables
    best_protein = protein
    best_score = 0
    temp_protein = protein
    steps = protein.length // stepsize
    if steps*stepsize != protein.length:
        steps += 1
    startingpoint = [2*protein.length + 3, 2*protein.length + 3]
    
    for i in range(steps):
        
        if i != 0:
            p = i*stepsize - 1
            startingpoint = protein.coordinates[p]
            
        
        for j in range(n):
            
            temp_protein.grit.reset()
            if i != 0:
                for k in range(p+1):
                    temp_protein.coordinates[k] = protein.coordinates[k]
                sequence = protein.sequence[0:p+1]
                coordinates = temp_protein.coordinates[0:p+1]
                coordinates_to_grit(temp_protein, sequence, coordinates)
            
            if i == 0:
                sequence = protein.sequence[i*stepsize : (i+1)*stepsize]
                score = RandomPiece(temp_protein, 0, startingpoint, sequence, True)
        
            elif i != steps - 1:
                sequence = protein.sequence[i*stepsize : (i+1)*stepsize]
                score = RandomPiece(temp_protein, p, startingpoint, sequence, False) 
                if j == 0 :
                    print(p,startingpoint,sequence)

            elif i == steps - 1:
                sequence = protein.sequence[i*stepsize : protein.length]
                score = RandomPiece(temp_protein, p, startingpoint, sequence, False)
                
            
            if score <= best_score:
                best_protein = copy.deepcopy(temp_protein)
                best_score = score
                
        protein = copy.deepcopy(best_protein)
        
    return best_protein, best_score



def coordinates_to_grit(protein, sequence, coordinates):
        for i in range(len(coordinates)):
            protein.grit.grit[coordinates[i][0]][coordinates[i][1]] = sequence[i]
    
    

