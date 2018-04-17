# aanpassingen aangeven

class Protein:
    def __init__(self, sequence):
        self.sequence = []
        for i in range(len(sequence)):
            self.sequence.append(sequence[i])

    def reveal(self):
        for j in range(len(self.sequence) - 1):
            print(self.sequence[j][0], end='-')
        print(self.sequence[len(self.sequence) - 1][0])
        
    def length(self):
        print(len(self.sequence))

class Grit:
    def __init__(self, size):
        self.grit = []
        row = []
        for i in range(size):
            row.append('0')
        for j in range(size):
            self.grit.append(row)
			
    def reveal(self):
        for i in self.grit:
            for j in i:
                print(j, end='-')
            print()
