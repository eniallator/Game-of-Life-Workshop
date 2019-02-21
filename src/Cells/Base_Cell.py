class Base_Cell:
    """The base class for all cell types"""
    _dead = False
    _neighbour_radius = 1

    @classmethod
    def try_spawn(cls, neighbours):
        """The method called when trying to spawn a cell

        Parameters
        ----------
        neighbours : list
            A 2D list containing the grid of cells around the current cell

        Raises
        ------
        Exception
            When not overridden, this will raise an error saying to override this method.
        """

        raise Exception('Error: ' + cls.__name__ + ' implemented a try_spawn method yet.')

    @classmethod
    def get_neighbour_radius(cls):
        """Gets the radius for how many neighbours per cell

        Returns
        -------
        int
            The radius
        """

        return cls._neighbour_radius

    @property
    def is_dead(self):
        """Returns True if the cell is dead, False otherwise

        Returns
        -------
        bool
        """

        return self._dead

    def update(self, neighbours):
        """
        The update method that's called every tick. Meant to be overridden.

        Parameters
        ----------
        neighbours : list
                2D list filled with cell objects or None

        Raises
        ------
        Exception
            When not overridden, this will raise an error saying to override this method.
        """

        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented an update method yet.')

    def draw(self):
        """The draw method that's called every time the game needs to be rendered. Meant to be overridden."""
        raise Exception('Error: ' + self.__class__.__name__ + ' hasn\'t implemented a draw method yet.')
