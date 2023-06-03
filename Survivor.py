from Gameboard import Gameboard
class Survivor:
    def __init__(self, gameboard:Gameboard):
        self.gameboard = gameboard
        self.inventario_comida:str = []
        self.inventario_armas:str = []
        self.vida:int = 10
        self.icon:str = "😎"