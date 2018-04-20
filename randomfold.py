from classes import *
from random import randint
import copy

def RandomFold(protein):
    directions = []
    last_coordinate = [len(protein.sequence) + 1, len(protein.sequence) +1]
    coordinates = [last_coordinate]
    for amino in protein.sequence:
        directions = []

        if protein.grit.grit[last_coordinate[0] + 1][last_coordinate[1]] == '0' :
            directions.append([1,0])

        if protein.grit.grit[last_coordinate[0] - 1][last_coordinate[1]] == '0' :
            directions.append([-1,0])

        if protein.grit.grit[last_coordinate[0]][last_coordinate[1] + 1] == '0' :
            directions.append([0,1])

        if protein.grit.grit[last_coordinate[0]][last_coordinate[1] -1 ] == '0' :
            directions.append([0,-1])

        if len(directions) > 0 :
            direction = directions[randint(0, len(directions) - 1)]
            amino[1] = [last_coordinate[0] + direction[0], last_coordinate[1] + direction[1]]
            last_coordinate = amino[1]
            protein.grit.grit[amino[1][0]][amino[1][1]] = amino[0]
            coordinates.append(amino[1])

        else :
            return 0.0
    return protein.folded_score()

def Random_n(protein, n):
    protein.reveal()
    best_protein = protein
    best_score = 0

    for i in range(n):
        protein.grit.reset()
        score = RandomFold(protein)
        if score < best_score:
            best_score = score
            best_protein = copy.deepcopy(protein)

    best_protein.grit.reveal()
    print(best_score)

myProtein = Protein('HHPHHHPH')
Random_n(myProtein, 10000)


    
