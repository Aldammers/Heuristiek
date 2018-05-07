from classes import *
import queue
import copy

def choose():
    protein = Protein('HHPHHHPH')
    file = open("data.txt","r")
    data = file.readlines()
    for i in range(len(data)):
        print(i + 1, data[i], end='')
    print()
    protein_number = int(input("Enter the number of he protein you wish to fold: "))
    if protein_number in range(1,10):
        protein = Protein(data[protein_number - 1])
    return protein




def validate(directions, n):
    plain = [[0 for x in range(2*n - 1)] for y in range(2*n - 1)]
    options = []
    has_bend = False


    x, y = n, n

    plain[x][y] = 1

    for direction in directions:
        if direction == [1,0]:
            has_bend = True
        x, y = x + direction[0], y + direction[1]
        plain[x][y] = 1

    #for i in range(len(plain)):
    #    print(plain[i])
    #print()

    if has_bend:
        if plain[x + 1][y] == 0:
            options.append([1,0])
        if plain[x - 1][y] == 0:
            options.append([-1,0])
        if plain[x][y + 1] == 0:
            options.append([0,1])
        if plain[x][y - 1] == 0:
            options.append([0,-1])
    else:
        options = [[0,1],[1,0]]
    return options



def breadth(length):

    possibilities = queue.Queue()
    width, n = 1, 2

    possibilities.put([[0,1]])
    for i in range(length - 2):
        n += 1
        old_width = width
        print(old_width)
        for i in range(width):

            directions = possibilities.get()

            options = validate(directions, n)

            width += len(options)

            for option in options:
                new_directions = copy.deepcopy(directions)
                new_directions.append(option)
                possibilities.put(new_directions)

        width -= old_width
        print(width)

    return possibilities

def convert_queue(sequence, possibilities):
    proteins = []
    while not possibilities.empty():

        directions = possibilities.get()
        protein = Protein(sequence)
        protein.directions_to_coordinates(directions)
        proteins.append(protein)

    return proteins

def found_score(proteins):
    best_score = 0

    for protein in proteins:

        score = protein.folded_score()
        if score < best_score:
            best_score = score
            best_protein = copy.deepcopy(protein)

    return score
