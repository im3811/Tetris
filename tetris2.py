EMPTY_SPOT = '\033[92m-\033[0m'
BLOCKER_SPOT = '\033[91mX\033[0m'
import random
import pygame


class Shape:
    def __init__(self, table):
        self.table = table
        self.position = None
        rows, cols = (6, 6)
        self.listt = [[EMPTY_SPOT] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(len(table[row])):
                if table[row][col] == 1:
                    self.listt[row][col] = '\033[94m\u25A0\033[0m'

    def print_matrix(self):
        print("    \033[92m0 1 2 3 4 5")
        print("   ------------")
        for row in range(0, 6):
            print(f"\033[92m{row} \033[92m|", end=" ")
            for col in range(0, 6):
                print(self.listt[row][col], end=" ")
            print("")

    def add_shape(self, shape, row, col):
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == 1:
                    self.listt[row + r][col + c] = '\033[94m\u25A0\033[0m'


class Puzzle:
    def __init__(self, shape, blocker_locations=None):
        self.shape_instance = Shape(shape)
        self.blocker_locations = blocker_locations or []

    def draw(self, locations):
        for row in range(len(locations)):
            for col in range(len(locations[0])):
                if locations[row][col] == 1:
                    self.shape_instance.listt[row][col] = '\033[94m\u25A0\033[0m'

        for blocker_location in self.blocker_locations:
            row, col = blocker_location
            self.shape_instance.listt[row][col] = BLOCKER_SPOT

    def import_matrix(self, locations):
        for location in locations:
            row, col = location
            self.shape_instance.listt[row][col] = '\033[94m\u25A0\033[0m'

    def print_matrix(self):
        self.shape_instance.print_matrix()


def modify_matrix(shape_1, blocker_locations, first_input, current_row):
    input_row = int(input("\033[92mInput the row of shape:\033[92m "))
    input_col = int(input("\033[92mInput the column of shape:\033[92m "))
    print("\n")

    if first_input and input_row != 0:
        print("\033[91mFirst move must be on row 0.\033[91m")
        return None

    if not first_input and input_row > current_row:
        print("\033[91myou can't skip rows.\033[91m")
        return None

    if (input_row, input_col) in blocker_locations:
        print("\033[91mYou hit a blocked spot.\033[91m")
        return None

    shape_1[input_row][input_col] = 1

    if input_row == 5:

        print("     \033[91mYOU WON!\033[91m\n")
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound("data/victory.mp3")
        sound.play()
        
        return shape_1
        
    return shape_1



def main():
    print("\n")
    print("\033[91mWelcome to the RGB Matrix enjoy your stay!\033[91m")
    shape_1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]


    blocker_locations = []
    max_traps = 12
    for row in range(6):
        traps_in_row = min(2, max_traps)
        max_traps -= traps_in_row
        while traps_in_row > 0:
            random_location = (row, random.randint(0, 5))
            if random_location not in blocker_locations:
                blocker_locations.append(random_location)
                traps_in_row -= 1



    current_position = (0, 0)
    puzzle1 = Puzzle(shape_1, blocker_locations)
    puzzle1.draw(shape_1) 
    puzzle1.print_matrix()
    
    first_input = True
    
    for current_row in range(36):
        result = modify_matrix(shape_1, blocker_locations, first_input, current_row)
        first_input = False
        if result is None:
            break
        puzzle1.draw(result)
        puzzle1.print_matrix()
        
    
   


    


if __name__ == "__main__":
    main()
