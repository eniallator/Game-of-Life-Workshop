from src.GOL import GOL
from src.Axiom_Parser import Axiom_Parser
from src.Engine import Engine

# GOL = GOL(15, 15)
# AXIOMS = Axiom_Parser()

# with open('axioms.txt', 'r') as file_handle:
#     AXIOMS.parse(file_handle.read())

# from src.Cells.Gol_Cell import Gol_Cell
# GOL.set_sequence([
#     [None, Gol_Cell(), None],
#     [None, Gol_Cell(), Gol_Cell()],
#     [Gol_Cell(), Gol_Cell(), None]
# ])

# GOL.draw()


def main():
    # for i in range(3):
    #     GOL.update()
    #     GOL.draw()
    engine = Engine()
    engine.run()


if __name__ == '__main__':
    main()
