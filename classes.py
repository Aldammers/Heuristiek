# aanpassingen aangeven



class Protein:
    def __init__(self, sequence):
        self.sequence = []
        self.grit = Grit(2*len(sequence) + 1)
        for i in range(len(sequence)):
            self.sequence.append([sequence[i], [0,0]])

    def reveal(self):
        for j in self.sequence:
            print(j[0], end='-')
        print()

    def folded_score(self):
        correction = 0
        for i in range(len(self.sequence) - 1):
            if self.sequence[i][0] == self.sequence[i + 1][0]:
                if self.sequence[i][0] == 'H' :
                    correction += 1
        return self.grit.score() - correction



class Grit:
    def __init__(self, size):
        self.grit = [['0' for x in range(size)] for y in range(size)]
        self.size = size

    def reveal(self):
        for i in self.grit:
            for j in i:
                print(j, end='-')
            print()
        print()

    def reset(self):
        self.grit = [['0' for x in range(self.size)] for y in range(self.size)]

    def score(self):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.grit[i][j] == 'H':
                    if self.grit[i+1][j] == 'H':
                        score += 1
                    if self.grit[i-1][j] == 'H':
                        score += 1
                    if self.grit[i][j+1] == 'H':
                        score += 1
                    if self.grit[i][j-1] == 'H':
                        score += 1
        return score/2
