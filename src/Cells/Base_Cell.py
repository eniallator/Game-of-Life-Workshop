class Base_Cell:
    """The base class for all cell types"""
    _dead = False
    _neighbour_radius = 1

    @classmethod
    def try_spawn(cls, neighbours):
        raise Exception('Error: ' + cls.__name__ + ' implemented a try_spawn method yet.')

    @classmethod
    def get_neighbour_radius(cls):
        """Gets the radius for how many neighbours per cell"""
        return cls._neighbour_radius

    @property
    def is_dead(self):
        """Returns True if the cell is dead, False otherwise"""
        return self._dead

    def update(self, neighbours):
        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented an update method yet.')

    def draw(self):
        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented a draw method yet.')
