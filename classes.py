# aanpassingen aangeven


# protein class
class Protein:

    #instantiate the grit and the sequence
    def __init__(self, sequence):
        self.sequence = []
        self.grit = Grit(4*len(sequence) + 9)
        for i in range(len(sequence)):
            self.sequence.append([sequence[i], [0,0]])

    # function to reveal the sequence of the protein
    def reveal(self):
        for j in self.sequence:
            print(j[0], end='-')
        print()

    # function to return the score of a protein when folded
    def folded_score(self):
        correction = 0
        for i in range(len(self.sequence) - 1):
            if self.sequence[i][0] == 'H':
                if self.sequence[i + 1][0] == 'H' :
                    correction += 1
                if self.sequence[i + 1][0] == 'C':
                    correction += 1
            if self.sequence[i][0] == 'C':
                if self.sequence[i + 1][0] == 'H' :
                    correction += 1
                if self.sequence[i + 1][0] == 'C':
                    correction += 5
        return correction - self.grit.score()


# Grit class
class Grit:

    # instantiate the grit with correct size
    def __init__(self, size):
        self.grit = [[' ' for x in range(size)] for y in range(size)]
        self.size = size

    # function which finds the place of the protein in the grit, so that no useless part of the grit gets printed
    def protein_place(self):
        self.top = self.size
        self.left = self.size
        self.right = 0
        self.bottom = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.grit[i][j] != ' ':
                    if i < self.top:
                        self.top = i
                    elif i > self.bottom:
                        self.bottom = i
                if self.grit[i][j] != ' ':
                    if j < self.left:
                        self.left = j
                    elif j > self.right:
                        self.right = j


    # show the grit
    def reveal(self):
        self.protein_place()
        for i in range(self.top - 1, self.bottom + 2):
            for j in range(self.left - 1, self.right + 2):
                print(self.grit[i][j], end=' ')
            print()
        print()

    # reset the grit to its initial state
    def reset(self):
        self.grit = [[' ' for x in range(self.size)] for y in range(self.size)]

    # function to determine the score of a grit(the protein on it to be precise)
    def score(self):
        score = 0
        for i in range(1, self.size, 2):
            for j in range(1, self.size, 2):

                # check for H-H bonds
                if self.grit[i][j] == 'H':
                    if self.grit[i+2][j] == 'H':
                        score += 0.5
                    if self.grit[i-2][j] == 'H':
                        score += 0.5
                    if self.grit[i][j+2] == 'H':
                        score += 0.5
                    if self.grit[i][j-2] == 'H':
                        score += 0.5

                # check for C-H bonds
                if self.grit[i][j] == 'C':
                    if self.grit[i+2][j] == 'H':
                        score += 1
                    if self.grit[i-2][j] == 'H':
                        score += 1
                    if self.grit[i][j+2] == 'H':
                        score += 1
                    if self.grit[i][j-2] == 'H':
                        score += 1

                # check for C-C bonds
                if self.grit[i][j] == 'C':
                    if self.grit[i+2][j] == 'C':
                        score += 2.5
                    if self.grit[i-2][j] == 'C':
                        score += 2.5
                    if self.grit[i][j+2] == 'C':
                        score += 2.5
                    if self.grit[i][j-2] == 'C':
                        score += 2.5



        return score
