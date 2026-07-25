import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves) 
        print(f"choice {move}")
        x, y = self.position
        print(f"position (x,y) :{x},{y}")
        dx ,dy = move
        self.position =  (x + dx, y + dy)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]

    def level_up(self):
        self.moves.extend([
        (-1,-1),  # <^
        (-1,1),   # ^>
        (1,-1),   # <v
        (1,1)     # v>
    ])

player1 = Pawn()

# moves = [
#     (-1,0), # ^
#     (1,0), # v
#     (0,1), # >
#     (0,-1) # <
#     ]
# player1.moves = moves
print(player1.make_move())
print(player1.make_move())
print("\033[33mTest length of moves:\033[0m",player1.moves)
player1.level_up()
print("\033[33mTest length of moves:\033[0m",len(player1.moves))
print(player1.make_move())
print(player1.make_move())
