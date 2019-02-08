from src.Cells.Base_Cell import Base_Cell
from src.Cells.Gol_Cell import Gol_Cell

CELL_TYPES = [Gol_Cell]


class Game:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__grid = self.__gen_grid(width, height)

    def __gen_grid(self, width, height):
        grid = []

        for i in range(height):
            grid.append([None for j in range(width)])

        return grid

    def __get_neighbours(self, cell_x, cell_y, radius):
        neighbours = []

        for y in range(2 * radius + 1):
            neighbours.append([None for i in range(2 * radius + 1)])
            for x in range(2 * radius + 1):
                grid_y = cell_y - radius + y
                grid_x = cell_x - radius + x

                if 0 <= grid_y < self.__height and 0 <= grid_x < self.__width:
                    neighbours[y][x] = self.__grid[grid_y][grid_x]

        neighbours[radius][radius] = None
        return neighbours

    def set_sequence(self, axiom):
        for y, row in enumerate(axiom):
            for x, cell in enumerate(row):
                cell_y = int((self.__height / 2) - (len(axiom) / 2) + y)
                cell_x = int((self.__width / 2) - (len(axiom) / 2) + x)

                self.__grid[cell_y][cell_x] = cell

    def __try_spawn(self, x, y):
        for cell_type in CELL_TYPES:
            neighbours = self.__get_neighbours(x, y, cell_type.get_neighbour_radius())
            cell = cell_type.try_spawn(neighbours)
            if cell is not None:
                return cell

    def update(self):
        new_grid = self.__gen_grid(self.__width, self.__height)
        for y, row in enumerate(self.__grid):
            for x, cell in enumerate(row):
                if cell is not None and Base_Cell in cell.__class__.__bases__:
                    neighbours = self.__get_neighbours(x, y, cell.get_neighbour_radius())
                    cell.update(neighbours)
                    if not cell.is_dead:
                        new_grid[y][x] = cell
                elif cell is None:
                    new_cell = self.__try_spawn(x, y)
                    if new_cell is not None:
                        new_grid[y][x] = new_cell
        self.__grid = new_grid

    def draw(self):
        s = ''
        for row in self.__grid:
            s += '\n' if s else ''
            for cell in row:
                s += '#' if cell else ' '
                # if cell is not None and Base_Cell in cell.__bases__:
                #     cell.draw()
        print(s)
