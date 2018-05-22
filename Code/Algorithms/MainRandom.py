import classes as c
import RandomFold as rf


# get the needed user input
protein_string = input('Protein: ')
n = input('Fold how many times: ')
n = int(n)
print()

# fold the given protein n times
myProtein = c.Protein(protein_string)
startingpoint = [2*len(myProtein.sequence) + 3, 2*len(myProtein.sequence) + 3]
results = rf.Random_n(myProtein, n, startingpoint)

results[0].grit.reveal()
print('Score: ', results[1])
print("This is the folding with the best score of the", n, " we tried!")
