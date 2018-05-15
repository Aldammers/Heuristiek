
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

    # function to reveal the sequence of the protein
    def reveal(self):
        for j in self.sequence:
            print(j[0], end='-')
        print()

    # function to return the score of a protein when folded
    def folded_score(self):
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
    
    
    def upper_bound(self):
        upper_bound = 0
        if self.sequence[0] == 'H':
            upper_bound += 3
        if self.sequence[self.length] == 'H':
            upper_bound += 3
        for i in range(self.length - 3):
            if self.sequence[i + 1] == 'H':
                upper_bound += 2
        upper_bound = upper_bound//2 - 4
        return upper_bound

    
    def directions_to_coordinates(self, directions):
        self.directions = directions
        self.coordinates[0] = [(4*self.length + 9) // 2, (4*self.length + 9) // 2]
        i = 1
        for direction in directions:

            self.coordinates[i] = [self.coordinates[i - 1][0] + 2*direction[0], self.coordinates[i - 1][1] + 2*direction[1]]
            i += 1

    def fill_grit(self):

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

    def ez_score(self):
        score = 0

        def invert(direction):
            new_direction = [0,0]
            new_direction[0] = - 2 * direction[0]
            new_direction[1] = - 2 * direction[1]
            return new_direction

        def fuck_stan(direction):
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
                    if not tile in (invert(self.directions[i - 1]), fuck_stan(self.directions[i])):
                        if self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'C' or self.grit.grit[cursor[0] + tile[0]][cursor[1] + tile[1]] == 'H':
                            score += 1

            elif self.sequence[i] == 'C':
                for tile in surrounding:
                    if not tile in (invert(self.directions[i - 1]), fuck_stan(self.directions[i])):
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

    def is_valid(self, m, n):
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
