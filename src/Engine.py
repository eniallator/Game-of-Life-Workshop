from time import sleep
from src.Game_Graphics import Game_Graphics
from src.GOL import GOL
from src.Cells.Gol_Cell import Gol_Cell


class Engine:
    def __init__(self, gol_grid_dim=(80, 60), screen_dim=(800, 600)):
        self.__graphics = Game_Graphics(*screen_dim)
        self.__GOL = GOL(*gol_grid_dim)

    def run(self):
        self.__GOL.set_sequence([
            [None, Gol_Cell(), None],
            [None, Gol_Cell(), Gol_Cell()],
            [Gol_Cell(), Gol_Cell(), None]
        ])
        self.__GOL.update()
        self.__GOL.draw(self.__graphics)
        sleep(1)
