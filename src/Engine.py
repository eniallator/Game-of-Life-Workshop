from src.Game_Graphics import Game_Graphics
from src.GOL import GOL
from src.Cells.Gol_Cell import Gol_Cell


class Engine:
    def __init__(self, gol_grid_dim=(80, 60), screen_dim=(800, 600)):
        self.__graphics = Game_Graphics(*screen_dim)
        self.__GOL = GOL(*gol_grid_dim)

    def __run_func(self, dt):
        self.__counter += dt
        while self.__counter >= self.__update_delay:
            self.__GOL.update()
            self.__counter -= self.__update_delay
        self.__GOL.draw(self.__graphics)

    def run(self, update_delay=0.5):
        self.__GOL.set_sequence([
            [None, Gol_Cell(), None],
            [None, Gol_Cell(), Gol_Cell()],
            [Gol_Cell(), Gol_Cell(), None]
        ])
        self.__update_delay = update_delay
        self.__counter = 0
        self.__graphics.loop(self.__run_func)
