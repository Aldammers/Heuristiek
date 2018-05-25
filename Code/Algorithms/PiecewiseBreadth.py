from classes import *
from BreadthFirst import *

proteinsequence = choose()
invalid = True
while invalid:
    argument = int(input("Enter a reasonable segment size: "))
    if argument < 1:
        print("This segment size is not reasonable, please enter a larger number.")
    elif argument > 10:
        print("This segment size is not reasonable, please enter a smaller number.")
    else:
        invalid = False

protein = Protein(proteinsequence)
segments = protein.segmentise(argument, 'default')
print(segments)


result = concatenate(segments[0], [], segments, False, protein.sequence, 0)

if not result == 'error':
    file = open("piecewisedirections.txt", "a")
    file.write(proteinsequence)
    file.write(', segmentation argument: ')
    strargument = str(argument)
    file.write(strargument)
    file.write('\n')
    for protein in result[1]:
        directions = str(protein.directions)
        file.write(directions)
        file.write('\n')
    file.close()
    print(result[0])

    for protein in result[1]:
        protein.grit.reveal()
