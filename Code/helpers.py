import classes as c
import RandomFold as rf
import RandomPiecewise as rp
import BreadthFirst as bf
import timeit as t

def ChooseProtein():

    # open the file with proteins and display them
    file = open("data.txt","r")
    data = file.readlines()
    for i in range(len(data)-1):
        print(i + 1, data[i], end='')
    
    # also give the user an option to input another protein    
    print(10, "Input another protein")
    
    # Let the user choose a protein
    print()
    protein_number = input("Enter the number of he protein you wish to fold: ")
    while not checkInt(protein_number):
        protein_number = input("That is not a number, try again: ")
    protein_number = int(protein_number)
    while protein_number not in range(1,11):
        protein_number = input("No protein with that number, try again: ")
        while not checkInt(protein_number):
            protein_number = input("That is not a number, try again: ")
        protein_number = int(protein_number)
        
    # if they pick one from the list, use that one 
    if protein_number in range(1,10):
        proteinsequence = data[protein_number - 1]
        proteinsequence = proteinsequence.rstrip()
    
    # otherwise check if it is a valid sequence
    elif protein_number == 10:
        good = False
        aminoacids = ["H", "C", "P"]
        proteinsequence = input("Give your proteinsequence: ")
        while not good:
            for i in range(len(proteinsequence)):
                if proteinsequence[i] not in aminoacids:
                    proteinsequence = input("Not a valid sequence, try again: ")
                    break
                if i == len(proteinsequence) - 1:
                    good = True
        
    return proteinsequence

def ChooseAlgortihm(proteinsequence):
    
    # initiate your list of algorithms
    algorithms = ['RandomFold', 'RandomHalfs', 'Breadthfirst', 'PiecewiseBreadth']

    # display the alforithms
    print()
    for i in range(len(algorithms)):
        print(i+1, algorithms[i])
    
    # let the user pick an algorithm    
    algorithm = input("Which algorithm would you like to use: ")
    while not checkInt(algorithm):
        algorithm = input("That is not a number, try again: ")
    algorithm = int(algorithm)
    while algorithm not in range(1, len(algorithms) + 1):
        algorithm = input("Wrong number, try again: ")
        while not checkInt(algorithm):
            algorithm = input("That is not a number, try again: ")
        algorithm = int(algorithm)
    
    # RandomFold        
    if algorithm == 1:
        
        # ask how many times 
        n = input("How many times do you wish to fold the protein: ")
        while not checkInt(n):
            n = input("That is not a number, try again: ")
        n = int(n)
        
        start = t.default_timer()
        protein = c.Protein(proteinsequence)
        
        # let the startingpoint be in the middle of the grit
        startingpoint = [2 * protein.length + 4, 2 * protein.length + 4]
        
        # randomfold the protein n times
        results = rf.RandomN(protein, n, startingpoint)
        stop = t.default_timer()
        
        # show the results
        results[0].grit.reveal()
        print('Score: ', results[1])
        print("This is the folding with the best score of the", n, "foldings we tried!")
        print("It took", stop - start, "seconds.")
    

    # RandomHalfs
    elif algorithm == 2:
        
        # ask how many times 
        n = input("How many times do you wish to fold the protein: ")
        while not checkInt(n):
            n = input("That is not a number, try again: ")
        n = int(n)
        
        start = t.default_timer()
        protein = c.Protein(proteinsequence)
        
        # let the startingpoint be in the middle of the grit
        startingpoint = [2 * protein.length + 2, 2 * protein.length + 2]
        
        # randomfold the halfs n times
        results = rp.RandomHalfsN(protein, n, startingpoint)
        stop = t.default_timer()
        
        # show the results
        results[0].grit.reveal()
        print("This is the best folding of the", n, "times we tried, the score is:", results[1])
        print("It took", stop - start, "seconds.")
    
    # BreadthFirst
    elif algorithm == 3:
        
        # use breadthfirst on your protein
        start = t.default_timer()
        foldings = bf.breadth(len(proteinsequence))
        proteins = bf.convert_queue(proteinsequence, foldings)
        
        # show the results
        result = bf.found_score(proteins)
        stop = t.default_timer()
        for protein in result[1]:
            protein.grit.reveal()
        print("The best possible score for this protein is", result[0], "and these are all the best foldings there are.")
        print("It took", stop - start, "seconds.")
    
    #PiecewiseBreadth
    #elif algorithm == 4:
        
        
def checkInt(string):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(string)):
        if string[i] not in numbers:
            return False
    return True

