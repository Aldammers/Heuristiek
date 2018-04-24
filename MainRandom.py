from classes import *
from RandomFold import *
import cs50

# get the needed user input
protein_string = cs50.get_string('Protein: ')
n = cs50.get_int('Fold how many times: ')
print()

# fold the given protein n times
myProtein = Protein(protein_string)
Random_n(myProtein, n)
print("This is the folding with the best score of the", n, " we tried!")
