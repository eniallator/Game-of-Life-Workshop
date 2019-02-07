from src.Cells.Base_Cell import Base_Cell

CELL_TYPES = []


class Game:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__grid = []

        for j in range(height):
            row = [None for i in range(width)]
            self.__grid.append(row)

    def __get_neighbours(self, cell_x, cell_y, radius):
        neighbours = []

        for y in range(2 * radius + 1):
            neighbours.append([])
            for x in range(2 * radius + 1):
                grid_y = cell_y - radius + y
                grid_x = cell_x - radius + x

                if 0 <= grid_y < self.__height and 0 <= grid_x < self.__width:
                    neighbours[y][x] = self.__grid[grid_x][grid_y]

        return neighbours

    def set_sequence(self, axiom):
        for y, row in enumerate(axiom):
            for x, cell in enumerate(row):
                cell_y = (self.__height / 2) - (len(axiom) / 2) + y
                cell_x = (self.__width / 2) - (len(axiom) / 2) + x

                self.__grid[cell_y][cell_x] = cell

    def __try_spawn(self, x, y):
        for cell_type in CELL_TYPES:
            neighbours = self.__get_neighbours(x, y, cell_type.get_radius())
            cell_type.try_spawn(neighbours)

    def update(self):
        for y, row in enumerate(self.__grid):
            for x, cell in enumerate(row):
                if cell is not None and Base_Cell in cell.__bases__:
                    cell.update()
                elif cell is None:
                    self.__try_spawn(x, y)

    def draw(self):
        for row in self.__grid:
            for cell in row:
                if cell is not None and Base_Cell in cell.__bases__:
                    cell.draw()
