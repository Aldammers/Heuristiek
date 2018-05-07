from classes import *
from BreadthFirst import *

protein = choose()
foldings = breadth(len(protein.sequence) - 1)
#while not foldings.empty():
#
#   folding = foldings.get()
#   print(folding)
proteins = convert_queue(protein.sequence, foldings)
result = found_score(proteins)
print(result)
