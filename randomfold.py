from classes import *
from random import randint
import copy

# function to randomly fold a protein
def RandomFold(protein):

    # instantiate variables
    directions = []
    last_coordinate = [2*len(protein.sequence) + 3, 2*len(protein.sequence) + 3]
    coordinates = [last_coordinate]
    i = 0

    # for each amino acid in the protein, randomly go into a direction
    for amino in protein.sequence:
        directions = []

        # check which directions are free to go to
        if protein.grit.grit[last_coordinate[0] + 2][last_coordinate[1]] == ' ' :
            directions.append([2,0])

        if protein.grit.grit[last_coordinate[0] - 2][last_coordinate[1]] == ' ' :
            directions.append([-2,0])

        if protein.grit.grit[last_coordinate[0]][last_coordinate[1] + 2] == ' ' :
            directions.append([0,2])

        if protein.grit.grit[last_coordinate[0]][last_coordinate[1] - 2] == ' ' :
            directions.append([0,-2])

        # if there are free directions, pick one and place the amino acid there
        if len(directions) > 0 :

            # place the amino acid on the correct coordinates
            direction = directions[randint(0, len(directions) - 1)]
            amino[1] = [last_coordinate[0] + direction[0], last_coordinate[1] + direction[1]]
            protein.grit.grit[amino[1][0]][amino[1][1]] = amino[0]

            # place the connection on the correct coordinates
            if direction == [2,0]:
                connection = [1,0]
            elif direction == [-2,0]:
                connection = [-1,0]
            elif direction == [0,2]:
                connection = [0,1]
            else:
                connection = [0,-1]
            connection_place = [last_coordinate[0] + connection[0], last_coordinate[1] + connection[1]]
            if i != 0 :
                if connection[0] != 0:
                    protein.grit.grit[connection_place[0]][connection_place[1]] = '|'
                else:
                    protein.grit.grit[connection_place[0]][connection_place[1]] = '-'
            coordinates.append(amino[1])
            i += 1

            # change the last coordinate
            last_coordinate = amino[1]

        # otherwise, give up and return a score of 0
        else :
            return 0.0

    # return the score of the folded protein
    return protein.folded_score()

# function to randomly fold a protein n times
def Random_n(protein, n):

    # show the protein at the beginning
    protein.reveal()
    print("Folding...")
    print()

    # instantiate variables
    best_protein = protein
    best_score = 0

    # fold n times
    for i in range(n):
        protein.grit.reset()
        score = RandomFold(protein)

        # keep the score and folding if it is the best until now
        if score < best_score:
            best_score = score
            best_protein = copy.deepcopy(protein)

    # show the best folding and score
    print("Folding: ")
    best_protein.grit.reveal()
    print("Score: ", best_score)
