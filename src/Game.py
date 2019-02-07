from Base_Cell import Base_Cell


class Game:

    def __init__(self, width, height):
        self.__grid = []
        for j in range(height):
            row = [None for i in range(width)]
            self.__grid.append(row)

    def update(self):
        for row in self.__grid:
            for cell in row:
                if cell is not None and Base_Cell in cell.__bases__:
                    cell.update()

    def draw(self):
        for row in self.__grid:
            for cell in row:
                if cell is not None and Base_Cell in cell.__bases__:
                    cell.draw()
