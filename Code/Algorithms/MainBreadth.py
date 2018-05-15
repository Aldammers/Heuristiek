from classes import *
from BreadthFirst import *

proteinsequence = choose()
print(proteinsequence)
foldings = breadth(len(proteinsequence))

proteins = convert_queue(proteinsequence, foldings)

result = found_score(proteins)
print(result[0])
for protein in result[1]:
    protein.grit.reveal()
