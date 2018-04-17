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


class Grit:
    def __init__(self, size):
        self.grit = [['0' for x in range(size)] for y in range(size)]

    def reveal(self):
        for i in self.grit:
            for j in i:
                print(j, end='-')
            print()

    def change(self, i,j,v):
        self.grit[i][j] = v
