# protein class
class Protein:

    #instantiate the grit and the sequence
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)
        self.coordinates = []
        self.directions = []
        self.grit = Grit(4*self.length + 9)
        for i in range(self.length):
            self.coordinates.append([0,i])


    # function to return the score of a protein when folded
    def FoldedScore(self):
        correction = 0
        for i in range(self.length - 1):
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


    # fill in the amino acids at the right coordinates
    def fillGrit(self):

        self.grit.reset()
        cursor = [self.grit.size // 2, self.grit.size // 2]

        for i in range(self.length - 1):

            self.grit.grit[cursor[0]][cursor[1]] = self.sequence[i]
            if self.directions[i][0] == 0:
                self.grit.grit[cursor[0] + self.directions[i][0]][cursor[1]  + self.directions[i][1]] = '-'
            else:
                self.grit.grit[cursor[0] + self.directions[i][0]][cursor[1]  + self.directions[i][1]] = '|'

            cursor[0] = cursor[0] + 2 * self.directions[i][0]
            cursor[1] = cursor[1] + 2 * self.directions[i][1]
        j = self.length - 1
        self.grit.grit[cursor[0]][cursor[1]] = self.sequence[j]
        
    def coordinatesToDirections(self):
        self.directions = []
        for i in range(self.length - 1):
            direction0 = (self.coordinates[i+1][0] - self.coordinates[i][0]) // 2
            direction1 = (self.coordinates[i+1][1] - self.coordinates[i][1]) // 2
            direction = [direction0, direction1]
            self.directions.append(direction)

    # calculate the score, ireating over the folded protein
    def ezScore(self):
        score = 0

        def invert(direction):
            new_direction = [0,0]
            new_direction[0] = - 2 * direction[0]
            new_direction[1] = - 2 * direction[1]
            return new_direction

        def normalise(direction):
            new_direction = [0,0]
            new_direction[0] = 2 * direction[0]
            new_direction[1] = 2 * direction[1]
            return new_direction

        surrounding = [[0,2],[2,0],[0,-2],[-2,0]]
        cursor = [self.grit.size // 2, self.grit.size // 2]

        if self.sequence[0] == 'H':
            for tile in surrounding:
                if not tile == [0,2]:
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C' or self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                        score += 1

        elif self.sequence[0] == 'C':
            for tile in surrounding:
                if not tile == [0,2]:
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C':
                        score += 5
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                        score += 1


        cursor[0] = cursor[0] + 2 * self.directions[0][0]
        cursor[1] = cursor[1] + 2 * self.directions[0][1]


        for i in range(1, self.length - 1):
            if self.sequence[i] == 'H':
                for tile in surrounding:
                    if not tile in (invert(self.directions[i - 1]), normalise(self.directions[i])):
                        if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C' or self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                            score += 1

            elif self.sequence[i] == 'C':
                for tile in surrounding:
                    if not tile in (invert(self.directions[i - 1]), normalise(self.directions[i])):
                        if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C':
                            score += 5
                        if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                            score += 1

            cursor[0] = cursor[0] + 2 * self.directions[i][0]
            cursor[1] = cursor[1] + 2 * self.directions[i][1]

        if self.sequence[self.length - 1] == 'H':
            for tile in surrounding:
                if not tile == invert(self.directions[self.length - 2]):
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C' or self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                        score += 1

        elif self.sequence[self.length - 1] == 'C':
            for tile in surrounding:
                if not tile == invert(self.directions[self.length - 2]):
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C':
                        score += 5
                    if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                        score += 1

        return -score//2

    def segmentise(self, argument, method):
        if method == 'default':
            segment_size = argument
            segments = []
            c = 0
            while c < len(self.sequence) - segment_size:
                segments.append(self.sequence[c:c+segment_size])
                c += segment_size
            segments.append(self.sequence[c:len(self.sequence)])
            return segments

        elif method == 'manual':
            segments = argument
            return segments

        elif method == 'cleverly':
            segment = self.sequence[0]
            H = self.sequence.count('H')
            P = self.sequence.count('P')
            segments = []
            c = 0
            for i in range(self.length):
                segment = self.sequence[c:i]
                partialH = segment.count('H')
                partialP = segment.count('P')
                if i - c > 7:
                    segments.append(segment)
                    c = i
                elif H * partialP >= P * partialH:
                    segments.append(segment)
                    c = i
            return segments



# Grit class
class Grit:

    # instantiate the grit with correct size
    def __init__(self, size):
        self.grit = [[' ' for x in range(size)] for y in range(size)]
        self.size = size

    # function which finds the place of the protein in the grit, so that no useless part of the grit gets printed
    def proteinPlace(self):
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
        self.proteinPlace()
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
        for i in range(2, self.size - 2, 2):
            for j in range(2, self.size - 2, 2):

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

    # determine which position surrounding an amino acid are still available
    def isValid(self, m, n):
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
