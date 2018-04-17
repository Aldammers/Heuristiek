class Protein:
    def __init__(self, sequence):
        self.sequence = []
        for i in range(len(sequence)):
            self.sequence.append(sequence[i])

    def reveal(self):
        for j in range(len(self.sequence) - 1):
            print(self.sequence[j][0], end='-')
        print(self.sequence[len(self.sequence) - 1][0])

myProtein = Protein('HHPHPHPP')
myProtein.reveal()

class Grit:
    def __init__(self):
        self.grit = []