from re import finditer, MULTILINE
from src.Cells.Gol_Cell import Gol_Cell

CELL_KEYS = {
    '#': Gol_Cell
}


class Axiom_Parser:
    __axioms = {}

    def __init_axiom(self, axiom_string):
        axiom_list = []

        for line_num, line in enumerate(axiom_string.split('\n')):
            axiom_list.append([])
            for char in line:
                if char in CELL_KEYS:
                    axiom_list[line_num].append(CELL_KEYS[char]())
                else:
                    axiom_list[line_num].append(None)

        return axiom_list

    def parse(self, in_string):
        for match in finditer(r'(?P<axiom_name>\w+):.*$\n(?P<axiom>(^.+$\n?)+)', in_string, MULTILINE):
            self.__axioms[match.group('axiom_name')] = self.__init_axiom(match.group('axiom'))
        print(self.__axioms)

    def get_axiom_names(self):
        return list(self.__axioms.keys())

    def get_axiom(self, axiom_name):
        return self.__axioms[axiom_name]
