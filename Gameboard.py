import random


class GameBoard:
    def __init__(self, size:int) -> None:
        self.matrix:list = []
        self.size:int = size
        self.guns:list = ["🔫", "💣", "🔪", "🪃"]
        self.food:list = ["🍎", "🌭", "🍓", "🍺"]
        

        for i in range(self.size):
            self.matrix.append(['_']*self.size)

        for i in range(4):
            radom_position_i = random.randint(1,self.size-1)
            radom_position_j = random.randint(1,self.size-1)
            self.matrix[radom_position_i][radom_position_j] = random.choice(self.guns)

        for i in range(4):
            radom_position_i = random.randint(1,self.size-1)
            radom_position_j = random.randint(1,self.size-1)
            self.matrix[radom_position_i][radom_position_j] = random.choice(self.food)
        
    def add_player(self, player):
        radom_position_i = random.randint(1,self.size-1)
        radom_position_j = random.randint(1,self.size-1)
        self.matrix[radom_position_i][radom_position_j] = player



        



game = GameBoard(5)
for i in game.matrix:
    print(i) 
