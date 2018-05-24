from classes import *
from BreadthFirst import *
import timeit

proteinsequence = choose()
print(proteinsequence)

start = timeit.default_timer()
foldings = breadth(len(proteinsequence))

proteins = convert_queue(proteinsequence, foldings)

result = found_score(proteins)
print(result[0])
for protein in result[1]:
    protein.grit.reveal()

stop = timeit.default_timer()
print("Runtime:", stop - start, "seconds")
