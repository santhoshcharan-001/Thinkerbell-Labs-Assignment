# importing the modules required
import random
import os
import msvcrt

# function to clear the terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# class which contains controls and positions of the rabbit, hole and carrot 
class Game:
    # constructor to create map
    def __init__(self):
        self.map=['-']*47
        self.map+=['O','r','c']
        random.shuffle(self.map)
        self.rabbit_pos = self.map.index('r')
        self.hole_pos = self.map.index('O')
        self.carrot_pos = self.map.index('c')
        self.has_carrot=False
    
    # function when player want to move left
    def move_left(self):
        if self.rabbit_pos==0:
            return 
        else:
            if self.rabbit_pos-1 == self.hole_pos:
                return 
            elif self.rabbit_pos-1 == self.carrot_pos:
                return 
            else:
                if self.has_carrot == True:
                    self.rabbit_pos = self.rabbit_pos-1
                    self.map[self.rabbit_pos] = "R"
                    self.map[self.rabbit_pos+1]='-'
                else:
                    self.rabbit_pos = self.rabbit_pos-1
                    self.map[self.rabbit_pos] = "r"
                    self.map[self.rabbit_pos+1]='-'

    # function when player want to move right
    def move_right(self):
        if self.rabbit_pos==49:
            return 
        else:
            if self.rabbit_pos+1==self.hole_pos:
                return 
            elif self.rabbit_pos+1==self.carrot_pos:
                return 
            else:
                if self.has_carrot == True:
                    self.rabbit_pos = self.rabbit_pos+1
                    self.map[self.rabbit_pos],self.map[self.rabbit_pos-1] = self.map[self.rabbit_pos-1],self.map[self.rabbit_pos]

                else:
                    self.rabbit_pos = self.rabbit_pos+1
                    self.map[self.rabbit_pos] = "r"
                    self.map[self.rabbit_pos-1]='-'
    
    # function when player want to jump
    def jump(self):
        if self.rabbit_pos+1==self.hole_pos:
            if self.rabbit_pos+2<=49:
                self.rabbit_pos+=2
                self.map[self.rabbit_pos],self.map[self.rabbit_pos-2]=self.map[self.rabbit_pos-2],self.map[self.rabbit_pos]
            else:
                return 
        elif self.rabbit_pos-1 == self.hole_pos:
            if self.rabbit_pos-2>=0:
                self.rabbit_pos-=2
                self.map[self.rabbit_pos],self.map[self.rabbit_pos+2]=self.map[self.rabbit_pos+2],self.map[self.rabbit_pos]
            else:
                return 
        else:
            return
    
    # function when player enters 'p'
    def pick(self):
        if self.rabbit_pos+1==self.carrot_pos:
            self.map[self.rabbit_pos]='R'
            self.map[self.rabbit_pos+1]='-'
            self.has_carrot=True
            self.carrot_pos=100
        elif self.rabbit_pos-1 == self.carrot_pos:
            self.map[self.rabbit_pos]='R'
            self.map[self.rabbit_pos-1]='-'
            self.has_carrot=True
            self.carrot_pos=100
        elif self.rabbit_pos+1==self.hole_pos:
            print("You Won!!!")
            return True
        elif self.rabbit_pos-1==self.hole_pos:
            print("You Won!!!")
            return True
        else:
            return False


    # function called when player wanted to play the game
    def start(self):
        while True:
            clear_screen()
            print("".join(self.map))
            player_input = msvcrt.getch().decode("utf-8")
            if player_input == 'a':
                self.move_left()
            elif player_input == 'd':
                self.move_right()
            elif player_input == 'j':
                self.jump()
            elif player_input == 'p':
                if self.pick():
                    break
                else:
                    continue
            else:
                break

print("""--------------------------------
Welcome to the Rabbit Hole Game!
You are a rabbit who has to get a carrot from the other side of the field.
You can move left and right using the 'a' and 'd' keys.
You can pick up the carrot using the 'p' key.
You can jump across the rabbit hole using the 'j' key.
You can drop the carrot at the rabbit hole using the 'p' key.
--------------------------------""")
input("Press enter to start the game...")
while True:    
    g = Game()
    g.start()
    if input("Do you want to play again? (y/n):") == "n":
        break
