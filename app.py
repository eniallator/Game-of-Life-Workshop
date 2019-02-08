from src.Game import Game
from src.Axiom_Parser import Axiom_Parser

GAME = Game(15, 15)
AXIOMS = Axiom_Parser()

with open('axioms.txt', 'r') as file_handle:
    AXIOMS.parse(file_handle.read())

from src.Cells.Gol_Cell import Gol_Cell
GAME.set_sequence([
    [None, Gol_Cell(), None],
    [None, Gol_Cell(), Gol_Cell()],
    [Gol_Cell(), Gol_Cell(), None]
])

GAME.draw()


def main():
    for i in range(3):
        GAME.update()
        GAME.draw()


if __name__ == '__main__':
    main()
