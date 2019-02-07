from Base_Cell import Base_Cell


class Gol_Cell:
    __radius = 1

    @classmethod
    def try_spawn(cls, neighbours):
        gol_cell_count = 0

        for row in neighbours:
            for cell in neighbours:
                if isinstance(cell, Gol_Cell):
                    gol_cell_count += 1

        if gol_cell_count == 3:
            return Gol_Cell()
