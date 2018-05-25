import classes as c
from random import randint
import copy

def RandomPiece(protein, p, startingpoint, sequence, start):
    ''' function which randomly folds a part of a protein '''
    
    # initiate variables
    directions = []
    last_coordinate = startingpoint
    if p == 0:
        protein.coordinates[0] = [startingpoint[0] + 2, startingpoint[1]]
        protein.grit.grit[protein.coordinates[0][0]][protein.coordinates[0][1]] = protein.sequence[0]
        last_coordinate = protein.coordinates[0]
    
    for i in range(len(sequence)):

        # looks which directions are available
        directions = protein.grit.isValid(last_coordinate[0], last_coordinate[1])

        # if there are free directions, pick one and place the amino acid there
        if len(directions) > 0 :

            # place the amino acid on the correct coordinates
            direction = directions[randint(0, len(directions) - 1)]
            protein.coordinates[p + i + 1] = [last_coordinate[0] + direction[0], last_coordinate[1] + direction[1]]
            protein.grit.grit[protein.coordinates[p + i + 1][0]][protein.coordinates[p + i + 1][1]] = sequence[i]

            # change the last coordinate
            last_coordinate = protein.coordinates[p + i + 1]

        # otherwise, give up and return a score of 0
        else :
            return 1.0
    protein.coordinatesToDirections()   
    protein.fillGrit()
    return protein.FoldedScore()

def RandomHalfsN(protein, n, startingpoint):
    ''' function which folds the halfs of a protein n times randomly 
    and returns the one with the best score'''

    # reset the grit of the protein
    protein.grit.reset()
    
    #instantiate variables
    stepsize = protein.length // 2
    best_protein = protein
    best_score = 0
    temp_protein = protein
    steps = 2
    
    for i in range(steps):
        
        # if you are doing the second half, change the startingpoint
        if i == 1:
            p = i*stepsize - 1
            startingpoint = protein.coordinates[p]
            
        
        for j in range(n):
            
            # reset the temporaray proteins grit
            temp_protein.grit.reset()
            
            # if its the second half, fill it with the first half
            if i == 1:
                for k in range(p+1):
                    temp_protein.coordinates[k] = protein.coordinates[k]
                sequence = protein.sequence[0:p+1]
                coordinates = temp_protein.coordinates[0:p+1]
                CoordinatesToGrit(temp_protein, sequence, coordinates)
            
            # randomfold the fist half
            if i == 0:
                sequence = protein.sequence[i*stepsize : (i+1)*stepsize]
                score = RandomPiece(temp_protein, 0, startingpoint, sequence, True)
        
            #randomfold the second half
            elif i == 1:
                sequence = protein.sequence[i*stepsize : protein.length]
                score = RandomPiece(temp_protein, p, startingpoint, sequence, False)
                
            # keep the score and folding if its the best one up to now
            if score <= best_score:
                best_protein = copy.deepcopy(temp_protein)
                best_score = score
                
        protein = copy.deepcopy(best_protein)
      
    return best_protein, best_score



def CoordinatesToGrit(protein, sequence, coordinates):
    ''' function which fills a grit of a protein if you give a list of 
    coordinates and a sequence to fill it with'''
    
    for i in range(len(coordinates)):
        protein.grit.grit[coordinates[i][0]][coordinates[i][1]] = sequence[i]
    
    

