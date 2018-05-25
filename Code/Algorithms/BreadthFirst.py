from classes import *
import queue
import copy

def choose():

    file = open("data.txt","r")
    data = file.readlines()
    for i in range(len(data)):
        print(i + 1, data[i], end='')
    print()
    protein_number = int(input("Enter the number of he protein you wish to fold: "))
    if protein_number in range(1,10):
        proteinsequence = data[protein_number - 1]
        proteinsequence = proteinsequence.rstrip()
    return proteinsequence

def validate(directions, n):
    plain = [[0 for x in range(2*n - 1)] for y in range(2*n - 1)]
    options = []
    has_bend = False


    x, y = n - 1, n - 1

    plain[x][y] = 1

    for direction in directions:
        if direction == [1,0]:
            has_bend = True
        x, y = x + direction[0], y + direction[1]
        plain[x][y] = 1

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
        for i in range(width):

            directions = possibilities.get()

            options = validate(directions, n)

            width += len(options)

            for option in options:
                new_directions = copy.deepcopy(directions)
                new_directions.append(option)
                possibilities.put(new_directions)

        width -= old_width

    return possibilities

def convert_queue(sequence, possibilities):
    proteins = []
    while not possibilities.empty():

        directions = possibilities.get()
        protein = Protein(sequence)
        protein.directions = directions
        #protein.directions_to_coordinates()
        protein.fill_grit()
        proteins.append(protein)

    return proteins

def found_score(proteins):
    best_score = 0
    good_protein = Protein('H')
    good_proteins = []


    for protein in proteins:

        #protein.grit.reveal()

        score = protein.ez_score()

        if score < best_score:
            good_proteins = []
            best_score = score

            good_protein = copy.deepcopy(protein)
            good_proteins.append(good_protein)

        elif score == best_score:

            good_protein = copy.deepcopy(protein)
            good_proteins.append(good_protein)

    return best_score, good_proteins



# extention for piecewise method

def piecewisebreadth(length, progressions):

    possibilities = queue.Queue()
    for progression in progressions:
        possibilities.put(progression)
    width, n = len(progressions), len(progressions[0]) + 1

    for i in range(length):
        n += 1
        old_width = width
        for i in range(width):

            directions = possibilities.get()

            options = validate(directions, n)

            width += len(options)

            for option in options:
                new_directions = copy.deepcopy(directions)
                new_directions.append(option)
                possibilities.put(new_directions)

        width -= old_width

    return possibilities

def concatenate(concatenation, progressions, segments, initiated, sequence, n):
    if progressions == [] and not n == 0:
        print('All proceeding possibilities using this segmentation were exhausted, sawry.')
        return 'error'
    if initiated:
        if not concatenation == sequence:
            propagation = piecewisebreadth(len(segments[n-1]), progressions)
            proteins = convert_queue(concatenation, propagation)
            result = found_score(proteins)
            progressions = []
            for candidate in result[1]:
                progressions.append(candidate.directions)
            
            concatenation = concatenation + segments[n]
            return concatenate(concatenation, progressions, segments, initiated, sequence, n+1)

        else:
            print('done')
            propagation = piecewisebreadth(len(segments[n-1]), progressions)
            proteins = convert_queue(concatenation, propagation)
            result = found_score(proteins)
            return result

    else:
        print('1')
        initiation = breadth(len(concatenation))
        proteins = convert_queue(concatenation, initiation)
        result = found_score(proteins)
        for candidate in result[1]:
            progressions.append(candidate.directions)
        initiated = True
        concatenation = concatenation + segments[1]
        return concatenate(concatenation, progressions, segments, initiated, sequence, 2)


