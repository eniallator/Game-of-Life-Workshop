from src.Cells.Base_Cell import Base_Cell


class Gol_Cell(Base_Cell):
    _neighbour_radius = 1

    @classmethod
    def try_spawn(cls, neighbours):
        gol_cell_count = 0

        for row in neighbours:
            for cell in row:
                if cell.__class__ == Gol_Cell:
                    gol_cell_count += 1

        if gol_cell_count == 3:
            return Gol_Cell()

    def update(self, neighbours):
        gol_cell_count = 0

        for row in neighbours:
            for cell in row:
                if cell.__class__ == Gol_Cell:
                    gol_cell_count += 1

        if gol_cell_count < 2 or gol_cell_count > 3:
            self._dead = True

    def draw(self, graphics, bounding_box):
        graphics.rect((255, 0, 0), bounding_box)
