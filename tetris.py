EMPTY_SPOT = '-'
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
        print("    \033[1;32m0 1 2 3 4 5")
        print("   \033[1;32m------------")
        for row in range(0, 6):
            print(f"{row} |", end=" ")
            for col in range(0, 6):
                print(self.listt[row][col], end=" ")
            print("")

    def get_table(self):
        return self.table
    
    def __str__(self) -> str:
        return f"{self.table} {self.position}"
    
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

def modify_matrix(shape_1,blocker_locations,current_position):
    input1 = int(input("Input the row of shape: "))
    input2 = int(input("Input the column of shape: "))
    print("\n")
    
    
    if (input1, input2) in blocker_locations:
        print("You lost! Hit a blocked spot.")
        return None
    
    if abs(input1 - current_position[0]) > 5:
        print("Invalid move! You cannot skip rows.")
        return None
    
    shape_1[input1][input2] = 1

    if input1 == 5:
        print("     You won!\n")
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound("data/victory.mp3")
        sound.play()
        pygame.mixer.music.set_volume(0.1)
        
         
        return shape_1
    return shape_1


def play_music():
    pygame.init()
    pygame.mixer.init()
    #sound = pygame.mixer.Sound("data/tetris.ogg")
    #sound.play()

def main():
    play_music()
    

    
    shape_1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    
    blocker_locations = []
    while len(blocker_locations) < 10:
        random_location = (random.randint(0,5), random.randint(0,5))
        if random_location not in blocker_locations:
            blocker_locations.append(random_location)

    current_position = (0,0)
    puzzle1 = Puzzle(shape_1,blocker_locations ) #blocker_locations
    puzzle1.draw(shape_1)
    puzzle1.print_matrix()


    
    while True:
        
        result = modded_matrix = modify_matrix(shape_1,blocker_locations,current_position)
        if modded_matrix is None:
            break   
        puzzle1 = Puzzle(modded_matrix, blocker_locations)  
        puzzle1.draw(modded_matrix)
        puzzle1.print_matrix()

        

   
    
    


if __name__ == "__main__":
    main()
