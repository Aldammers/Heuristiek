from random import randint
import copy

# function to randomly fold a protein
def RandomFold(protein, startingpoint):

    # instantiate variables
    directions = []
    last_coordinate = startingpoint
    start = True

    # for each amino acid in the protein, randomly go into a direction
    for i in range(len(protein.sequence)):

        # looks which directions are available
        directions = protein.grit.is_valid(last_coordinate[0], last_coordinate[1])

        # if there are free directions, pick one and place the amino acid there
        if len(directions) > 0 :

            # place the amino acid on the correct coordinates
            direction = directions[randint(0, len(directions) - 1)]
            protein.coordinates[i] = [last_coordinate[0] + direction[0], last_coordinate[1] + direction[1]]
            protein.grit.grit[protein.coordinates[i][0]][protein.coordinates[i][1]] = protein.sequence[i]

            # place the correct connection on the correct position
            connection = [int((last_coordinate[0] + protein.coordinates[i][0]) / 2), int((last_coordinate[1] + protein.coordinates[i][1]) / 2)]
            if not start :
                if connection[0] != last_coordinate[0]:
                    protein.grit.grit[connection[0]][connection[1]] = '|'
                else:
                    protein.grit.grit[connection[0]][connection[1]] = '-'
            start = False

            # change the last coordinate
            last_coordinate = protein.coordinates[i]

        # otherwise, give up and return a score of 0
        else :
            return 0.0

    # return the score of the folded protein
    return protein.folded_score()

# function to randomly fold a protein n times
def Random_n(protein, n, startingpoint):

    # instantiate variables
    best_protein = protein
    best_score = 0

    # fold n times
    for i in range(n):
        protein.grit.reset()
        score = RandomFold(protein, startingpoint)

        # keep the score and folding if it is the best until now
        if score < best_score:
            best_score = score
            best_protein = copy.deepcopy(protein)

    # return the best folding and score
    return(best_protein, best_score)
