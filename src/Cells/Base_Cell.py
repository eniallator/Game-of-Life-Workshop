class Base_Cell:
    """The base class for all cell types"""
    __state = 0
    __radius = 1

    @classmethod
    def try_spawn(cls, neighbours):
        raise Exception('Error: ' + cls.__name__ + ' implemented a try_spawn method yet.')

    @classmethod
    def get_radius(cls):
        """Gets the radius for how many neighbours per cell"""
        return cls.__radius

    @property
    def state(self):
        """Gets the current state of the cell"""
        return self.__state

    def update(self, neighbours):
        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented an update method yet.')

    def draw(self):
        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented a draw method yet.')
