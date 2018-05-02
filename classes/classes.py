# aanpassingen aangeven


# protein class
class Protein:

    #instantiate the grit and the sequence
    def __init__(self, sequence):
        self.sequence = sequence
        self.coordinates = []
        self.grit = Grit(4*len(sequence) + 9)
        for i in range(len(sequence)):
            self.coordinates.append([0,i])

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

    def max_score(self):
        max = 0
        if self.sequence[0] == 'H':
            max += 3
        if self.sequence[len(self.sequence)] == 'H':
            max += 3
        for i in range(len(self.sequence) - 3):
            if self.sequence[i + 1] == 'H':
                max += 2
        max = max//2
        return max


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

    # function to determine the score of a grit (the protein on it to be precise)
    def score(self):
        score = 0
        for i in range(3, self.size - 2, 2):
            for j in range(3, self.size - 2, 2):

                # check for any bonds
                if self.grit[i][j] != 'P' and self.grit[i][j] != ' ':
                    if self.grit[i+2][j] != 'P' and self.grit[i+2][j] != ' ':
                        score += 0.5
                    if self.grit[i-2][j] != 'P' and self.grit[i-2][j] != ' ':
                        score += 0.5
                    if self.grit[i][j+2] != 'P' and self.grit[i][j+2] != ' ':
                        score += 0.5
                    if self.grit[i][j-2] != 'P' and self.grit[i][j-2] != ' ':
                        score += 0.5

                # check for C-C bonds
                if self.grit[i][j] == 'C':
                    if self.grit[i+2][j] == 'C':
                        score += 2
                    if self.grit[i-2][j] == 'C':
                        score += 2
                    if self.grit[i][j+2] == 'C':
                        score += 2
                    if self.grit[i][j-2] == 'C':
                        score += 2

        return score

    # function to check which neighbours are free
    def is_valid(self,m,n):
        directions = []
        if self.grit[m][n+2] == ' ':
            directions.append([0,2])
        if self.grit[m][n-2] == ' ':
            directions.append([0,-2])
        if self.grit[m-2][n] == ' ':
            directions.append([-2,0])
        if self.grit[m+2][n] == ' ':
            directions.append([2,0])
        return directions
